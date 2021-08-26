from asyncio import sleep
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time


fileName = '/home/junyharang/다운로드/chromedriver'
driver = webdriver.Chrome(fileName)
driver.get("https://www.google.com/maps")

################### 내용 찾기 ################

# 다음 검색창 찾기
daumSearch = driver.find_element_by_name("q")
# 검색창에 검색어 입력
daumSearch.send_keys("네이버 본사")
# 엔터키 입력
daumSearch.send_keys(Keys.RETURN)
# 화면 스크롤 내리기
# naverBody = driver.find_element_by_css_selector('body') # body Tag 선택

# 총 2번의 스크롤 Down
# for scroll in range(2):
#     googleSearch.send_keys(Keys.PAGE_DOWN) # Page Down
#     time.sleep(0.5)



# 검색 결과 상에 xpath 값을 이용하여 해당 주소 링크 클릭

#####################################################

################### 회사 내용 가져오기 ################
idx = 0

time.sleep(5)

# *************** 네이버 정보 가져오기 ***************

# 회사 이름 크롤링
naverName = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
naverCompanyName = naverName.text


# 회사 주소 크롤링
naverAddress = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
navercompanyAddress = naverAddress.text



print(str(idx) + ' 번의 크롤링 한 ' + naverCompanyName + ' 의 정보를 출력 합니다.')

# print(companyInfoList)
# print(type(companyInfoList))
print('-'*100)



driver.quit()
# *****************************************************

driver = webdriver.Chrome(fileName)
driver.get("https://www.google.com/maps")

################### 내용 찾기 ################

# 다음 검색창 찾기
daumSearch = driver.find_element_by_name("q")
# 검색창에 검색어 입력
daumSearch.send_keys("카카오본사 제주")
# 엔터키 입력
daumSearch.send_keys(Keys.RETURN)
# 화면 스크롤 내리기
# naverBody = driver.find_element_by_css_selector('body') # body Tag 선택

# 총 2번의 스크롤 Down
# for scroll in range(2):
#     googleSearch.send_keys(Keys.PAGE_DOWN) # Page Down
#     time.sleep(0.5)



# 검색 결과 상에 xpath 값을 이용하여 해당 주소 링크 클릭

#####################################################

################### 회사 내용 가져오기 ################

idx += 1


time.sleep(5)

# *************** 카카오 정보 가져오기 ***************

# 회사 이름 크롤링
kakaoName = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
kakaocompanyName = kakaoName.text


# 회사 주소 크롤링
kakaoAddress = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
kakaoCompanyAddress = kakaoAddress.text



print(str(idx) + ' 번의 크롤링 한 ' + kakaocompanyName + ' 의 정보를 출력 합니다.')

# print(companyInfoList)
# print(type(companyInfoList))
print('-'*100)

idx += 1

driver.quit()

# *****************************************************

driver = webdriver.Chrome(fileName)
driver.get("https://www.google.com/maps")

################### 내용 찾기 ################

# 다음 검색창 찾기
daumSearch = driver.find_element_by_name("q")
# 검색창에 검색어 입력
daumSearch.send_keys("우아한 형제들")
# 엔터키 입력
daumSearch.send_keys(Keys.RETURN)
# 화면 스크롤 내리기
# naverBody = driver.find_element_by_css_selector('body') # body Tag 선택

# 총 2번의 스크롤 Down
# for scroll in range(2):
#     googleSearch.send_keys(Keys.PAGE_DOWN) # Page Down
#     time.sleep(0.5)



# 검색 결과 상에 xpath 값을 이용하여 해당 주소 링크 클릭

#####################################################

################### 회사 내용 가져오기 ################

companyInfoList = []

companyInfoList.append(idx)

time.sleep(5)

# *************** 우아한 형제들 정보 가져오기 ***************

# 회사 이름 크롤링
baeminName = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
baemincompanyName = baeminName.text


