from re import T
import tweepy
from tweepy.models import Status

# I forgot to remove these tokens before uploading my project to GitHub hehe, so even if I delete them and push
# the changes to my repo they could still be found on the initials commits, so y'all know my old tokens now xD.

# PD: THIS IS AN HORRIBLE WAY TO READ YOUR TOKENS WHILE WORKING WITH APIS AS YOU CAN SEE, SO DON'T DO IT.

consumer_key = "o6xdGFbZ5Yls1PHUbjoYNiE5X" # I can explain this! Read the comments above to know why this is here on a public repo
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

with open('tweet.txt', encoding ='utf8') as f:
    tweet = f.read()
    f.close()

print(tweet)
textToThread(tweet)