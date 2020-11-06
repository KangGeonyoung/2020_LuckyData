import requests as req, json
import xmltodict
from pprint import pprint
from urllib import parse

#json_openAPI_Get방식 - 미세먼지 경보 서비스
Dust_URL = "http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo"
API_Key = "UaUm57/q/4gzzTYthuvfXVxw2E6bM9GomUTgr18IjHMPJcH0LDP3OZrB0+A2ZW80KGIko+Zo9jhrcNiet7Jbsw=="

Dust_Params = {'ServiceKey' : API_Key, 'numOfRows' : '10', 'pageNo' : '1',  'year' : '2019', 'itemCode' : "PM10", '_returnType' : json}

Dust_Get = req.get(Dust_URL, params = Dust_Params)
Dust = json.loads(Dust_Get.text)['list']

for i in range(len(Dust)):
    print("발령 날짜 : " + Dust[i]['issueDate'])
    print("해제 날짜 : " + Dust[i]['clearDate'])
    print("지역 : " + Dust[i]['districtName'])
    print("권역 : " + Dust[i]['moveName'])
    print("농도 : " + Dust[i]['issueVal'])
    print("경보 단계 : " + Dust[i]['issueGbn'])
    print()



#xml_openAPI_Get방식 - 지진 옥외 대피장소 서비스
Earthquake_URL = "http://apis.data.go.kr/1741000/EmergencyAssemblyArea_Earthquake/getAreaList"
E_API_Key = "UaUm57/q/4gzzTYthuvfXVxw2E6bM9GomUTgr18IjHMPJcH0LDP3OZrB0+A2ZW80KGIko+Zo9jhrcNiet7Jbsw=="

Earthquake_Params = {'ServiceKey' : E_API_Key, 'pageNo' : '5', 'numOfRows' : '10', 'type' : 'xml',   'flag' : 'Y'}

Earthquake_Get = req.get(Earthquake_URL, params = Earthquake_Params)
Earthquake_Parse = xmltodict.parse(Earthquake_Get.text)

Earthquake = Earthquake_Parse['EarthquakeOutdoorsShelter']['row']

for i in range(5):
    print("시도명 : " + Earthquake[i]['ctprvn_nm'])
    print("시군구명 : " + Earthquake[i]['sgg_nm'])
    print("대피 시설명 : " + Earthquake[i]['vt_acmdfclty_nm'])
    print("상세 주소 : " + Earthquake[i]['dtl_adres'])
    print()


















