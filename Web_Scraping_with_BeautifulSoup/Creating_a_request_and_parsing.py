    #Import the libraries we'll be using

    #this library houses the "get" function, this process returns the reponse from the website containing the source code
import requests

    #these programs work in unity to create a navigable object that we can use to isolate specific data we want from website
from bs4 import BeautifulSoup

import lxml

    #get the website's address and save it as a variable
url = "https://quotes.toscrape.com/"

response = requests.get(url)

    # now parse the html document, for this we'll use "beautifulsoup" & "lxml"

    #we are parsing response's text attribute letting bs4 know we want to use "lxml" parser
soup = BeautifulSoup(response.text, 'lxml')

#print(soup) #to check what whether soup worked fine or not

'''How to Isolate data'''

    #the function we'll use is the "find_all" function which hones in on the tag and class we specify
    #quotes now contains a list of all the elements on the HTML website with the tag, span and a class "text"
quotes = soup.find_all('span', class_= 'text')
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")
print("\n")
    #clean the data a bit
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)

    quoteTags = tags[i].find_all("a", class_="tag")
    for quoteTag in quoteTags:
        print(quoteTag.text)

    print("\n")
    #scraped