#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
from getTwitterHandles import getTwitterHandles

#Twitter API credentials (expired, don't even try it)
consumer_key = "1H09Gu7nLBOY8aLr5MRpztb7u"
consumer_secret = "2fxngnfykmnV9o3FDy7pE0nAiLQpMHiUpre0vV7mustBNIL8QO"
access_key = "908720691889020928-vg1LwKaItsSy5ivk4QKcqL4S4UfhFht"
access_secret = "OU74GrCrWuJmLQRwevqUk5UObZnx9bWctEr8aGUt6T39N"


def get_all_tweets(screen_name):
	print("Getting tweets from @" + str(screen_name))

	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("Getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % (len(alltweets)))

	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
	
	#write the csv	
	with open('./Tweets/%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	handles = getTwitterHandles()
	
	startHere = 0
	for i in range(len(handles)):
		if handles[i]=="petertoddbtc":
			handles[i]="peterktodd"
			startHere = i

	for i in range(startHere, len(handles)):
		get_all_tweets(str(handles[i]))



#	for handle in handles:
#		get_all_tweets(str(handle))


