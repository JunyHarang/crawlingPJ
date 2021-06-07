# Copyright 2021. (주니하랑) all rights reserved.

import folium, requests
import pandas as pd

urlHeader = 'https://dapi.kakao.com/v2/local/search/address.json?query='
apiKey = '[카카오 개발자 API]'
header = {'Authorization' : 'KakaoAK ' + apiKey}

csvFile = '/home/junyharang/pythonPJ/IT_Company_List/IT_Company_info.csv'
itFrame = pd.read_csv(csvFile, index_col=0, encoding='utf-8')

copyright = 'Copyright 2021. (주니하랑) all rights reserved.'
junyHarangMail = 'junyharang8592@gmail.com'
junyHarangGitHub = 'https://github.com/JunyHarang'
junyHarangBlog = 'https://junyharang.tistory.com/'


address = itFrame['본사 위치']

address = address[2]

url =  urlHeader + address

def getGeoCoder(companyAddress):
    result = ""
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        
        try:
            resultAddress = r.json()["documents"][0]["address"]
            result = resultAddress["y"], resultAddress["x"]

        except Exception as err:
            return None

    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

addressLating = getGeoCoder(address)
latitude = addressLating[0]
longitude = addressLating[1]

print("주소지 : ", address)
print("위도 : ", latitude)
print("경도 : ", longitude)

companyInfo = '배달의 민족', str(address)
foliMap = folium.Map(location=[latitude, longitude], zoom_start=17)
naverIcon = folium.Icon(color='green', icon='info-sign')
naveriframe = folium.IFrame(width=300, height=300)
naverpopup = folium.Popup(naveriframe, max_width=650)
folium.Marker([latitude, longitude], popup=naverpopup, tooltip=companyInfo, icon=naverIcon).add_to(foliMap)

# CircleMarker를 통해 지도 상에 기준점 반경을 나타낸다.
folium.CircleMarker([latitude, longitude], radius=300, color='green', fill_color='yellow', fill=False, popup=companyInfo).add_to(foliMap)

foliMap.save('BaeminMapGraph.html')

print(copyright + '\n 상업용으로 본 프로그램을 사용 및 무단 복제, 배포를 금지합니다.')
print('프로그램 관련 문의는 아래 메일로 보내주시거나, GitHub, Blog 등을 활용 해 주시기 바랍니다! \n' + 'Mail : ' + junyHarangMail + ', Github : ' + junyHarangGitHub + ', Blog : ' + junyHarangBlog)

companyName = '배달의민족'

print(str(companyName) + '의 지도가 저장 되었습니다. \n 프로그램을 종료 합니다!')
