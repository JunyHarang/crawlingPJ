import os
from datetime import datetime

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

response = urlopen('https://www.tiobe.com/tiobe-index/')
soup = BeautifulSoup(response, 'html.parser')
tiobeTable = soup.find('table', attrs={'class':'table table-striped table-top20'})

projectFolder = '/home/junyharang/pythonPJ'

try :
    # project폴더가 없다면 폴더 생성
    if not os.path.exists(projectFolder):
        os.mkdir(projectFolder)

except FileExistsError as err:
    print(err) # 오류 내용 출력
    pass       # 오류를 무시하고, 넘어간다.

projectTbody = tiobeTable.find('tbody')
# print(type(mythead))
# print('-'*50)
# print(mythead)
# print('#'*50)

projectTr = projectTbody.findAll('tr')
print('언어 개수 : %d' % (len(projectTr)))
print('-'*50)
print(type(projectTr))
print('-'*50)
print(projectTr)
print('#'*50)

langList = []

for td in projectTr:

    programningLanguage = td.select_one('td:nth-of-type(4)').string

    ratings = td.select_one('td:nth-of-type(5)').string

    langdata = [programningLanguage, ratings]
    langList.append(langdata)

    myfram = DataFrame(langList, columns = ['언어 이름', '이용률'])

print(langList)
print('#'*50)  

timeList = []

myyear = datetime.today().year
mymonth = datetime.today().month
mydays = datetime.today().day

date = [myyear, mymonth, mydays]

timeList.append(date)

# print (timeList)

fileName = (str(timeList).replace(',','').replace(' ','').replace('[', '').replace(']', '') + '_tiobe_지수.csv')

# print(fileName)

myfram.to_csv(fileName, encoding= 'utf-8', index=False)

print(fileName + '의 저장이 완료 되었습니다!')

print(fileName + '의 크롤링이 완료 되었습니다!')




