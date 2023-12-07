# import requests

# def fetch_article_data(company_name):
#     # Replace "YOUR_API_URL" with the actual API endpoint
#     url = f"https://YOUR_API_URL/{company_name}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         # Extract relevant information from the API response
#         text = data.get("text")
#         sentiment_score = analyze_sentiment(text)
#         source_url = data.get("url")
        
#         # Create and save the article data
#         article = ArticleData(text=text, sentiment_score=sentiment_score, source_url=source_url)
#         db.session.add(article)
#         db.session.commit()
#     else:
#         print(f"Error fetching data for {company_name}")