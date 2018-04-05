# Dependencies
import numpy as np
import tweepy
import time
import json
# Twitter API Keys
consumer_key = "evHVYPKDjAJ0JAitpY49z7KJ4"
consumer_secret = "MpG65nQZOuf0ErIyEtaUDPA0J8aI2qIdGRcbeLmgIpXuOXbCKM"
access_token = "979169626012631041-vEFBfFZ1FCam3j9lRdqcMwn27aA2puX"
access_token_secret = "I1AJRehHaXYZbfuYs1x64hVth0nzKALMhMLxOjU2pkSmN"
# Target Term
target_term = "@T0B1Z"
# Opening message
print("We're going live!")
# Create Thank You Function
def ThankYou():
    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")
    # Loop through all tweets
    for tweet in public_tweets["statuses"]:
        
        
        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]
        tweet_text = tweet["text"]
      
        # Print the tweet_id
        print(tweet_text)
        print(tweet_author)
        # Use Try-Except to avoid the duplicate error
        try:
            
            api.update_status(f"{tweet_author}thank you, come again")
            
        except: 
            (f"{tweet_author}What did you call me!?")
            # Print success message
    print("success!")
            # Print message if duplicate
    print("This is a duplicate!")
        # Print message to signify complete cycle
    print("complete")  
    while(True):
    
    ThankYou()
    
    time.sleep(60)


Add CommentCollapse 

Message Input

Message @Alexandra Olivier