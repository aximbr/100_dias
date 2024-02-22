#Time Machine Project
from bs4 import BeautifulSoup
import requests

# date = input("Which year do you want to travel to? Type the date in this format (YYYY-MM-DD): ")
date = "1964-08-02"
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, 'html.parser')

songs_tag = soup.select("li ul li h3")
# titles = []
# for tag in titles_tag:
#     titles.append(tag.text)
songs = [tag.get_text().strip() for tag in songs_tag]
print(songs)

#Saving to a file
# with open("movies.txt", "w") as fp:
#     fp.write("\n".join(titles[::-1]))
    # for title in titles:
    #     file.write(f"{title}\n")