import urllib3
import datetime
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

# 식단 주소
lunch_menu_url = ""
# 텔레그램 봇 토큰
bot_token = ""
# 텔레그램 챗 아이디
chat_id = ""


# 식단 크롤링
def lunch_menu(menu_url):
    response = http.request('GET', menu_url)
    today = datetime.datetime.today().weekday() + 2
    soup = BeautifulSoup(response.data, "html.parser")

    if today >= 5:
        exit()
    elif today == 0:
        ul = soup.select_one("ul.foodList")
    else:
        ul = soup.select_one(f"tr:nth-child(1) td:nth-child({today}) ul")

    return "\n".join([li.text.strip() for li in ul.select("li")])


# 텔레그램 메세지 전송
def telegram():
    lunch_menu_1 = lunch_menu(f"{lunch_menu_url}(식단번호)")
    lunch_menu_2 = lunch_menu(f"{lunch_menu_url}(식단번호)")
    date = f"{datetime.datetime.now():%Y-%m-%d}\n\n"
    result = f"{date}식단1\n{'-'*20}\n{lunch_menu_1}\n{'-'*20}\n\n식단2\n{'-'*20}\n{lunch_menu_2}\n{'-'*20}\n"
    url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id={chat_id}&text={result}"
    http.request('GET', url)

telegram()
