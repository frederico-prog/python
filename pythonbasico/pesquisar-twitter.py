import oauth2
import json
import urllib.parse


consumer_key = 'WRXnyJds71yDayQaXFxPpI2jv'
consumer_secret = 'AjpaogRVFUyuZTfvaNgwj08J0pD3n6f1k08BjUUlapnUFca2w4'

token_key = '799122088594460672-vzJloX2qozKzEuJhNuyB1oew8rJSEzF'
token_secret = 'COd1bb65SodeBgD7zPTseuZ9lUBpkeeapROr0MXFprlqz'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

query = str(input("Pesquisa: ")).lower().strip()
query_decode = urllib.parse.quote(query, safe='')
request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_decode + '&lang=pt')

decode = request[1].decode()

object = json.loads(decode)
twittes = object['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()
