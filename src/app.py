#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

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
def analyze_sentiment():
    company_name = request.form.get("company_name", "")
    return f"Sentiment analysis for {company_name}"