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