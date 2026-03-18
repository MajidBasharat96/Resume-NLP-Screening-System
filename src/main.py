from flask import Flask, request, render_template
from src.parser import extract_resume_text
from src.nlp_pipeline import score_candidate

app = Flask(__name__)

JOB_SKILLS = ['Python', 'Data Analysis', 'Machine Learning', 'SQL', 'NLP', 'Deep Learning']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    text = extract_resume_text(file)
    result = score_candidate(text, JOB_SKILLS)
    return result

if __name__ == "__main__":
    app.run(debug=True)
