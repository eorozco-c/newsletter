import tweepy
from decouple import config
from .models import Noticia
from apps.medios.models import Medio

def obtenerTwitters(keywords,cant):
    access_token=config('access_token')
    access_token_secret=config('access_token_secret')
    consumer_key=config('consumer_key')
    consumer_secret=config('consumer_secret')

    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    

    tweets = api.search_tweets(q=keywords,lang="es",result_type="recent",count=cant)
    return tweets
    # for tweet in tweets:
    #     print(f"created_at: {tweet.created_at}\nuser: {tweet.user.screen_name}\ntweet text: {tweet.text}\ngeo_location: {tweet.user.location}\nurl: https://twitter.com/twitter/statuses/{tweet.id}")
    #     print("\n")

def GrabarTwitters(tweets,company,keyword):
    medio = Medio.objects.get(nombre__icontains="twitter")
    for tweet in tweets:
        if Noticia.objects.filter(url=tweet.id).exists():
            continue
        elif Noticia.objects.filter(contenido=tweet.text).exists():
            continue
        else:
            Noticia.objects.create(contenido = tweet.text,url = tweet.id,date = tweet.created_at,medio = medio,keyword = keyword,company = company)

