import requests

# headers = {
#     'Host': 'kandian.youth.cn',
#     'User-Agent': 'okhttp/3.12.2',
# }

# params = (
#     ('catid', '0'),
#     ('op', '0'),
#     ('behot_time', '0'),
#     ('oid', '0'),
#     ('video_catid', '1453'),
#     ('access', 'WIFI'),
#     ('androidid', 'e425be03490b7b94'),
#     ('app_name', 'zqkd_app'),
#     ('app_version', '2.8.8'),
#     ('carrier', 'CMCC'),
#     ('channel', 'c1008'),
#     ('device_brand', 'HUAWEI'),
#     ('device_id', '50457564'),
#     ('device_model', 'LIO-AN00'),
#     ('device_platform', 'android'),
#     ('device_type', 'android'),
#     ('dpi', '240'),
#     ('fp', 'DuSypxlqjcilx6T9S7kwrEnD09AGXsVBNqd369NPEj+wnpBRXX7Vm61hqpFNFl3ue2RhU3ywqx6O9TrvFhLmC+cA'),
#     ('imei', '863064275407718'),
#     ('inner_version', '202102011723'),
#     ('language', 'zh-CN'),
#     ('memory', '2'),
#     ('mi', '0'),
#     ('mobile_type', '1'),
#     ('net_type', '1'),
#     ('network_type', 'WIFI'),
#     ('openudid', 'e425be03490b7b94'),
#     ('os_api', '25'),
#     ('os_version', 'LIO-AN00-user 7.1.2 LIO-AN00 700210126 release-keys'),
#     ('phone_sim', '1'),
#     ('request_time', '1613806099'),
#     ('resolution', '720x1280'),
#     ('rom_version', 'LIO-AN00-user 7.1.2 LIO-AN00 700210126 release-keys'),
#     ('sm_device_id', '20210212183314acc8b702bc06105566bf382c250a81ee015cf93ece20105f'),
#     ('storage', '61.39'),
#     ('szlm_ddid', 'DuSypxlqjcilx6T9S7kwrEnD09AGXsVBNqd369NPEj+wnpBRXX7Vm61hqpFNFl3ue2RhU3ywqx6O9TrvFhLmC+cA'),
#     ('uid', '53046866'),
#     ('version_code', '56'),
#     ('zqkey', 'MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzZtrhaKp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3gWyFfHqZsLm6apqGcXY'),
#     ('zqkey_id', 'bd26d98ae95c1dfd2820b29273515a89'),
#     ('sign', '48003e0456aba66b6361965829173ec5'),
# )

# response = requests.get('https://kandian.youth.cn/v3/article/lists.json', headers=headers, params=params)
# r = response.json()
# # print(r)
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.get('https://kandian.youth.cn/v3/article/lists.json?catid=0&op=0&behot_time=0&oid=0&video_catid=1453&access=WIFI&androidid=e425be03490b7b94&app_name=zqkd_app&app_version=2.8.8&carrier=CMCC&channel=c1008&device_brand=HUAWEI&device_id=50457564&device_model=LIO-AN00&device_platform=android&device_type=android&dpi=240&fp=DuSypxlqjcilx6T9S7kwrEnD09AGXsVBNqd369NPEj%2BwnpBRXX7Vm61hqpFNFl3ue2RhU3ywqx6O9TrvFhLmC%2BcA&imei=863064275407718&inner_version=202102011723&language=zh-CN&memory=2&mi=0&mobile_type=1&net_type=1&network_type=WIFI&openudid=e425be03490b7b94&os_api=25&os_version=LIO-AN00-user%207.1.2%20LIO-AN00%20700210126%20release-keys&phone_sim=1&request_time=1613806099&resolution=720x1280&rom_version=LIO-AN00-user%207.1.2%20LIO-AN00%20700210126%20release-keys&sm_device_id=20210212183314acc8b702bc06105566bf382c250a81ee015cf93ece20105f&storage=61.39&szlm_ddid=DuSypxlqjcilx6T9S7kwrEnD09AGXsVBNqd369NPEj%2BwnpBRXX7Vm61hqpFNFl3ue2RhU3ywqx6O9TrvFhLmC%2BcA&uid=53046866&version_code=56&zqkey=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzZtrhaKp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3gWyFfHqZsLm6apqGcXY&zqkey_id=bd26d98ae95c1dfd2820b29273515a89&sign=48003e0456aba66b6361965829173ec5', headers=headers)

# # print(r)
# lst = r['items']
# # print(lst)
# # lst2 = [i['id'] for i in lst]
# # print(lst2)
# lst2 =[]
# for i in lst:
#     if('id' in i.keys()):
#         lst2.append(i['id'])
# print(lst2)
a = ['36371922', '36350545', '36258912', '36354513', '36361731', '36385817', '36372495', '36378208', '36384000', '36385596', '36356196', '36366811']


headers = {
    'Token': 'dd71bb6afe5de995d0490c3a2d26dbf5',
    'Host': 'kandian.youth.cn',
    'User-Agent': 'okhttp/3.12.2',
}

data = {
  'access': 'WIFI',
  'androidid': 'e425be03490b7b94',
  'app-version': '2.8.8',
  'app_name': 'zqkd_app',
  'app_version': '2.8.8',
  'article_id': '36350545',
  'carrier': 'CMCC',
  'channel': 'c1008',
  'device_brand': 'HUAWEI',
  'device_id': '50457564',
  'device_model': 'LIO-AN00',
  'device_platform': 'android',
  'device_type': 'android',
  'dpi': '240',
  'fp': 'DuSypxlqjcilx6T9S7kwrEnD09AGXsVBNqd369NPEj+wnpBRXX7Vm61hqpFNFl3ue2RhU3ywqx6O9TrvFhLmC+cA',
  'from': '4',
  'imei': '863064275407718',
  'inner_version': '202102011723',
  'language': 'zh-CN',
  'memory': '2',
  'mi': '0',
  'mobile_type': '1',
  'net_type': '1',
  'network_type': 'WIFI',
  'openudid': 'e425be03490b7b94',
  'os_api': '25',
  'os_version': 'LIO-AN00-user 7.1.2 LIO-AN00 700210126 release-keys',
  'request_time': '1613806280',
  'resolution': '720x1280',
  'rom_version': 'LIO-AN00-user 7.1.2 LIO-AN00 700210126 release-keys',
  'sim': '1',
  'sm_device_id': '20210212183314acc8b702bc06105566bf382c250a81ee015cf93ece20105f',
  'storage': '61.39',
  'stype': 'wx',
  'subv': '1.2.2',
  'szlm_ddid': 'DuSypxlqjcilx6T9S7kwrEnD09AGXsVBNqd369NPEj+wnpBRXX7Vm61hqpFNFl3ue2RhU3ywqx6O9TrvFhLmC+cA',
  # 'token': 'dd71bb6afe5de995d0490c3a2d26dbf5',
  'uid': '53046866',
  'version_code': '56',
  'zqkey': 'MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzZtrhaKp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3gWyFfHqZsLm6apqGcXY',
  'zqkey_id': 'bd26d98ae95c1dfd2820b29273515a89'
}

response = requests.post('https://kandian.youth.cn/v6/article/share/put.json', headers=headers, data=data)
r = response.json()
print(r)

