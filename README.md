# 🧠 AI Resume Screener

AI Resume Screener is a Streamlit-based web app that analyzes PDF resumes using LLMs to generate a job-fit score and suggest suitable roles. It uses OpenAI's API with LangChain for context-aware evaluation and Pinecone for vector search (e.g., skill-job match retrieval).


## Tech Stack
- Frontend/UI: Streamlit
- LLM: OpenAI (GPT-4 or GPT-3.5-turbo)
- Framework: Langchain
- Vector DB: Pinecone
- Parser: PyMuPDF / pdfminer / pdfplumber
- Backend Logic: Python
- Extras: tiktoken (token counting), dotenv (for secret management)

## Features
- Upload PDF resume
- Extract text using PyMuPDF
- Embed content and store in Pinecone
- Match against predefined job descriptions
- Get:
    - Job-fit score (0–100)
    - Suggested roles
    - LLM-generated feedback

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

Add your `.env` file with:
```
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_pinecone_environment
PINECONE_INDEX=your_pinecone_index_name

```

## Example Output
- Job Fit Score: 85/100
- Suggested Roles: ["Python Developer", "Backend Engineer", "ML Engineer"]
