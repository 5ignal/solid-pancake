# solid-pancake

이 봇은 제가 재학 중인 학교의 학식 식단을 텔레그램으로 알려주는 기능을 제공합니다.

<hr/>

### 사용 방법

app_sample.py
```py
# 7 ~ 12
# 식단 주소
lunch_menu_url = ""
# 텔레그램 봇 토큰
bot_token = ""
# 텔레그램 챗 아이디
chat_id = ""

# 33 ~ 34
lunch_menu_1 = lunch_menu(f"{lunch_menu_url}(식단번호)")
lunch_menu_2 = lunch_menu(f"{lunch_menu_url}(식단번호)")
```
해당 줄 내용을 수정하시면 됩니다.

<hr/>

### AWS

Lambda + CloudWatch로 매일 특정 시간에 알림을 보내도록 할 수 있습니다. 

- bs4.zip을 계층에 업로드 후 함수에서 계층을 추가해야 사용할 수 있습니다.

<hr/>

### 참고 사항

- 현재는 재학 중인 학교를 기준으로 작성되었습니다. 다른 학교의 식단 URL에서는 이용이 불가능할 수 있습니다.