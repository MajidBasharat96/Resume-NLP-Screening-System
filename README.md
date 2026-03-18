# Resume-NLP-Screening-System

## Overview
Automated system to parse resumes, extract skills, evaluate experience, and perform sentiment analysis on text data. Designed for recruiters and AI HR products.

## Features
- Extract text from PDF & DOCX resumes
- Detect relevant skills & experience
- Sentiment analysis on cover letters or summary sections
- Candidate scoring system
- Flask web interface
- Production-ready, Docker-enabled

## Tech Stack
- Python, Flask
- NLP: spaCy, NLTK, Transformers
- PDF/DOCX Parsing
- Docker

## Setup
1. Clone the repository:
```bash
git clone https://github.com/<username>/resume_nlp_system.git
cd resume_nlp_system
Install dependencies:

pip install -r requirements.txt
python -m spacy download en_core_web_sm
Run the Flask app:

python src/main.py
Visit http://127.0.0.1:5000 and upload a resume.

Docker
docker build -t resume_nlp .
docker run -p 5000:5000 resume_nlp
Sample Data
Place PDF/DOCX resumes in data/sample_resumes/ for testing.
