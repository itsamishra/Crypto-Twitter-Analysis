from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

exampleText = "Hello Mr. Bob, how are you doing today? The weather is great and python is awesome."
#print(word_tokenize(exampleText))
stopWords = set(stopwords.words("english"))

print(stopWords)