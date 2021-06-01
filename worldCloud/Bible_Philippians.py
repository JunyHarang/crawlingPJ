from configparser import Interpolation
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import STOPWORDS
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
# import matplotlib.font_manager as fm
# import matplotlib as mpl

# fontList = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# print(fontList[:100])

# [f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

# path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

# mpl.rcParams['axes.unicode_minus'] = False

# plt.rcParams['font.family'] = 'NanumGothic'

# plt.rc('font', family='NanumGothic') 

imageFile = 'Jesus.png'

imgFile = Image.open(imageFile)

idx = 0

print(str(idx) + '번 예수님 그림 파일 내용')
print('*'*100)
print(type(imgFile))
print('-'*100)
print(imgFile)
print('='*100)
print('\n')

idx += 1


loveJESUS = np.array(imgFile)

print(str(idx) + '번 예수님 그림 파일 색깔 배열 상세')
print('*'*100)
print(type(loveJESUS ))
print('-'*100)
print(loveJESUS )
print('='*100)
print('\n')

idx += 1

# 그림 영역(캔버스) 설정
plt.figure(figsize=(16, 16))

plt.imshow(loveJESUS, interpolation='bilinear')

# 축 선과 라벨 없애기
plt.axis('off')

fileName = 'IloveJESUS.png'
plt.savefig(fileName, dpi=400, bbox_inches='tight')
print(fileName + ' 의 파일이 저장 완료 되었습니다!')

######################################################################################################

# 불용어 제거 (필요 없는 말들 지우기)
thisStopWords = set(STOPWORDS)
thisStopWords.add('will') # 기본 불용어에 만들기

thisStopWords.update(['know', 'whatever', 'everything', 'take', 'need', 'put', 'one', 'joy']) # 기본 불용어에 추가하기
# print(len(thisStopWords))
# print(thisStopWords)

######################################################################################################

wc = WordCloud(background_color='white', max_words=1000, mask=loveJESUS, stopwords=thisStopWords)

greatFile = 'Bible_Philippians.txt'
text = open(greatFile, 'rt', encoding='utf-8')
text = text.read()

wc = wc.generate(text)

print(str(idx) + '번 빌립보서 1~4장 내용 가져오기')
print('*'*100)
print(wc.words_)
print('='*100)
print('\n')

plt.figure(figsize=(15, 15))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

fileName = 'Philippians.png'
plt.savefig(fileName, dpi=400, bbox_inches='tight')
print(fileName + '의 저장이 완료 되었습니다!')

######################################################################################################

# plt.show()

print('Bible_Philippians의 작업이 완료 되었습니다!')