# I Am Feeling Lucky Project

# To Execute:
# python3 IamFeelingLucky.py OOP

# This script opens the first 5 Google Search Results for the keyword 'OOP'


import bs4, requests, sys, webbrowser

rawSearch = []
if (len(sys.argv) < 2):
    print('What is to be Google\'ed?')
    sys.exit()
# sys.argv[1:] gets all the keywords entered in the terminal after the Python filename
for keyword in sys.argv[1:]:
    rawSearch.append(keyword)

# Creating a string of the arguments given in the terminal with a '+'
# in between every keyword
search = '+'.join(rawSearch)

# Concatenating 'search' and Google's URL gives us a valid Google Search
url = 'http://google.com/search?q=' + search

# Webpage is received in the form of a response object stored in 'res'
res = requests.get(url)

# Exception is raised if url is invalid
res.raise_for_status()

# The Document Object Model (DOM) of the webpage is then parsed
# and stored in soup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# All <a> tags whose parent tag has the class 'r' are stored in 'links'
# In simpler terms, the Google Search Result URLs are stored in 'links'
links = soup.select(' .r a')

# Opening only first 5 links
for i in range(5):
    # The webbrowser module opens the links in your favorite web browser
    webbrowser.open('http://google.com'+ links[i].get('href'))