# # models.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class SentimentData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     company_name = db.Column(db.String(255))
#     sentiment_score = db.Column(db.Float)
#     timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# class ArticleData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String)
#     sentiment_score = db.Column(db.Float)
#     source_url = db.Column(db.String)
#     timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())