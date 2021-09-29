import tweepy
from decouple import config

def obtenerTwitters(keywords,cant):
    access_token=config('access_token')
    access_token_secret=config('access_token_secret')
    consumer_key=config('consumer_key')
    consumer_secret=config('consumer_secret')

    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    words = ""
    for key in keywords:
        words += f"{key} OR "

    search_words = words

    tweets = api.search_tweets(q=search_words,lang="es",result_type="recent",count=cant)
    return tweets
    # for tweet in tweets:
    #     print(f"created_at: {tweet.created_at}\nuser: {tweet.user.screen_name}\ntweet text: {tweet.text}\ngeo_location: {tweet.user.location}\nurl: https://twitter.com/twitter/statuses/{tweet.id}")
    #     print("\n")