# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import ctypes  
import win32api, win32con
import requests
import os
import json
from PIL import Image
import time
import socket
def isNetOK(address=('www.baidu.com',443)):
    s=socket.socket()
    s.settimeout(3)
    status = s.connect_ex(address)
    if status == 0:
        s.close()
        return True
    else:
        #print("没联网")
        return False
def setWallpaper( bmp ):
    import win32api, win32con, win32gui
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp, 1+2)
def Judge(time):
    path = "D:\BingPicture\\"
    filelist = os.listdir(path)
    if len(filelist)==0:
        return False
    #print(filelist[-1])
    #print('BingPicture_' + time + '.jpg')
    return filelist[-1] ==('BingPicture_' + time + '.jpg') 
if __name__ == '__main__':
    if isNetOK():
        #print("联网了")
        url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        base_url = "https://cn.bing.com"
        timedata = time.strftime('%Y%m%d',time.localtime(time.time()))
        if Judge(timedata)==False:
            #print("没下载新版壁纸")
            data = requests.get(url)
            #print(data.text)
            json_data = json.loads(data.text)
            #print(json_data['images'][0]['url'])
            image = requests.get(base_url + json_data['images'][0]['url'])
            image_part_name = json_data['images'][0]['enddate']
            image_name = "BingPicture_" + image_part_name + ".jpg"
            image_path = "D:\BingPicture\\" + image_name
            with open(image_path, 'wb') as f:
                    f.write(image.content)
                    f.close()
            setWallpaper(image_path)