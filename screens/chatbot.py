from openai import OpenAI
import tiktoken
import requests
import os
import streamlit as st
import fitz
from docx import Document
import base64
from src.database import SessionLocal, Conversation
import uuid

DEFAULT_API_KEY = os.getenv("API_KEY")
DEFAULT_BASE_URL = os.getenv("BASE_URL")
DEFAULT_MODEL = os.getenv("MODEL")
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 500
DEFAULT_TOKEN_BUDGET = 4096

class ConversationManager:
    def __init__(self,chat_id=None, api_key=DEFAULT_API_KEY, base_url=DEFAULT_BASE_URL, model=DEFAULT_MODEL, temperature=DEFAULT_TEMPERATURE, max_tokens=DEFAULT_MAX_TOKENS, token_budget=DEFAULT_TOKEN_BUDGET):
        self.chat_id = chat_id
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_budget = token_budget
        self.system_message = "Halo! Saya Aetheria, asisten konsultasi karir Anda. Ada yang bisa saya bantu hari ini?"
        self.additional_role_play = ""
        self.conversation_history = self.load_conversation_history() or [{"role": "system", "content": self.system_message}]

    def update_system_message(self, system_message, additional_role_play):
        self.system_message = system_message
        self.additional_role_play = additional_role_play
        self.reset_conversation_history(preserve_history=True)

    def load_conversation_history(self):
        """Load conversation history from SQLite database."""
        session = SessionLocal()
        try:
            # Query the conversation history from the database for the given chat_id
            conversations = session.query(Conversation).filter(Conversation.chat_id == self.chat_id).all()
        except Exception as e:
            print(f"Error loading conversation history: {e}")
            conversations = []
        finally:
            session.close()

        # Return the conversation history as a list of dicts (role and content)
        history = [{"role": c.role, "content": c.content} for c in conversations]
        return history

    def count_tokens(self, text):
        try:
            encoding = tiktoken.encoding_for_model(self.model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(text)
        return len(tokens)
    
    def total_tokens_used(self):
        try:
            return sum(self.count_tokens(message['content']) for message in self.conversation_history)
        except Exception as e:
            print(f"Error calculating total tokens used: {e}")
            return None
    
    def enforce_token_budget(self):
        try:
            while self.total_tokens_used() > self.token_budget:
                if len(self.conversation_history) <= 1:
                    break
                self.conversation_history.pop(1)
        except Exception as e:
            print(f"Error enforcing token budget: {e}")

    def save_message_to_db(self, role, content):
        """Save a single message to the database, filtering out file-related content."""
        session = SessionLocal()
        
        # Filter out messages that contain file-related content
        if "Additional context from file:" in content:
            print("Ignored message: contains file content")
            return  # Skip saving this message to the database
        
        try:
            conversation_entry = Conversation(
                chat_id=self.chat_id, 
                role=role, 
                content=content
            )
            session.add(conversation_entry)
            session.commit()
            print(f"Message saved to DB: {content}")
        except Exception as e:
            print(f"Error saving message to DB: {e}")
            session.rollback()
        finally:
            session.close()

    def chat_completion(self, prompt, temperature=None, max_tokens=None, model=None):
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens
        model = model if model is not None else self.model

        self.conversation_history.append({"role": "user", "content": prompt})
        self.save_message_to_db("user", prompt)
        self.enforce_token_budget()

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=self.conversation_history,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})
        self.save_message_to_db("assistant", ai_response)
        return ai_response
    
    def reset_conversation_history(self, preserve_history=True):
        system_message_entry = {"role": "system", "content": self.system_message + "\n\n" + self.additional_role_play}
        if preserve_history:
            if self.conversation_history:
                self.conversation_history[0] = system_message_entry
            else:
                self.conversation_history.append(system_message_entry)
        else:
            self.conversation_history = [system_message_entry] + self.conversation_history[1:]

