import csv
import glob
import os
from datetime import datetime

# CSV 파일 존재 경로
path = '/home/junyharang/pythonPJ/'

timeList = []

myyear = datetime.today().year
mymonth = datetime.today().month
mydays = datetime.today().day

date = [myyear, mymonth, mydays]

timeList.append(date)

fileName = (str(timeList).replace(',','').replace(' ','').replace('[', '').replace(']', '') + '_tiobe_Total.csv')

merge_path = '/home/junyharang/pythonPJ/' + fileName

# print(merge_path)

# 01. merge 대상 파일 확인 (해당 경로에 있는 모든 파일을 읽어온다.)
fileList = glob.glob(os.path.join(path, '*.csv'))
print(fileList)

# 02. merge할 파일 open
with open(merge_path, 'w') as fileWrite:
    for file in fileList:
        with open(file, 'r') as fileRead:
            while True:
                # 02-1. merge 대상 파일의 row 한 줄을 읽어온다.
                line = fileRead.readline()

                # row가 없으면 해당 csv 파일을 종료한다.
                if not line: 
                    break
                
                # 03. 읽은 row 한 줄을 merge할 파일에 쓴다.
                fileWrite.write(line)

        fileName = file.split('\\')[-1]

print('mergeCsv가 정상적으로 완료 되었습니다!')