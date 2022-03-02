










import requests

def china_point():

    # 根据 地理位置查找经纬度
    url = 'http://127.0.0.1:8000/api/v1/china/point'
    # params = {"location": "丰台"}
    params = {"location": "86.481488,39.990464", "type": "2"}
    res = requests.get(url, params=params)
    print(res.json())



if __name__ == '__main__':
    china_point()












