# from cProfile import label
# from operator import index
# from turtle import color
import pandas as pd
import matplotlib
from matplotlib import ticker as mtick, use
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
csvFile = '/home/junyharang/pythonPJ/tiobe/202161_tiobe_Total.csv'
thisFrame = pd.read_csv(csvFile, encoding='utf-8')

print(thisFrame.info())
print('-'*50)
print(thisFrame['언어 이름'].unique())

# y = np.arange(20)
langName = thisFrame.sort_values(by='이용률', axis=0, ascending=True)['언어 이름']
userate = thisFrame.sort_values(by='이용률', axis=0, ascending=True)['이용률']


thisColor = ['r', 'b', 'g', 'c', 'm', 'y', 'lime', 'turquoise', 'lightseagreen', 'darkblue', 'royalblue', 'blueviolet', 'darkorchid', 'violet', 'purple', 'tomato', 'brown', 'orange', 'greenyellow', 'aqua', 'slategrey']


        

# barh 그래프
plt.figure(figsize=(15,15))
plt.title('2021 Language Ranking')



ax = plt.barh(langName, height= -0.5, align='edge', color=thisColor, edgecolor="gray", linewidth=1, tick_label=langName, log=False)

for p in ax.patches:
    x, y, width, height = p.get_bbox().bounds
    ax.text(width*1.01, y+height/2, "%.1f %%"%(width), va='center')

plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
plt.xlim(0, 13.5)
plt.gca().xaxis.set_major_locator(mtick.MultipleLocator(0.5))


fileName='tiobe_주요_언어_순위.png'

# bbox_inches='tight'는 캔버스에 표를 맞추어준다.
plt.savefig(fileName, dpi=400, bbox_inches='tight')

plt.show()

print(fileName + ' 의 파일이 저장 되었습니다!')

print('tiobebarhGraph.py를 종료 합니다!')