# Advance Capstone Project - Aetheria ✨
![Chatbot Aetheria](mainpage.gif)

You can open the application via this HTTP link:
**http://team5-alb-1402898587.ap-southeast-1.elb.amazonaws.com/**

Alternatively, you can access the application with streamlit:
[Click here to access the Chatbot Aetheria](https://capstone-aetheria.streamlit.app/)

## 📚 Overview
Welcome to the Aetheria Chatbot Repository! Aetheria is a helpful project for career planning, offering tips on resumes, CV guides to pass ATS, job recommendations based on skills and experience, as well as networking tips. This project supports users in achieving their career goals more effectively.

## 🤖 Features
- **Read File Capability**: Enables file uploads with basic explanations for easy understanding.
- **Save Conversation**: Allows users to save and revisit past chats for reference.
- **Response Control**: Enables control over the length of responses by adjusting tokens per message.
- **Customizable Creativity**: Provide temperature settings to fine-tune the chatbot's response creativity.
- **User-Friendly Interface**: Developed using Streamlit to ensure an intuitive and engaging experience.
- **Conversation Management**: Allows switching between bot behaviors and retrieving past conversations using SQLAlchemy.

## ⚙️ Installation
1. Clone the Repository
```
git clone https://github.com/aismaanly/capstone-aetheria.git
cd capstone-aetheria.git
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Get Your TogetherAI API Key
To enable AI functionality in the app, you’ll need an API key from TogetherAI. Register for an account at [Together AI – Fast Inference, Fine-Tuning & Training](https://www.together.ai/)
4. Configure Your .env File  
Find the `.env.sample` file in the root directory of the project. Rename it to `.env`, open the file, and set the `TOGETHER_API_KEY` value to the API key you received from TogetherAI.  

## 💻 Usage
1. **Start the Chatbot Application**:
    ```
    streamlit run main.py
    ```
2. **Interact with the chatbot**:
    - Launch the application in your browser.
    - Use the sidebar to start a new conversation or access a previously saved one.
    - Enter your messages in the input field and receive instant responses from the chatbot.
    - Upload files by drag, drop, or selecting file with certain file type.

This will launch the chatbot on your local machine at at `http://localhost:8501`. Open the displayed URL in your web browser to start interacting with the chatbot.

## 📖 Appendix 
- **Streamlit**: A framework designed to build interactive web applications directly from Python scripts. 
- **AWS EC2 Instance Architecture**: A cloud-based solution enabling secure and scalable application deployment.  
- **SQLAlchemy**: A versatile library for database operations, supporting both ORM and raw SQL queries.  
- **Tiktoken**: A high-performance tokenizer optimized for seamless integration with OpenAI models.  
- **OpenAI**: Advanced AI models that facilitate natural language processing and conversational AI tasks.  
- **Fitz (PyMuPDF)**: A robust tool for handling and extracting content from PDF files.  
- **python-docx**: A library for creating, modifying, and extracting data from Word documents.  
