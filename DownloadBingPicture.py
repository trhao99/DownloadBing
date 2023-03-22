# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import ctypes  
import win32api, win32con, win32gui
import requests
import os
import json
from PIL import Image
import time
import socket
from tkinter import *
import threading
base_path = "C:\\Users\\19279\\Pictures\\Bing\\"
def closewindows(tk):
    for radio in range(100):
        tk.attributes("-alpha", 1-0.01*radio)
        #print('radio:' + str(radio))
        time.sleep(0.05)
    #print('要摧毁')
    tk.destroy()
    #print('已摧毁')
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
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp, 1+2)
def Judge(time):
    filelist = os.listdir(base_path)
    if len(filelist)==0:
        return False
    #print(filelist[-1])
    #print('BingPicture_' + time + '.jpg')
    return filelist[-1] ==('BingPicture_' + time + '.jpg') 
def windowstext(text):
    tk=Tk()
    #创建画布
    tk.title('今日bing')
    canvas=Canvas(tk,width=1600, height=60)
    canvas.pack()
    #在画布上创建文字
    canvas.create_text(600, 40, text=text)
    return tk
if __name__ == '__main__':
    if isNetOK():
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
        image_path = base_path + image_name
        with open(image_path, 'wb') as f:
                f.write(image.content)
                f.close()
        setWallpaper(image_path)
        tk = windowstext(text)
        t = threading.Thread(target=closewindows,args=(tk,))
        t.start()
        tk.mainloop()