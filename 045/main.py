import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

#main()
response = requests.get(url=URL)

soup = BeautifulSoup(response.text, 'html.parser')

titles_tag = soup.find_all(name="h3", class_="title")
# titles = []
# for tag in titles_tag:
#     titles.append(tag.text)
titles = [tag.text for tag in titles_tag]
print(titles[::-1])

#Saving to a file
with open("movies.txt", "w") as fp:
    fp.write("\n".join(titles[::-1]))
    # for title in titles:
    #     file.write(f"{title}\n")




