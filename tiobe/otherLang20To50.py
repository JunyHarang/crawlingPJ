import os
from datetime import datetime

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

response = urlopen('https://www.tiobe.com/tiobe-index/')
soup = BeautifulSoup(response, 'html.parser')
tiobeOtherTable = soup.find('table', attrs={'class':'table table-striped'})

print(type(tiobeOtherTable))
print(tiobeOtherTable)

projectFolder = '/home/junyharang/pythonPJ'

try :
    # project폴더가 없다면 폴더 생성
    if not os.path.exists(projectFolder):
        os.mkdir(projectFolder)

except FileExistsError as err:
    print(err) # 오류 내용 출력
    pass       # 오류를 무시하고, 넘어간다.

tiobeOtherTbody = tiobeOtherTable.find('tbody')
print('tiobeOtherTbody')
print(type(tiobeOtherTbody))
print('-'*50)
print(tiobeOtherTbody)
print('#'*50)

tiobeOtherTr = tiobeOtherTbody.findAll('tr')
print('tiobeOtherTr')
print('언어 개수 : %d' % (len(tiobeOtherTr)))
print('-'*50)
print(type(tiobeOtherTr))
print('-'*50)
print(tiobeOtherTr)
print('#'*50)

otherLangList = []

for tr in tiobeOtherTr:
    langName = tr.select_one('td:nth-of-type(2)').string

    rating = tr.select_one('td:nth-of-type(3)').string
    
    otherLangData = [langName, rating]

    otherLangList.append(otherLangData)

    myfram = DataFrame(otherLangList, columns = ['언어 이름', '이용률'])

print('otherLangList')
print(otherLangList)
print('#'*50)

timeList = []

myyear = datetime.today().year
mymonth = datetime.today().month
mydays = datetime.today().day

date = [myyear, mymonth, mydays]

timeList.append(date)

fileName = (str(timeList).replace(',','').replace(' ','').replace('[', '').replace(']', '') + '_tiobe_Other_Lang_순위.csv')

myfram.to_csv(fileName, encoding= 'utf-8', index=False)

print(fileName + '의 저장이 완료 되었습니다!')

print(fileName + '의 크롤링이 완료 되었습니다!')