# 회사 주소 크롤링
baeminAddress = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
baeminCompanyAddress = baeminAddress.text



print(str(idx) + ' 번의 크롤링 한 ' + baemincompanyName + ' 의 정보를 출력 합니다.')

# print(companyInfoList)
# print(type(companyInfoList))
print('-'*100)

idx += 1

driver.quit()

# *****************************************************

driver = webdriver.Chrome(fileName)
driver.get("https://www.google.com/maps")

################### 내용 찾기 ################

# 다음 검색창 찾기
daumSearch = driver.find_element_by_name("q")
# 검색창에 검색어 입력
daumSearch.send_keys("당근마켓 본사")
# 엔터키 입력
daumSearch.send_keys(Keys.RETURN)
# 화면 스크롤 내리기
# naverBody = driver.find_element_by_css_selector('body') # body Tag 선택

# 총 2번의 스크롤 Down
# for scroll in range(2):
#     googleSearch.send_keys(Keys.PAGE_DOWN) # Page Down
#     time.sleep(0.5)



# 검색 결과 상에 xpath 값을 이용하여 해당 주소 링크 클릭

#####################################################

################### 회사 내용 가져오기 ################



companyInfoList.append(idx)

time.sleep(5)

# *************** 당근마켓 정보 가져오기 ***************

# 회사 이름 크롤링
danggunName = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
dangguncompanyName = danggunName.text


# 회사 주소 크롤링
danggunAddress = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
danggunCompanyAddress = danggunAddress.text



print(str(idx) + ' 번의 크롤링 한 ' + dangguncompanyName + ' 의 정보를 출력 합니다.')

# print(companyInfoList)
# print(type(companyInfoList))
print('-'*100)

idx += 1

driver.quit()

# *****************************************************

driver = webdriver.Chrome(fileName)
driver.get("https://www.google.com/maps")

################### 내용 찾기 ################

# 다음 검색창 찾기
daumSearch = driver.find_element_by_name("q")
# 검색창에 검색어 입력
daumSearch.send_keys("Toss")
# 엔터키 입력
daumSearch.send_keys(Keys.RETURN)
# 화면 스크롤 내리기
# naverBody = driver.find_element_by_css_selector('body') # body Tag 선택

# 총 2번의 스크롤 Down
# for scroll in range(2):
#     googleSearch.send_keys(Keys.PAGE_DOWN) # Page Down
#     time.sleep(0.5)



# 검색 결과 상에 xpath 값을 이용하여 해당 주소 링크 클릭

#####################################################

################### 회사 내용 가져오기 ################


time.sleep(5)

# *************** 토스 정보 가져오기 ***************

# 회사 이름 크롤링
tossName = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
tosscompanyName = tossName.text


# 회사 주소 크롤링
tossAddress = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
tossCompanyAddress = tossAddress.text



print(str(idx) + ' 번의 크롤링 한 ' + tosscompanyName + ' 의 정보를 출력 합니다.')

# print(companyInfoList)
# print(type(companyInfoList))
# print('-'*100)

idx += 1

driver.quit()

# *****************************************************
companyInfo_dict_List = [ 
    {'번호' : 1, '회사명': naverCompanyName, '본사 위치' : navercompanyAddress},
    {'번호' : 2, '회사명': kakaocompanyName, '본사 위치' : kakaoCompanyAddress},
    {'번호' : 3, '회사명': baemincompanyName, '본사 위치' : baeminCompanyAddress},
    {'번호' : 4, '회사명': dangguncompanyName, '본사 위치' : danggunCompanyAddress},
    {'번호' : 5, '회사명': tosscompanyName, '본사 위치' : tossCompanyAddress},
]

print(companyInfo_dict_List)

companyFram = DataFrame(companyInfo_dict_List, columns=['번호', '회사명', '본사 위치'])

print(companyFram)
print('=' * 100)

fileName = 'IT_Company_info.csv'

companyFram.to_csv(fileName, encoding='utf-8', index=True)



