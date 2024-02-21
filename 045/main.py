from bs4 import BeautifulSoup


#main()
with open("website.html", "r", encoding='utf-8') as fp:
    contents = fp.read()
    
soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))
    
heading = soup.find(name="h1", id="name")
print(heading.text)

company_url = soup.select_one("p a")
print(company_url)
    