import random
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class sentenceBuilder:
    #vowels = ('a','i','e','o','u')
    def __init__(self):
        # set Twitter API keys
        self.consumer_key = 'YHH7gGaFW0vHZ23Mm9vXNrxIp'
        self.consumer_secret = 'FqwTk1DL0DLUbyAhXQF81lyVo6DRysTkEVIxhhZgK4OebptsUg'
        self.access_token = '496434978-Y8bhra1cqqggo806PvtYLelrbPhAhpHCSzlXGXQ2'
        self.access_secret = 'Zgme9RDOMrQLSyaQopqKfOIL85NnI8bRkjWDwqSeJKgan'
        # Below used by word_len_dict()
        self.word_freq = []
        self.temp_dict = {}
        self.perm_word_dictionary = {}

    def grab_twitter_feed(self):
        '''
        Takes in all words grabbed from twitter
        '''
        self.question_word = list()

        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth) # initiate tweepy API

        for status in tweepy.Cursor(api.home_timeline).items(2):
            # Process a single status
            pulled_tweet = status.text
            print pulled_tweet
            print "Pulled Tweet"
            self.word_len_dict(pulled_tweet)

    def add_to_perm_dict(self, passed_dict):
        #Doesn't take anything
        #Reads the dictionary created below to update the master dictionary after each execution

        for self.key,self.value in passed_dict:
            self.perm_word_dictionary[self.key] = self.value
            print key,value

    def word_len_dict(self, my_string):
        #Takes in string
        #Counts occurances of words
        #Adds them to a dictionary along with frequency

      self.wordlist = my_string.split()
      for w in self.wordlist:
          self.word_freq.append(self.wordlist.count(w))
          self.temp_dict[self.wordlist] = self.wordlist.count(w)

      master_string = str(zip(self.wordlist, self.word_freq))
      print master_string
      self.add_to_perm_dict(temp_dict)

sentenceBuilder().grab_twitter_feed()
