from urllib import request
import requests
from bs4 import BeautifulSoup

# In this simple web scraping project i will be scraping the-
# records of the presidential briefings and statements from the white house

# Purpose: extract all the links on the page that point to the briefings and-
# statements.

# step 1: first thing is to access the website
result = requests.get('https://www.whitehouse.gov/briefing-room/')

# step 2: store the contents of the webpage in variable.
src = result.content

# step 3: create a soup object that allows me to parse the src
soup = BeautifulSoup(src, 'lxml')

# step 4: create an empty list that i will populate with the links i want
# i want to loop through all the links.
urls = []
# since i inpected the webpage and found that the h2-tag contains the links,
# i will loop throgh the h2 tags. .find_all() returns a list of all the h2 tags
for h2_tag in soup.find_all('h2'):
  # now inside the h2 tag, there is a <a tag. i want that as well
  # this will return a single element and stores it in the a_tag variable.
  a_tag = h2_tag.find('a')
  
  # here i use the if statement because i was getting the AttributeError: 'NoneType' object has no attribute 'attrs'
  # upon further analysis, i found the error to be the list returns two items that are empty for some reason.
  if a_tag is not None:
    # now i add the a_tag to the urls list. but i also include its attribute.
    urls.append(a_tag.attrs['href'])

print(urls)