from bs4 import BeautifulSoup
import requests


#main()
yc_response = requests.get(url="https://news.ycombinator.com/")

soup = BeautifulSoup(yc_response.text, 'html.parser')

print(soup.title.text)
articles = soup.find_all(name="span", class_="titleline")
article_names = []
article_hrefs = []
for article in articles:
    article_names.append(article.get_text())
    article_hrefs.append(article.find(name="a").get("href"))
    
# article_text = article_tag.get_text()
# article_link = article_tag.find_all(name="a").get("href")
article_scores =[]


scores = soup.find_all(name="span", class_="score")
for score in scores:
    point = int(score.text.split()[0])
    article_scores.append(point)

# print(article_names)
# print(article_hrefs)
print(article_scores)

position = article_scores.index(max(article_scores))
print(position)
print(article_names[position])
print(article_scores[position])
