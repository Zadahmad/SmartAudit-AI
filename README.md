# 🧠 SmartAudit AI Backend

SmartAudit AI is a backend application that allows users to upload financial or tax-related documents (like invoices), extract text from them using OCR tools, and analyze the content using LLMs (OpenAI or Anthropic Claude) to summarize or interpret key information.

---

## 🚀 Features

- 🧾 **PDF Upload**: Extracts text from PDF invoices using `pdfplumber`
- 🤖 **LLM Analysis**: Analyzes extracted text with OpenAI (`gpt-4`, `gpt-4o`) or Anthropic (`claude-3-opus`, etc.)
- ⚙️ **REST API**: Built with FastAPI
- 🐳 **Dockerized**: Easily run with Docker & Docker Compose
- ✅ **CI/CD**: GitHub Actions workflow for automated testing

---

## 📁 Project Structure

```bash
.
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── upload.py
│   │   └── analyze.py
│   ├── services/
│   │   ├── file_handler.py
│   │   └── llm_agent.py
│   └── models/
│       └── schemas.py
├── tests/
│   ├── test_upload.py
│   └── test_analyze.py
├── sample-data/
│   └── invoice_sample.pdf
├── .github/workflows/ci.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── .env
``` 
---

## 🔧 Installation
1. Clone the Repository
```bash

git clone https://github.com/your-username/smartaudit-ai-backend.git
cd smartaudit-ai-backend
``` 
2. Setup Virtual Environment
```bash

python -m venv venv
venv\Scripts\activate  # On Windows

 OR

source venv/bin/activate  # On Mac/Linux
``` 
3. Install Dependencies
```bash

pip install -r requirements.txt
``` 

## 🔐 Environment Setup


Create a .env file in the project root:

env

```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
``` 

## 🧪 Testing the API (via Swagger UI)
Start the app:

```bash

uvicorn app.main:app --reload
Open your browser at: http://127.0.0.1:8000/docs

Use:

POST /upload/ to upload a PDF and extract text

POST /analyze/ to analyze the extracted text using OpenAI or Anthropic
``` 
---
## 🐳 Docker Usage
Build & Run
```bash

docker-compose up --build
The app will be available at http://localhost:8000.
``` 
---
## ✅ Run Tests
```bash

pytest
Tests are located in the tests/ folder.
``` 
## 🤖 GitHub Actions CI
On every push to main, the workflow:

Sets up Python 3.10

Installs dependencies

Runs unit tests

Workflow file: .github/workflows/ci.yml

## 📄 Sample Invoice
You can find a sample invoice to test in:

```bash

sample-data/invoice_sample.pdf


---

## 📬 Contact

Developed by:

**Manouchehr Zadahmad Jafarlou**

✉️ Email: zadahmad@gmail.com  
🔗 GitHub: [github.com/zadahmad](https://github.com/zadahmad)

---

