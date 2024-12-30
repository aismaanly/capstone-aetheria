# Advance Capstone Project - Aetheria ✨
![Chatbot Aetheria](mainpage.gif)

You can open the application via this HTTP link:
**http://team5-alb-1402898587.ap-southeast-1.elb.amazonaws.com/**

Alternatively, you can access the application with streamlit:
**https://capstone-aetheria.streamlit.app/**

## 📚 Overview
Welcome to the Aetheria Chatbot Repository! Aetheria is a career consultation assistant designed to help you improve your chances of success in the job market. This app offers a variety of services, including creating CV ATS friendly, interview practice, job recommendations based on skills and experience, and networking strategies.

## 👾 Features
- User-friendly interface for a comfortable app experience  
- Ability to upload files and provide clear, easy-to-understand explanations  
- Access to previous conversations to avoid losing important information  
- Customizable chatbot response length, tailored to your needs (shorter or more detailed)  
- Adjustable creativity level for varied chatbot responses  
- Selection of different chatbot personalities to make conversations more engaging  
- AWS-powered app for reliable performance, even during high traffic  
- Resume creation in PDF format, ready to share or print after data entry  

## ⚙️ Installation
1. Clone the Repository
```
git clone https://github.com/aismaanly/capstone-aetheria.git
cd capstone-aetheria
```
2. Create a virtual environment (optional but recommended):
```
python -m venv env
```
3. Activate the Virtual Environment
```
.\env\Scripts\activate    # On Linux, use `source venv/bin/activate`
```
4. Install the required packages
```
pip install -r requirements.txt
```
3. Get Your TogetherAI API Key
To enable AI functionality in the app, you’ll need an API key from TogetherAI. Register for an account at [Together AI – Fast Inference, Fine-Tuning & Training](https://www.together.ai/)
4. Configure Your .env File  
Find the `.env.example` file in the root directory of the project. Rename it to `.env`, open the file, and set the `TOGETHER_API_KEY` value to the API key you received from TogetherAI.  

## 💻 Usage
1. **Run the Streamlit app**
    ```
    streamlit run main.py
    ```
2. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).
3. **Interact with the chatbot**
    - Use the sidebar to start a new conversation or access a previously saved one.
    - Navigate to the "Chatbot" section in the sidebar.
    - Enter your messages in the input field and receive instant responses from the chatbot.
    - Upload files by drag, drop, or selecting file with certain file type.
4. **Create CV ATS friendly**
    - Navigate to the "Buat CV" section in the sidebar.
    - Follow the step-by-step process to input your information:
        - Enter your name, contact details, and other personal information.
        - Add your academic qualifications, including degrees and institutions.
        - List your past job roles, responsibilities, and achievements.
        - Provide a list of relevant skills tailored to the job you're seeking.
    - In the final step, click "Generate Resume PDF" to create and download your CV ATS.

## 📖 Appendix 
- **Streamlit**: A framework designed to build interactive web applications directly from Python scripts. 
- **AWS EC2 Instance Architecture**: A cloud-based solution enabling secure and scalable application deployment.  
- **SQLAlchemy**: A versatile library for database operations, supporting both ORM and raw SQL queries.  
- **Tiktoken**: A high-performance tokenizer optimized for seamless integration with OpenAI models.  
- **OpenAI**: Advanced AI models that facilitate natural language processing and conversational AI tasks.  
- **Fitz (PyMuPDF)**: A robust tool for handling and extracting content from PDF files.  
- **Python Docx**: A library for creating, modifying, and extracting data from Word documents.  
- **ReportLab**: A library for generating PDFs, used for creating styled documents, including features such as paragraphs, tables, and page formatting.