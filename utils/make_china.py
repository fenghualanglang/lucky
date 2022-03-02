import json
import requests
import simplekml
from simplekml import Kml, Types, Snippet, Color


from settingConf.constants import (
    key,
    gd_district_url
)

# area_name = request.data.get('area_name')  # 城市名
# line_color = request.data.get('line_color')  # 线颜色
# line_wide = request.data.get('line_wide')  # 线宽



def map_border(name, polyline, center, line_color, line_wide):
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


def search_china_district(name, polyline, center):
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
    pol.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)

    pnt =kml.newpoint(name=name, coords=[center], )  # lon, lat, optional height
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

    # pol.altitudemode = simplekml.AltitudeMode.relativetoground
    # pol.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
    pol.camera.longitude = center[0]   #照相机经度      112.157
    pol.camera.latitude = center[1]        # 照相机纬度     35
    pol.camera.altitude = 2316550          # 照相机海拔

    # pol.camera.heading = -60.333      # 照相机标题
    # pol.camera.tilt = 63.5           # 照相机倾斜
    # pol.camera.roll = 45              # 照相机滚动
    kml.save("商朝地图03.kml")
    # coords = tt['coord'][0]
    # # Create the gx:Track and style it
    # trk = kml.newgxtrack(name=None)
    # trk.linestyle.width = 3
    # trk.linestyle.color = Color.red
    # trk.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)
    # trk.newgxcoord(coords)
    # kml.save('商朝地图01' + "444.kml")

    # altitude    67500





from utils.search_china import ali_china_district

def china_district_bound():
    """
    查询  不带子区域
    :return:
    """
    each = ali_china_district()["features"][0]
    name = each.get("properties")["name"]
    center = each.get("properties")["center"]
    coordinates = each.get("geometry")["coordinates"]

    kml = Kml()
    fol = kml.newfolder(name='polygon')

    for idx, coords in enumerate(coordinates):
        coords = coords[0]
        lin = fol.newlinestring(name=f"coord-{idx}", coords=coords)
        lin.style.linestyle.color = simplekml.Color.red  # Red
        lin.style.linestyle.width = 2  # 10 pixels

    point = kml.newfolder(name='point')
    pnt = point.newpoint(name=name)
    pnt.coords = [center]
    # pnt.style.iconstyle.scale = 3  # Icon thrice as big
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

    kml.save(f"{name}.kml")



def china_district_bound_full():

    each = ali_china_district()["features"][0]
    name = each.get("properties")["name"]
    center = each.get("properties")["center"]
    coordinates = each.get("geometry")["coordinates"]

    kml = Kml()
    fol = kml.newfolder(name='polygon')

    for idx, coords in enumerate(coordinates):
        coords = coords[0]
        lin = fol.newlinestring(name=f"coord-{idx}", coords=coords)
        lin.style.linestyle.color = simplekml.Color.red  # Red
        lin.style.linestyle.width = 2  # 10 pixels

    point = kml.newfolder(name='point')
    pnt = point.newpoint(name=name)
    pnt.coords = [center]
    # pnt.style.iconstyle.scale = 3  # Icon thrice as big
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

    kml.save(f"{name}.kml")




if __name__ == '__main__':
    address = "河南"
    from utils.search_china import search_district
    # res = search_district(address)
    china_district_bound()
    # name = res.get('name')
    # polyline = res.get('polyline')
    # center = res.get('center')
    # search_china_district(name, polyline, center)
    # china_district_bound()





