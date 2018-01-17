# Crypto-Twitter-Analysis

## Purpose

An analysis of the tweets of the "100 most influential people in crypto" (found here: https://cryptoweekly.co/100/)

## Directory/File Functionality

./Tweets:	CSV documents containing last ~3000 tweets for correponding account

getTwitterHandles.py:	Gets handles from https://cryptoweekly.co/100/

tweetDump.py:	Creates CSV containing last ~3000 tweets for user

createHandleNames.py:	# Creates dictionary {Name:Twitter Handle} and pickles it

handleNamePair.pickle: 	Pickle of {Name:Twitter Handle} dictionary

Analysis.ipnb:	Analysis on tweets