def apply_css():
    with open("src/style.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
        
apply_css()

def get_local_img(file_path: str) -> str:
    """Load an image and return its base64 encoded string."""
    try:
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""

def get_chat_message(contents: str, align: str = "left") -> str:
    """Menghasilkan balon percakapan dengan ikon."""
    div_class = "AI-chat"
    color = "#f1f0f0" 
    file_path = os.path.join("assets", "ai_icon.png")  

    if align == "right":  
        div_class = "user-chat"
        color = "#d1f7c4"
        file_path = os.path.join("assets", "user_icon.png")  

    src = f"data:image/png;base64,{get_local_img(file_path)}"

    icon_code = f"<img class='chat-icon' src='{src}' style='width: 30px; height: 30px; border-radius: 50%;' alt='avatar'>"
    formatted_contents = f"""
    <div class="{div_class}">
        {icon_code}
        <div class="chat-bubble">
            {contents}
        </div>
    </div>
    """
    return formatted_contents

def get_instance_id():
    """Retrieve the EC2 instance ID from AWS metadata using IMDSv2."""
    try:
        # Step 1: Get the token
        token = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=1
        ).text

        # Step 2: Use the token to get the instance ID
        instance_id = requests.get(
            "http://169.254.169.254/latest/meta-data/instance-id",
            headers={"X-aws-ec2-metadata-token": token},
            timeout=1
        ).text
        return instance_id
    except requests.exceptions.RequestException:
        return "Instance ID not available (running locally or error in retrieval)"

# Load all chats from the database
def load_all_chats():
    session = SessionLocal()
    try:
        chats = session.query(Conversation).all()
        session.close()
        grouped_chats = {}
        for chat in chats:
            if chat.chat_id not in grouped_chats:
                grouped_chats[chat.chat_id] = []

            if "Additional context from file:" not in chat.content:
                grouped_chats[chat.chat_id].append({"role": chat.role, "content": chat.content})
        
        return grouped_chats
    except Exception as e:
        print(f"Error loading chats from database: {e}")
        return {}
    finally:
        session.close()

#  delete a conversation from the database and update session state
def delete_conversation(chat_id, chat_index):
    session = SessionLocal()
    try:
        rows_deleted = session.query(Conversation).filter(Conversation.chat_id == chat_id).delete()
        session.commit()

        if rows_deleted > 0:
            print(f"Conversation with chat_id {chat_id} deleted from DB.")
        else:
            print(f"No conversation found with chat_id {chat_id}.")
        
        del st.session_state['chats'][chat_index]

        if chat_index >= len(st.session_state['chats']):
            st.session_state['chat_selection'] = None
        else:
            st.session_state['chat_selection'] = chat_index
        st.experimental_rerun()

    except Exception as e:
        print(f"Error deleting conversation: {e}")
        session.rollback()
    finally:
        session.close()
        
# delete a selected chat from session state using index
def delete_selected_chat(chat_index):
    if 0 <= chat_index < len(st.session_state['chats']):
        chat_id = st.session_state['chats'][chat_index]['chat_manager'].chat_id  
        delete_conversation(chat_id, chat_index)  
        st.session_state['chat_selection'] = None  

### Streamlit code ###
# Create three columns
col1, col2, col3 = st.columns([1, 3, 1])

# Displaying images in the center column
with col2:
    st.image("assets/cover_aetheria.png")
# Display EC2 Instance ID
instance_id = get_instance_id()

if 'chat_selection' not in st.session_state:
    st.session_state['chat_selection'] = None

# Initialize Session State for Chats
if 'chats' not in st.session_state:
    st.session_state['chats'] = []

    # Load all chats into session state
    all_chats = load_all_chats()
    for chat_id, history in all_chats.items():
        user_messages = [msg['content'] for msg in history if msg['role'] == 'user']
        topic = " | ".join(user_messages)[:30]  # Use user message preview for topic
        
        st.session_state['chats'].append({
            'chat_manager': ConversationManager(chat_id=chat_id),
            'conversation_history': history,
            'topic': topic  
        })

# Function to start a new chat
def start_new_chat():
    chat_id = str(uuid.uuid4())  
    st.session_state['chats'].append({
        'chat_manager': ConversationManager(chat_id=chat_id),  
        'conversation_history': [],
        'topic': 'Obrolan Baru'
    })  
    st.session_state['chat_selection'] = len(st.session_state['chats']) - 1
    st.session_state['file_used'] = False

# Chat selection
st.sidebar.title("Aetheria👾")
if st.sidebar.button("Obrolan Baru"):
    start_new_chat()

if len(st.session_state['chats']) > 0:
    chat_selection = st.sidebar.selectbox(
        "💬Pilih Obrolan",
        range(len(st.session_state['chats'])),
        index=st.session_state['chat_selection'] if st.session_state['chat_selection'] is not None else 0,
        format_func=lambda x: st.session_state['chats'][x]['topic']
    )
    st.session_state['chat_selection'] = chat_selection
else:
    chat_selection = None

# Button to delete the selected chat
if chat_selection is not None and st.sidebar.button("Hapus Obrolan yang Dipilih"):
    delete_selected_chat(chat_selection)   

