# Crypto-Twitter-Analysis

## Purpose

An analysis of the tweets of the "100 most influential people in crypto" (found here: https://cryptoweekly.co/100/).

I plan on comparing how different Bitcoin thought leaders (Roger Ver, Jameson Lopp, etc.) feel about various Bitcoin controversies (e.g. Bitcoin Cash, SegWit/SegWit2X, etc.)

## Directory/File Functionality

./Tweets:	CSV documents containing last ~3000 tweets for corresponding account

getTwitterHandles.py:	Gets handles from https://cryptoweekly.co/100/

tweetDump.py:	Creates CSV containing last ~3000 tweets for user

createHandleNames.py:	Creates dictionary {Name:Twitter Handle} and pickles (serializes) it

handleNamePair.pickle: 	Pickle of {Name:Twitter Handle} dictionary

Analysis.ipnb:	Analysis of tweets