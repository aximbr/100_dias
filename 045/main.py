from bs4 import BeautifulSoup


#main()
with open("website.html", "r", encoding='utf-8') as fp:
    contents = fp.read()
    
soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)
  