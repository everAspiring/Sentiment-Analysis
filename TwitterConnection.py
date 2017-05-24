import nltk
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s



#consumer key, consumer secret, access token, access secret.
ckey="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
csecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
atoken="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
asecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        #tweet = "SRH is the best team"
        #file = open("short_reviews/IPL.txt","w").write()
        #print file
        #print tweet
        #for line in tweet:
            #file.write(tweet)
            #print line
        #print file
        #file.close()
        
        sentiment_value, confidence = s.sentiment(tweet)
        print tweet, sentiment_value, confidence
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#IPL 2017"])


