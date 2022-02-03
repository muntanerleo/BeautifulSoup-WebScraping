from bs4 import BeautifulSoup

# in this project i create certain objects in BeautifulSoap.
# then i will extract content from these objects from web resources i am interested in.

# to keep things simple, i used the following HTML code.
# the string will represent a simple HTML webpage 
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upona time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

# write the content to a file
with open('index.html', 'w') as f:
  f.write(html_doc)

# create a soup object. this will allow me to parse the html content
soup = BeautifulSoup(html_doc, 'lxml')

# one cool function is .prettify(). it outputs the html in a nice way
# print(soup.prettify())

# finds the first occurence for a 'b' bold tag and prints it.
# print(soup.b)

# the .find function also does the same.
# print(soup.find('b'))

# if i want all the elements on the page with the 'b' tag-
# i can use the .find_all function
# print(soup.find_all('b'))

# i can also get the name of the tags by using .name
# print(soup.b.name)

# i can alter the name and have it change in the source.
# i start by defining a variable and giving it the value of soup.b
tag = soup.b 
print(tag)
# now by using the .name i can set the new name 
tag.name = 'blockquote'
print(tag)