from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pickle

# Creates dictionary {Name:Twitter Handle} and pickles it
def getTwitterHandles():
	# Fill in with url of page which is to be scraped
	url = "https://cryptoweekly.co/100/"

	# Retreives and parses page html
	client = urlopen(url)
	pageHtml = client.read()
	pageSoup = soup(pageHtml, "html.parser")

	#print(pageSoup)
	profiles = pageSoup.findAll("div", {"class":"testimonial-wrapper"})
	twitterHandles = []
	for person in profiles:
		twitterHandles.append(person.findAll("div",{"class":"author"}))

	for i in range(len(twitterHandles)):
		twitterHandles[i]=twitterHandles[i][0].findAll("a")[0].text[1:]

	# Edits Peter Todd's old handle to new handle
	for i in range(len(twitterHandles)):
		if twitterHandles[i]=="petertoddbtc":
			twitterHandles[i]="peterktodd"
			break

	twitterNames = []
	for person in profiles:
		twitterNames.append(person.h3.text)


	client.close()
	
	handleNamePair = {}
	for i in range(len(twitterHandles)):
		handleNamePair[str(twitterNames[i])]=twitterHandles[i]

	pickle.dump(handleNamePair, open("handleNamePair.pickle", "wb" ))


if __name__ == '__main__':
	getTwitterHandles()