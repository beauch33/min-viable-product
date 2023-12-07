#!/usr/bin/env python3

import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import db, SentimentData
from sentiment.analysis import analyze_sentiment
from src.models import db, SentimentData

app = Flask(__name__)

# Use PostgreSQL database on Heroku, fallback to SQLite for development
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///sentiment_analysis.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for now

# Initialize SQLAlchemy
db.init_app(app)

# Create tables based on the defined models
with app.app_context():
    db.create_all()

@app.route("/")
def main():
    return '''
     <form action="/analyze_sentiment" method="POST">
         <label for="company_name">Enter Company Name:</label>
         <input type="text" id="company_name" name="company_name" required>
         <input type="submit" value="Submit">
     </form>
     '''

@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment_route():
    company_name = request.form.get("company_name", "")
    
    # Example: Save sentiment data to the database
    sentiment_score = analyze_sentiment(company_name)
    save_sentiment_data(company_name, sentiment_score)
    
    return f"Sentiment analysis for {company_name}"

def save_sentiment_data(company_name, sentiment_score):
    # Save sentiment data to the database
    new_entry = SentimentData(company_name=company_name, sentiment_score=sentiment_score)
    db.session.add(new_entry)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)