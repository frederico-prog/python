import oauth2
import urllib.parse
import json


class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.con(consumer_key, consumer_secret, token_key, token_secret)

    def con(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.client = oauth2.Client(self.consumer, self.token)

    def tweet(self, novo_tweet):
        query_decode = self.parser(novo_tweet)
        request = self.client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_decode,
                                 method='POST')
        decode = request[1].decode()
        object = json.loads(decode)
        return object

    def search(self, query, lang):
        query_decode = self.parser(query)
        request = self.client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_decode + '&lang=' + lang)

        decode = request[1].decode()

        object = json.loads(decode)
        twittes = object['statuses']
        return twittes

    def parser(self, text):
        query_decode = urllib.parse.quote(text, safe='')
        return query_decode