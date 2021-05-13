# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import ctypes  
import requests
import os
import json
from PIL import Image
import time
import socket
import datetime
hours = 24
if __name__ == '__main__':
    while 1:
        starttime = datetime.datetime.now()
        #print("联网了")
        url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        base_url = "https://cn.bing.com"
        timedata = time.strftime('%Y%m%d',time.localtime(time.time()))
        # if Judge(timedata)==False:
        #print("没下载新版壁纸")
        data = requests.get(url)
        #print(data.text)
        json_data = json.loads(data.text)
        #print(json_data['images'][0]['url'])
        image = requests.get(base_url + json_data['images'][0]['url'])
        text = json_data['images'][0]['copyright']
        image_part_name = json_data['images'][0]['enddate']
        image_name = "BingPicture_" + image_part_name + ".jpg"
        new_dir = "/root/Projects/py_projects/TestWebProject/static/smallimage/"
        image_path = "/root/Projects/py_projects/TestWebProject/static/BingPicture/" + image_name
        with open(image_path, 'wb') as f:
                f.write(image.content)
                f.close()
        image = Image.open("/root/Projects/py_projects/TestWebProject/static/BingPicture/" + image_name)
        image_size = image.resize((35, 35),Image.ANTIALIAS)
        image_size.save(new_dir + img)
        with open('/root/Projects/py_projects/TestWebProject/static/BingText.txt','a+') as b:
            b.write(text + '\n')
        endtime = datetime.datetime.now()
        time.sleep(1000*3600*hours-(endtime-starttime).seconds)