import pandas as pd

# Measures apathy towards Bitcoin Cash (0 to 1, 0=low apathy, 1=high apathy)
def bchApathyIndex(df):
    # Creates search terms and counters
    bitcoinCashsearch1 = "bitcoincash"
    bitcoinCashsearch2 = "bitcoin cash"
    bcashSearch = "bcash"
    bitcoinCashCounter=0
    bcashCounter=0

    # Iterates over all tweets
    for i in df["text"]:
        # Increments bitcoin cash
        if bitcoinCashsearch1 in i.lower():
            bitcoinCashCounter+=1
        # Increments bitcoin cash
        elif bitcoinCashsearch2 in i.lower():
            bitcoinCashCounter+=1
        # Increments bcash
        elif bcashSearch in i.lower():
            bcashCounter+=1
    
    # Calculates total # of mentions
    totalMentions = bcashCounter+bitcoinCashCounter
    
    # If individual has mentioned bch, calculates apathy index value
    if totalMentions!=0:
        index = bcashCounter/totalMentions
    # If individual hasn't mentioned bch, sets apath index value to zero
    else:
        index = 0
    return [index, totalMentions]

# Returns number of tweets which match keyword for all 100 twitter users
def searchTweets(df, keyword):
    matches = []
    keyword = keyword.lower()
    
    # Iterates over each twitter user
    for path in df["Path To Tweets"]:
        counter = 0

        # Creates dataframe containing his/her tweets
        tempDf = pd.read_csv(path)

        # Iterates over tweets
        for tweet in tempDf["text"]:
            # If a tweet contains the keyword, increments counter
            if keyword in tweet.lower():
                counter+=1

        # Adds number of tweets which match keyword for current user to 'matches' array
        matches.append(counter)
    
    return matches


''' For testing purposes
import pickle
import pandas as pd

temp = pickle.load(open("temp.pickle", "rb"))
searchTweets(temp, "segwit")
'''