
import json
import requests
import simplekml
from simplekml import Kml, Types, Snippet, Color

from config.setting import (
    key,
    gd_district_url
)


def map_border(name, polyline, center):
    '''
    线条颜色
    线条宽度

    框里透明度
    框里颜色
    '''

    kml = Kml(name=name, open=1)
    pol = kml.newpolygon(name=name)
    pol.outerboundaryis = polyline
    # 线段框的颜色，粗细
    pol.style.linestyle.color = simplekml.Color.green
    # pol.style.linestyle.color = None
    pol.style.linestyle.width = 4
    # 框里的透明度，与颜色  透明与越小越，越清晰
    pol.style.polystyle.color = simplekml.Color.changealphaint(150, simplekml.Color.green)

    pnt =kml.newpoint(name=name, coords=[center])  # lon, lat, optional height
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

    # pol.altitudemode = simplekml.AltitudeMode.relativetoground
    # pol.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
    pol.camera.longitude = 112.157   #照相机经度
    pol.camera.latitude = 35    # 照相机纬度
    pol.camera.altitude = 1316550       # 照相机海拔
    # pol.camera.heading = -60.333      # 照相机标题
    # pol.camera.tilt = 63.5           # 照相机倾斜
    # pol.camera.roll = 45              # 照相机滚动
    kml.save("商朝地图02.kml")
    # coords = tt['coord'][0]
    # # Create the gx:Track and style it
    # trk = kml.newgxtrack(name=None)
    # trk.linestyle.width = 3
    # trk.linestyle.color = Color.red
    # trk.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)
    # trk.newgxcoord(coords)
    # kml.save('商朝地图01' + "444.kml")

# altitude    67500


def parser_url(keywords, border, subdistrict=1, extensions="all"):

    """
    1. 仅仅要大外框
    2. 仅仅要子节点
    3. 要自己点与大外框
    """
    parameters={"keywords": keywords, "subdistrict": subdistrict, "extensions": extensions, "key": key}
    res = requests.get(url=gd_district_url, params=parameters).json()['districts'][0]
    if border == 1:
        name = res.get("name")
        polyline = res.get("polyline")
        center = res.get("center").split(",")
        polyline = [each.split(",") for each in polyline.split(";")]
        print(polyline)
        return {"name": name, "center": center, "polyline": polyline}



if __name__ == '__main__':
    url = "北京"
    res = parser_url(url, border=1)
    name = res.get('name')
    polyline = res.get('polyline')
    center = res.get('center')
    map_border(name, polyline, center)


























