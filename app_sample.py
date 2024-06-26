import datetime
import requests
from bs4 import BeautifulSoup


# 메뉴 크롤링
def crawling(url, num):
    response = requests.get(f'{url}{num}')
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    today = datetime.today().weekday()

    food_lists = soup.find_all('ul', class_='foodList')

    menu_text = food_lists[today].text.replace('\n', '')
    menu_text = menu_text.replace('\r', '\n')

    return menu_text


# 디스코드 웹훅
def webhook(webhook_url, name, menu):
    payload = {
        "embeds": [
            {
                "title": name,
                "description": menu
            }
        ]  
    }
    requests.post(webhook_url, json=payload)


# AWS Lambda Handler
def lambda_handler(event, context):
    menu_url = "학식 URL"
    discord_webhook_url = "Webhook URL"
    webhook(discord_webhook_url, "메뉴 1", crawling(menu_url, "메뉴번호"))
    webhook(discord_webhook_url, "메뉴 2", crawling(menu_url, "메뉴번호"))


# 메인 함수
if __name__ == "__main__":
    lambda_handler(None, None)
