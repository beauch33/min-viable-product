# test_sentiment.py

import unittest
from your_app.sentiment import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment_positive(self):
        result = analyze_sentiment("This is a positive statement.")
        self.assertEqual(result, 'positive')

    # Add more test cases as needed