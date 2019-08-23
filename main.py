# -*- coding: utf-8 -*-
from selenium import webdriver

web = webdriver.Chrome("D://Dev/ChromeWebDriver/chromedriver.exe")

# 인터파크 접속
web.get("http://ticket.interpark.co.kr/")

# 로그인
loginBtn = web.find_element_by_id("imgLogin").click()

# 로그인 iframe으로 변경
loginIFrame = web.find_element_by_css_selector("div.leftLoginBox > iframe")
web.switch_to.frame(loginIFrame)

# iframe내부 Form 요소 (로그인 수행)
idInput = web.find_element_by_id("userId")
myId = input("아이디를 입력하세요 >>> ")
idInput.send_keys(myId)
pwInput = web.find_element_by_id("userPwd")
myPwd = input("비밀번호를 입력하세요 >>> ")
pwInput.send_keys(myPwd)
loginSubmitBtn = web.find_element_by_id("btn_login").click()

# iframe 탈출
web.switch_to.default_content()

# 해당 티켓팅 URL로 이동
goodsCode = input("예매상품 GoodsCode를 입력하세요 >>> ")
defaultTicketUrl = "http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode="
web.get(defaultTicketUrl + goodsCode)

# 예매하기 버튼 클릭
revBtn = web.find_element_by_css_selector("div.tk_dt_btn_TArea > a").click()

# 팝업창 전환
web.switch_to.window(web.window_handles[1])