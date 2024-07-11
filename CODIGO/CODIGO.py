import tweepy
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

with open("MENSAGEM.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    tweet_text = data["tweet_text"]

try:
    tweet = client.create_tweet(text=tweet_text)
    print("Tweet postado com sucesso!")
except tweepy.TweepError as e:
    print(f"Erro ao postar tweet: {e.response.text}")
except Exception as e:
    print(f"Erro inesperado: {e}")
