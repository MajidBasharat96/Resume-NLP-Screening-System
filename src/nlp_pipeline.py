import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
import re

nlp = spacy.load('en_core_web_sm')
sia = SentimentIntensityAnalyzer()

def extract_skills(text, skill_set):
    text = text.lower()
    found_skills = [skill for skill in skill_set if skill.lower() in text]
    return found_skills

def extract_experience_years(text):
    pattern = r'(\d+)\s+(?:years|yrs)'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return sum([int(x) for x in matches]) if matches else 0

def analyze_sentiment(text):
    return sia.polarity_scores(text)

def score_candidate(resume_text, job_skills):
    skills = extract_skills(resume_text, job_skills)
    experience = extract_experience_years(resume_text)
    sentiment = analyze_sentiment(resume_text)
    
    score = len(skills)*10 + experience*5 + sentiment['compound']*10
    return {
        'skills_found': skills,
        'experience_years': experience,
        'sentiment': sentiment,
        'score': round(score, 2)
    }
