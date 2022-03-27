import requests
from bs4 import BeautifulSoup
import lxml

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

    #inspect the items for the search for tags and classes

items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
count = 1
for item in items:
    itemName = item.find("h4", class_='card-title').text.strip("\n")
    itemPrice = item.find("h5").text

    print("%s ) Price: %s, Item Name: %s" % (count, itemPrice, itemName))

    count = count + 1


"""Scraping paginated/multi-page content"""

    #collect all the page urls and store them in a list
pages = soup.find("ul", class_="pagination")
urls = []
links = pages.find_all("a", class_="page-link")

    #iterate through all the page-link element & convert their text to integers for the comparison to avoid dublication
for link in links:
        #check if the link's text property can be converted into digits
    pageNum = int(link.text) if link.text.isdigit() else None  #at this point the else will be triggered when the pageNum will be = next or previous else otherwise

        #if pageNum != None the grab "href" attribute and append it to our url's list
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

print(urls)
    #now lopp through each url in our list
count = 1
for i in urls:
        #adding it to our existing base url then create a new request for scraping the page
    newURL = url + i
    response = requests.get(newURL)
    soup = BeautifulSoup(response.text, "lxml")

        # inspect the items for the search for tags and classes

    items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    for item in items:
        itemName = item.find("h4", class_='card-title').text.strip("\n")
        itemPrice = item.find("h5").text

        print("%s ) Price: %s, Item Name: %s" % (count, itemPrice, itemName))

        count = count + 1