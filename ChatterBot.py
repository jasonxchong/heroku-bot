# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "uOF1mT0SLO9S8zMeGhqkJra8v"
consumer_secret = "mI0QoCTbCBTLo9sMj7PgdimiW7AnXQXnFE46daqt4HidleL6RD"
access_token = "969399623415562240-jPmZQZagnYGw8igneV1Dc8dzzGJSseG"
access_token_secret = "JZCG8RfGTf5HbYe8k5drmpqpQQIX2rm4YxTG4jB67lqIA"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE