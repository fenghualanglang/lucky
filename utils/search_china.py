import json
import requests
import simplekml
from simplekml import Kml, Types, Snippet, Color

from settingConf.constants import (
    key,
    gd_district_url,
    gd_newroute_url,
    gd_china_point_url,
    ali_district_url,
    ali_district_full_url,
)


def china_location_address(address):
    '''
    # 给一个地点, 查询属于区域坐标
    '''
    parameters = {"key": key, "address": address}
    res = requests.get(gd_china_point_url, params=parameters).json()

    if res.get("infocode") != "10000":
        return {"name": address, "point": '', "location": '查无此处'}
        # return {'name': address, 'point': '请联系管理员', 'location': '请联系管理员'}

    addr = res.get("geocodes")[0]
    location = res.get("geocodes")[0]['location']

    if addr.get('district'):
        address = addr.get('district')
    elif addr.get('city'):
        address = addr.get('city')
    elif addr.get('province'):
        address = addr.get('province')
    elif addr.get('country'):
        address = addr.get('country')
    else:
        address = addr.get('')
    return {"name": address, "point": location, "location": addr.get('formatted_address')}


def china_location_point(point):
    # 给一个坐标, 查询属于那个区域
    url = f"https://restapi.amap.com/v3/geocode/regeo?key={key}&location={point}&poitype=&radius=1000&extensions=base&batch=false&roadlevel=1"
    res = requests.get(url).json()

    if res.get("infocode") != "10000":
        return {'point': point, 'province': '请联系管理员', 'district': '请联系管理员', 'country': '请联系管理员'}

    addr = res.get("regeocode")["addressComponent"]
    dic = {"point": point}

    city = addr.get('city')
    province = addr.get('province')
    district = addr.get('district')
    country = addr.get('country')

    if country:
        dic.update({"country": country})
    if province:
        dic.update({"province": province})
    if city:
        dic.update({"city": city})
    if district:
        dic.update({"district": district})
    if not country and not province and not city and not district:
        return {'point': point, 'province': '仅支持中国', 'district': '仅支持中国', 'country': '仅支持中国'}
    return dic


def ali_china_district():
    url = ali_district_url.format("410000")
    res = requests.get(url)
    return res.json()


def ali_china_district_full():
    url = ali_district_full_url.format("100000")
    res = requests.get(url)
    return res.json()






def search_newroute(start_addr, end_addr):

    start_point = search_china_point(start_addr)["point"]
    end_point = search_china_point(end_addr)["point"]

    parameters = {
        "key": key, "origin": start_point, "destination": end_point,
        "origin_type": 1, "strategy": 38, "cartype":0,
        "waypoints": 16, "show_fields": "polyline"
    }
    res = requests.post(gd_newroute_url, data=parameters).json()
    steps = res.get("route")["paths"][0]['steps']

    newroute = []
    for step in steps:
        polyline = [each.split(",") for each in step['polyline'].split(";")]
        newroute.extend(polyline)
    return {"start_addr": start_addr, "end_addr": end_addr, "newroute": newroute}



def search_district(keywords, subdistrict=1, extensions="all"):
    """
    1. 仅仅要大外框
    2. 仅仅要子节点
    3. 要自己点与大外框
    """
    parameters={"keywords": keywords, "subdistrict": subdistrict, "extensions": extensions, "key": key}
    res = requests.get(url=gd_district_url, params=parameters).json()
    print(res)
    res = res['districts'][0]

    name = res.get("name")
    polyline = res.get("polyline")
    center = res.get("center").split(",")
    polyline = [each.split(",") for each in polyline.split(";")]
    return {"name": name, "center": center, "polyline": polyline}



if __name__ == '__main__':

    address = "美国"
    # res = search_china_point(address)
    # res = china_location("116.481488,39.990464")
    # start = "北京"
    # end = "淮阳县冯塘乡张庄"
    # res = search_newroute(start, end)
    # res = ali_china_district()
    print(res)







