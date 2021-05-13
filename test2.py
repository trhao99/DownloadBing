from tkinter import *
import ctypes  
import requests
import os
import json
from PIL import Image
import socket
import time
import threading
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
data = requests.get(url)
#print(data.text)
json_data = json.loads(data.text)
#print(json_data['images'][0]['url'])
text = json_data['images'][0]['copyright']
tk=Tk()
tk.title('今日bing')
#创建画布
canvas=Canvas(tk,width=1600,height=60)
canvas.pack()
#在画布上创建文字
canvas.create_text(600,40,text=text)
def closewindows():
    for radio in range(100):
        tk.attributes("-alpha", 1-0.01*radio)
        #print('radio:' + str(radio))
        time.sleep(0.05)
    tk.destroy()
t = threading.Thread(target=closewindows)
t.start()
tk.mainloop()