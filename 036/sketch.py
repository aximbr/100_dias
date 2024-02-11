# lista_cheia = [1, 2, 3, 4, 5, 6, 7]

# parcial = lista_cheia[0:10]

# print(parcial)
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


MY_NEWS_KEY = "d5dd011b95db4254bf82c7083d155fcf"
URL_NEWS = "https://newsapi.org/v2/everything"    
parameters = {
        "q" : COMPANY_NAME,
        "searchIn" : "description",
        "apikey" : MY_NEWS_KEY,
        "from" : '2024-02-09',
        "language" : "en"
        }

response = requests.get(URL_NEWS, params=parameters)
data_news = response.json()

#nr_articles = data_news["totalResults"]

three_articles_list = data_news["articles"][0:3]

up_down = "🔺"
diff_percent = 1

formated_articles_list = [[f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles_list]]


print(formated_articles_list)
