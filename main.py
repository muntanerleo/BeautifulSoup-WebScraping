import requests
from bs4 import BeautifulSoup

# using he requests module, i use the 'get' function provided to access-
# the webpage provided as an argument to this function below:
result = requests.get('https://journeyorl.com')

# i need to make sure the webpage is accessible.
# i do this by making sure i get back a 200 OK response when-
# i runt the program. i need to use the .status_code method to check
# print(result.status_code)

# i can also check the HTTP header of the website to-
# verify that i have accessed the correct page. (.headers method does this)
# print(result.headers)

# now i can extract and store the contents of the page from requests-
# to a variable.
src = result.content

# now that i have the page source stored, i will use the beautifulsoup-
# module to parse and process the source.
# to do this i need to create a beautifulsoup object based on the source-
# variable i created above:
# beautifulsoup creates this object from the source and lets me extract the data i want.
# now my variable 'soup' has the content
soup = BeautifulSoup(src, 'lxml')

# now that the page source has been processed through BeautifulSoup-
# i can access specific info directly from it. for example-
# if i want to see a list of all the links on the page:
# by using the .find_all method, i can pass in the argument 'a'-
# which will give me all the a-tags from the page and store them in the links variable. 
links = soup.find_all('a')
# print(links)
# print('\n')
# after running the above code i can see that the a-tags were ruturned as a list.
# the contents of the list are all the a-tags

# maybe i want to to extract the link that contains the text 'About'
# instead of every link. i can use the built-in 'text' function to access-
# the text content between the <a> </a> tags
# i do this by looping through all the links i have obtained from above.
for link in links:
  # as i am looping through the links in the list, all those elements in the list are-
  # BeautifulSoup element. that allows me to call the .text fucntion on each of those elements.
  if 'Give' in link.text:
    # what i'm saying here is "look at the text and if the word About is present, then printout the link"
    # and what it goes too. .attrs gives me the contents of the href as well.
    print(link)
    print(link.attrs['href'])