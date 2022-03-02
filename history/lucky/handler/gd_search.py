import json
import requests
import simplekml
from simplekml import Kml, Types, Snippet, Color

from config.setting import (
    key,
    gd_district_url,
    gd_newroute_url,
    gd_search_address_url
)


def search_address(address):
    '''
    查询某个区域的坐标
    '''
    parameters = {"key": key, "address": address}
    res = requests.get(gd_search_address_url, params=parameters).json()

    addr = res.get("geocodes")[0]['formatted_address']
    location = res.get("geocodes")[0]['location']
    print(addr, location)
    return {"name": address, "point": location}



def search_newroute(start_addr, end_addr):

    start_point = search_address(start_addr)["point"]
    end_point = search_address(end_addr)["point"]

    parameters = {
        "key": key, "origin": start_point, "destination": end_point,
        "origin_type": 1, "strategy": 38,
        "cartype":0,
        "waypoints": 16,
        "show_fields": "polyline"
    }
    res = requests.post(gd_newroute_url, data=parameters).json()
    print(res)
    steps = res.get("route")["paths"][0]['steps']

    newroute = []
    for step in steps:
        polyline = [each.split(",") for each in step['polyline'].split(";")]
        newroute.extend(polyline)
    return {"start_addr": start_addr, "end_addr": end_addr, "newroute": newroute}



if __name__ == '__main__':
    address = "周口市淮阳县"
    # search_address(address)
    start = "北京"
    end = "淮阳县冯塘乡张庄"
    search_newroute(start, end)