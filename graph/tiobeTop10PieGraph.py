# from cProfile import label
# from operator import index
# from turtle import color
import pandas as pd
import matplotlib
import matplotlib.font_manager
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

[f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]



# 유니코드 깨짐현상 해결
matplotlib.rcParams['axes.unicode_minus'] = False
# 나눔고딕 폰트 적용
plt.rcParams["font.family"] = 'NanumGothic'

# CSV 불러오기
csvFile = '/home/junyharang/pythonPJ/202161_tiobe_지수.csv'
thisFrame = pd.read_csv(csvFile, encoding='utf-8')

print(thisFrame.info())
print('-'*50)
print(thisFrame['언어 이름'].unique())

langname = thisFrame['언어 이름']
userate = thisFrame['이용률']

intuserate = []
for i in userate:
    intuserate.append(int(i))

print(langname)

print(userate)

thisColor = ['r', 'b', 'g', 'c', 'm', 'y', 'lime', 'turquoise', 'lightseagreen', 'darkblue', 'royalblue', 'blueviolet', 'darkorchid', 'violet', 'purple', 'tomato', 'brown', 
             'orange', 'greenyellow', 'aqua', 'slategrey']

ratio = [intuserate]

title = '2021 Language Use Ranking'

plt.figure(figsize=(15, 15))

plt.title(title)


# Pie 그래프
plt.pie(intuserate, shadow=True, startangle=90, autopct='%1.2f%%')
plt.legend(langname, loc='upper left', ncol=2, bbox_to_anchor=(1, 1))

fileName='pie_tiobe_rank.png'

plt.savefig(fileName, dpi=400, bbox_inches='tight')
plt.show()
print(fileName + ' 의 파일이 저장 되었습니다!')
