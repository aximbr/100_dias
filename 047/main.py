import requests
from bs4 import BeautifulSoup
import re

url = "https://www.amazon.com/Homall-Computer-Executive-Ergonomic-Adjustable/dp/B01MRZ02TL/ref=sr_1_2_sspa?crid"
"=292R36Z22OH8R&keywords=gaming%2Bchair&qid=1697382874&sprefix=gaming%2Bchair%2Caps%2C114&sr=8-2-spons&ufe"
"=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1 "

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/117.0.0.0 Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9,es-US;q=0.8,es;q=0.7,fr-FR;q=0.6,fr;q=0.5"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price_whole = soup.select_one("span.a-price-whole")
price_fraction = soup.select_one("span.a-price-fraction")

if price_whole and price_fraction:
    current_price = float(f"{price_whole.text}{price_fraction.text}")
else:
    current_price = None

previous_price_element = soup.select_one("span.a-text-price")
if previous_price_element:
    previous_price_text = previous_price_element.get_text(strip=True)
    previous_price = re.search(r'$([\d,.]+)', previous_price_text)
    if previous_price:
        previous_price = float(previous_price.group(1).replace(",", ""))
    else:
        previous_price = None
else:
    previous_price = None
    
if current_price is not None:
    if previous_price is not None:
        price_difference = previous_price - current_price
        price_difference_str = f"${abs(price_difference):.2f}"
        
        if price_difference > 0:
            message = f"This item is currently listed for ${current_price:.2f}. That's {price_difference_str} less than its original price."
        elif price_difference < 0:
            message = f"This item is currently listed for ${current_price:.2f}. That's {price_difference_str} more than its original price."
        else:
            message = f"This item is currently listed for ${current_price:.2f}, which is the same as its original price."
    else:
        message = f"This item is currently listed for ${current_price:.2f}, but the original price is not available."
else:
    message = "Price not found"

print(message)
