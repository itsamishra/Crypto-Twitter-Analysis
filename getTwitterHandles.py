from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

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

	client.close()
	return twitterHandles


if __name__ == '__main__':
	getTwitterHandles()