# Function to summarize the conversation history
def summarize_conversation(conversation_history):
    user_messages = [msg['content'] for msg in conversation_history if msg['role'] == 'user']
    return " | ".join(user_messages)[:30]  

# Ensure chat_selection is not None
if chat_selection is not None and chat_selection < len(st.session_state['chats']):
    # Initialize the ConversationManager object for the selected chat
    current_chat = st.session_state['chats'][chat_selection]
    chat_manager = current_chat['chat_manager']
    conversation_history = current_chat['conversation_history']

    # File input from the user
    uploaded_file = st.file_uploader("", type=["txt", "pdf", "docx"])

    def read_file(file):
        try:
            if file.name.endswith(".txt"):
                return file.read().decode("utf-8")
            elif file.name.endswith(".pdf"):
                pdf_document = fitz.open(stream=file.read(), filetype="pdf")
                return ''.join([page.get_text() for page in pdf_document])
            elif file.name.endswith(".docx"):
                doc = Document(file)
                return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            else:
                return "Unsupported file format"
        except Exception as e:
            return f"Error reading file: {e}"
  
    if 'file_used' not in st.session_state:
        st.session_state['file_used'] = False 

    # Process the uploaded file
    file_content = None
    if uploaded_file and not st.session_state['file_used']:
        file_content = read_file(uploaded_file)
        if file_content:
            st.success("File berhasil diunggah. File akan diproses setelah Anda mengetik pesan.")

    # Chat input from the user
    user_input = st.chat_input("Tanyakan apa saja kepada Chatbot Aetheria!")

    # Call the chat manager to get a response from the AI
    if user_input:
        if file_content and not st.session_state['file_used']:
            prompt = f"{user_input}\n\nAdditional context from uploaded file:\n{file_content[:500]}..."
            st.session_state['file_used'] = True
        else:
            prompt = user_input

        response = chat_manager.chat_completion(prompt)

        conversation_history.append({"role": "user", "content": user_input})
        if file_content and not st.session_state['file_used']:
            conversation_history.append({"role": "system", "content": f"Context from file:\n{file_content}"})
        conversation_history.append({"role": "assistant", "content": response})

        # Update the chat topic based on the summary of all user inputs
        current_chat['topic'] = f"{summarize_conversation(conversation_history)}"

    # Display the conversation history
    for message in conversation_history:
        if message["role"] == "user":  
            st.markdown(get_chat_message(message["content"], align="right"), unsafe_allow_html=True)
        elif message["role"] == "assistant":  
            st.markdown(get_chat_message(message["content"], align="left"), unsafe_allow_html=True)

    # Chatbot Personalities
    with st.sidebar:
        st.divider()
        st.write("💡Kepribadian Chatbot")
        set_custom_message = st.selectbox("Pilih Kepribadian", ("Profesional👔", "Ramah😊", "Humoris😂"), key="system_message_selectbox")

        if set_custom_message == "Profesional👔":
            with open('src/professional.txt', 'r') as file:
                custom_message = file.read()
        elif set_custom_message == "Ramah😊":
            with open('src/friendly.txt', 'r') as file:
                custom_message = file.read()
        elif set_custom_message == "Humoris😂":
            with open('src/humorous.txt', 'r') as file:
                custom_message = file.read()

        additional_role_play = st.text_area("Ingin menambah suasana?", key="additional_role_play")

        def set_system_message():
            chat_manager.update_system_message(custom_message, additional_role_play)

        if st.button("Coba Ubah!", on_click=set_system_message):
            pass
        
        st.divider()

        # Settings
        st.write("⚙️Pengaturan")
        set_token = st.slider("Batas Kata Obrolan", min_value=10, max_value=500, value=DEFAULT_MAX_TOKENS, step=1, disabled=False)
        chat_manager.max_tokens = set_token

        set_temp = st.slider("Temperatur", min_value=0.0, max_value=1.0, value=DEFAULT_TEMPERATURE, step=0.1, disabled=False)
        chat_manager.temperature = set_temp

        # Ensure the system message is updated when the role is changed
        if st.session_state.get("system_message_selectbox") != set_custom_message:
            chat_manager.update_system_message(custom_message, additional_role_play)
            st.session_state["system_message_selectbox"] = set_custom_message
        st.divider()
        st.write(f"**EC2 Instance ID**: {instance_id}")

else:
    st.subheader("👾 Chatbot Aetheria!")
    st.markdown("👈 Silakan mulai obrolan baru atau pilih obrolan yang ada di sidebar.")