# Resume-NLP-Screening-System

resume_nlp_system/
│
├── README.md
├── requirements.txt
├── Dockerfile
├── .gitignore
│
├── data/
│   └── sample_resumes/          # Sample PDF/DOCX resumes for testing
│
├── src/
│   ├── main.py                  # Flask app entry point
│   ├── parser.py                # Resume text extraction
│   ├── nlp_pipeline.py          # Keyword extraction, sentiment, scoring
│   ├── utils.py                 # Helper functions
│   └── config.py                # Config variables
│
├── models/
│   └── transformer_model/       # Pretrained sentiment model (HuggingFace)
│
└── notebooks/
    └── EDA_and_Testing.ipynb    # Exploratory notebook for testing NLP logic
