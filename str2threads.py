from re import T
import tweepy
from tweepy.models import Status

consumer_key = "o6xdGFbZ5Yls1PHUbjoYNiE5X"
consumer_secret = "07Yw1bFwNLZE8FavT5vmImycuwn6TEkJRTWWCU1RscYGOWZXol"

access_token = "848488981-oaRJQoSK3mvyFnioMxVVvyATuM8hzPmCGjzX1pxB"
access_token_secret = "mPtaaKygZ5ZIkf78J2R2UKKNKVt5dafWr1U4V3DjhtS5m"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.get_user("mrfiddl3")

# print(user.name)
# print(user.description)
# print("--------------------")
# print("Followers:")

def textToThread(txt):

    if (len(txt) % 280) != 0:
        numOfTweets = (len(txt) // 280) + 1
    else:
        numOfTweets = len(txt) / 280

    left = 0
    right = 0
    buffer = 1
    not_buffer = 0

    prv_tweet = 0

    for i in range(numOfTweets):
        if left > len(txt) or right > len(txt):
            break
        left = right
        right = right + 280
        try:
            if not_buffer == 0:
                tweet = api.update_status(status = txt[left:right] + "-")
                prv_tweet = tweet.id_str
                not_buffer = not_buffer + 1
            else:
                tweet = api.update_status(status = txt[left:right] + "-", in_reply_to_status_id = prv_tweet, auto_populate_reply_metadata=True)
                prv_tweet = tweet.id_str
                not_buffer = not_buffer + 1
            continue
        except:
            if not_buffer == 0:
                right = right - 50
                tweet = api.update_status(status = txt[left:right] + "-")
                prv_tweet = tweet.id_str
                not_buffer = not_buffer + 1
            else:
                right = right - 50
                tweet = api.update_status(status = txt[left:right] + "-", in_reply_to_status_id = prv_tweet, auto_populate_reply_metadata=True)
                prv_tweet = tweet.id_str
                not_buffer = not_buffer + 1
            continue    

tweet = "Este último año me he dado cuenta de que las personas a las que se le dificulta el uso de tecnología como computadoras / celulares (por lo general personas de 40+ años) tienden a tener un miedo a equivocarse mucho más grande que las personas que no se les dificulta la tecnología. Por esto mismo es que tienden a pedir ayuda a personas que saben que si le saben al tema en vez de buscar soluciones por su cuenta, porque les da miedo moverle y que dejen peor las cosas por más minima que sea, al menos esto pasa con mi papá y mi mamá. Siempre se me han hecho curiosas las diferencias generacionales. Muchas de estas personas se asombran cuando alguien les soluciona el problema que tenian y los ven como super genios, cuando en realidad muchas de las cosas las sabemos nomás por moverle y dar con lo que queremos o con una simple busqueda en Google xd"

print(tweet)
textToThread(tweet)