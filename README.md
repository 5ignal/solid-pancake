# solid-pancake

이 봇은 제가 재학 중인 학교에서 제공하는 학식 메뉴를 텔레그램으로 전달해주는 기능을 제공합니다.

<hr/>

### 사용 방법

app_sample.py
```py
# 39 ~ 42
menu_url = "학식 URL"
discord_webhook_url = "Webhook URL"
webhook(discord_webhook_url, "메뉴 1", crawling(menu_url, "메뉴번호"))
webhook(discord_webhook_url, "메뉴 2", crawling(menu_url, "메뉴번호"))
```
해당 줄 내용을 수정하시면 됩니다.

<hr/>

### AWS

Lambda + CloudWatch를 사용하면 특정 시간에 알림을 보내도록 할 수 있습니다. 

- bs4.zip을 계층에 업로드 후 함수에서 계층을 추가해야 사용할 수 있습니다.

<hr/>

### 참고 사항

- 제가 재학 중인 학교를 기준으로 작성되었습니다. 다른 학교에서는 이용이 불가능할 수 있습니다.