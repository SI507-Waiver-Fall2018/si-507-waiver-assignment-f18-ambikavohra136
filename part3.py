# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

site_url = "https://www.michigandaily.com/"
soup = BeautifulSoup(requests.get(site_url).content, 'html.parser')

#print(soup.prettify()) 

#drill down to most read div
mostReadSection = soup.find("div", attrs={'class': 'view-most-read'})

#drill down to most read ol
mostReadList = mostReadSection.find("ol")


#drill down to most read titles
mostReadTitles = mostReadList.find_all("li")


#print title
print("Michigan Daily -- MOST READ")

#iterate thorugh titles
for title in mostReadTitles:
	#print the link text
	print(title.find('a').text.strip())

	try:
		articleContent = BeautifulSoup(requests.get(site_url + title.find("a")['href']).content, 'html.parser')
		#print(articleContent.prettify())
		author= articleContent.find("div", attrs = {"class":"byline"}).find("div", attrs = {"class":"link"}).find('a').text.strip()
		print("by " + author)

	except:
		print("Daily staff writer")