import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# print(user)
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    

    # to like a tweet using the search_string
search_string = 'python'
numbersOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        # tweet.retweet()
        # tweet.follow()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


        # Generous Bot to follow back those following you
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'input_tweeter_name_here':
#         follower.follow()
#         break
    # print(follower.name)      # not neccessary anymore