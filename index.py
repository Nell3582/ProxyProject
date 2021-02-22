
import json

def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent = 2)) 
    work_lst = event['Message'].split('&')
    for item in work_lst:
    	print(f'{"-"*30}脚本{item}开始执行{"-"*30}')
    	work = __import__(item)
    	work.run() #请确保所有脚本文件最终的调用函数是run(),否则无法执行
    return ("本次任务结束")
    


