import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_ALPHA_KEY = "6QIV29HYITYJNB9J"
MY_NEWS_KEY = "d5dd011b95db4254bf82c7083d155fcf"

URL_STOCK =  "https://www.alphavantage.co/query"
URL_NEWS = "https://newsapi.org/v2/everything"

#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
#The free account limits to 25 calls a day



parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : MY_ALPHA_KEY
        }

response = requests.get(URL_STOCK, params=parameters)
response.raise_for_status()
if response.status_code == 200:
    if len(response.json()) < 2:
        print("Ops, reached the limit for free stuff!")
    else:
        data = response.json()


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#print(data)

# close_price = []

list_of_days = list(data["Time Series (Daily)"].keys())

# for day in list_of_days:
#     close_price.append(float((data["Time Series (Daily)"][day]["4. close"])))
close_price = [float((data["Time Series (Daily)"][day]["4. close"])) for day in list_of_days]
    
yesterday_price = close_price[0]
day_before_price = close_price[1]
yesterday = list_of_days[0]

delta =  round(((yesterday_price - day_before_price)/yesterday_price)*100)

up_down = None
if delta > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
    
# print(delta)
# print(day_before_price)
# print(yesterday_price)

if abs(delta) > 1:
    print(f"The variantion in 2 days was {delta}%")
    print(f"Let's check the News for {yesterday}")
#   print("Get news")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#https://newsapi.org/v2/everything?q=keyword&apiKey=d5dd011b95db4254bf82c7083d155fcf
    
    parameters = {
        "q" : COMPANY_NAME,
        "searchIn" : "description",
        "apikey" : MY_NEWS_KEY,
        "from" : yesterday,
        "language" : "en"
        }

    response = requests.get(URL_NEWS, params=parameters)
    data_news = response.json()

    #nr_articles = data_news["totalResults"]

    three_articles_list = data_news["articles"][0:3]
#   print(three_articles_list)
    formated_articles_list = [[f"{STOCK}: {up_down}{delta}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles_list]]

    print(formated_articles_list)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

    