from bs4 import BeautifulSoup
with open('test.html','r') as file:
    html = file.read()
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
#print(soup.title.string)
#print(soup.)
# print(soup.p['name'])
# print(soup.p['class'])
for td in soup.find_all(name='td'):
    print(td.string)