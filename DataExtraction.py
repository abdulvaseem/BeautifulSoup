"""K ABDUL VASEEM AKRAM """

"""command-pip install BeautifulSoup4"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
#all below are the commands to run in console window of python
soup.title # returns title
soup.title.name # returns title name
soup.title.string
soup.title.parent.name
soup.p
soup.p['class']
soup.a
soup.find_all('a') # returns all the hyperlinks present in the webpage used to make PAGERANK ALGORITHM 

soup.find(id="link3") 
for link in soup.find_all('a'):
    print(link.get('href'))
    
print(soup.get_text())
