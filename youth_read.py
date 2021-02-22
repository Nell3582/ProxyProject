#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

# 此脚本参考 https://raw.githubusercontent.com/Sunert/Scripts/master/Task/Youth_Read.js
# youth read 不支持 ac

import traceback
import time
import sys
import os
from util import send, requests_session
from datetime import datetime, timezone, timedelta
from concurrent.futures import ProcessPoolExecutor

# path = os.getcwd()
# zh1 = r'youth_data\zqreadbody_sswc.txt'
# zh2 = r'youth_data\zqreadbody_xxm.txt'

# filepaths = [zh1,zh2]

# for item , value in enumerate(filepaths):
#     with open( value,'r') as f:
#         exec(f'Read_BODY{item} = f.read()')

# body分割方式，默认 &
READ_BODY_SPLIT = '&'
READ_BODY0 ={
  'p': 'UwNMsLAQgw3E=h0-6Jj8on7af6ZV2ro0jIy20BO0Z9MQYsvQw26ibvbewmTKtpqQDLVML6SgYTaqi8PkhFrpysFm5XtQ31PFWhKPB7W7WNCUT5pk0siMSxT2KrPfghb2qnEl9Zm4LfZQ-SftC8vU8SoXxUd62sPBZM7F71cFeSFSky5PZSiMh-bKoospTGPGQgFUTOaFpJrZYXItsSYESUrbcMaglFGR-MvBH3Fd2LJ9jQpf9oH5Wwe4rWgxzhrgjsfMYvdOyShscEIl2XJARc_aeuKgK3rohy-l7y73wHUKcDUmK9h97GzE-b09xyJCcUIPLi978_ahrWf-7hOQiPi9wzEIPg9-Oks2R-9xnFC5MHQVUlEURxLQknWy2SEoRJOuI9CALzWGVhWEhG3unvm4jmf38GUxqe4UuGF-pSvUdJ3-_MMnKFPfkBdxwLp6W9nRAtVemerZFRXkTDOOX-hUrB0ini-M-odK3UipaRYj8mQ12ADG-iqsx3yrq9yDdQrOboJzn_12H4YcJynvsWyFC6DdKTi9BUUx8F2Y4usR8nmpPKe_8Sij9IsuPBe_WquOm3d2ys4QCLVKwON30QMPcCHz-PcvODEgjfFFb90C7RD4Ji9O47G9_TOLVcnHB5BQKecbPW2RU4ACqz_5xmxxd8qW8RHj8USPfCQLRX31ezcVZX4lUV5_I9i4vX5j5Yl8I7Vdb84lK_WaIAma9FKbMHi2zHg3IiZ2086k81T2URYmdl9AhRjQ2RVCjz_hOtv0RIqUc_ZiKWbMHIncS1aA5FTWjV5djhoE51CVZf3FVZEaLeMqbkt8gnJuI_OPrBSwQ_WaFW0vPHygkJZfTZIQWAamuChrw05H4wLNube8w1PNeNpS3jMSL6MnHq29i4H0KswwMSJU1N9aNvK20SXZTuZb5A_yCvNNoILLYjJYvm_ww5-RjTu3vCG2pguboceRc2HZ0fc3jqA11NqZ-79JjtWRbpySD_RKqu4MeApTWEMAP2G8wauf3xb1BOezmRmk99ZA9o1OOaxXZBWhP4Maqye8asHi9BoEnvs2GkVLzLugqCjFVEkAg98zRiSiSXHbkj--suNJtjYpkocPNQt5OaPjoyj55ufK--xV4P_nC_eEPe1V4fG-WNf0J06TnjRbHb7egnpPMjBE39hWvsbmOosU18aWfisQfqVPkOvy2u0VpGfRqW8PFUK_XFg1K12addrcsfysWzCN-2g0UJ-3IQeMGbJ0f-CG1VPaCTScuwG-Ve9DtR8WfjhqxYT8z2mcFZ_mtvaOf1EkLHSeyUAwpf7NE9hswX6yePa5c2ZhKBxwX1noH-j9EuH9leVtXTbNkmqw6QrnwnW1pkbFhmAdad2ioMevyP3wxOxQny4DWX8JY_oWEadOs1I-HS7PFIcUEy7sesdTLbHsTZTIsJGGNMpT4993YYktZaBljbGbbV9'
}
# 多账号
READ_BODYS = [READ_BODY0, ]

cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

def get_standard_time():
    """
  获取utc时间和北京时间
  :return:
  """
    # <class 'datetime.datetime'>
    utc_datetime = datetime.utcnow().replace(tzinfo=timezone.utc)  # utc时间
    beijing_datetime = utc_datetime.astimezone(timezone(timedelta(hours=8)))  # 北京时间
    return beijing_datetime

def read(body, i):
    """
  :param body:
  :return:
  """
    try:
        url = 'https://kandian.youth.cn/v5/article/complete.json'
        headers = {'User-Agent': 'KDApp/1.7.8 (iPhone; iOS 14.0; Scale/3.00)', 'Content-Type':
                   'application/x-www-form-urlencoded;charset=utf-8'}
        response = requests_session().post(
          url=url, headers=headers, data=body, timeout=30).json()
        if response['error_code'] == '0':
            if 'read_score' in response['items']:
                print(f"\n本次阅读获得{response['items']['read_score']}个青豆，请等待30s后执行下一次阅读\n")
                time.sleep(30)
            elif 'score' in response['items']:
                print(f"\n本次阅读获得{response['items']['score']}个青豆，即将开始下次阅读\n")
            elif 'max_notice' in response['items']:
                print(f"\n本次阅读获得{response['items']['max_notice']}个青豆，即将开始下次阅读\n")
        elif response['success'] == False:
            print(f'\n第{i}次阅读请求有误，请删除此请求\n')
        return
    except:
        print(traceback.format_exc())
        return

def run(body, index):
    beijing_datetime = get_standard_time()
    bodyList = body.split(READ_BODY_SPLIT)
    print(f'\n【中青看点账号{index}】{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'\n【中青看点账号{index}】总共{len(bodyList)}个body')
    for i in range(0, len(bodyList)):
        print(f'\n账号{index}开始中青看点第{i+1}次阅读')
        read(body=bodyList[i], i=i+1)
    print(f'\n【账号{index}中青结束】{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")}')

def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        for i in range(0, len(READ_BODYS)):
            executor.submit(run, READ_BODYS[i], i+1)
        executor.shutdown(wait=True)

    # 暂无通知
    # if beijing_datetime.hour == 23 and beijing_datetime.minute >= 0 and beijing_datetime.minute <= 10:
    #   send(title=title, content=result)
    # elif not beijing_datetime.hour == 23:
    #   print('未进行消息推送，原因：没到对应的推送时间点\n')
    # else:
    #   print('未在规定的时间范围内\n')

if __name__ == '__main__':
    main()