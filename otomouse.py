import numpy as np
from keras.models import model_from_json
from mss import mss
from PIL import Image
import cv2
import pyautogui
import time
import keyboard
import record
from PIL import Image
from PIL import ImageGrab
import tkinter as tk
import random

rec=record.ScreenRecorder()

x=410
x_start, y_start =x+170,x+40

'''
    1.  2.  3.
    4.  5. 6.
    7.  8  9.
'''

cordinat_box={"box 1":[x+25,x-60],"box 2":[x+95,x-60],"box 3":[x+165,x-60],
              "box 4":[x+25,x+10],"box 5":[x+95,x+10],"box 6":[x+165,x+10],
              "box 7":[x+25,x+80],"box 8":[x+95,x+80],"box 9":[x+165,x+80]}

# model yükle
model = model_from_json(open("model_json.json","r").read())
model.load_weights("xox_model.h5")


mon={"top": 315, "left": 385, "width": 280, "height": 210}
sct=mss()


width=125
height=50


flag = False

def on_esc_press(e):
    global flag
    if e.name == 'esc':
        flag = True

keyboard.on_press(on_esc_press)
counter=0


hamle_list=[]
tum_olasılık=[1,2,3,4,5,6,7,8,9]


   
while True:
    
    time.sleep(2)
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im2 = np.array(im.convert("L").resize((width, height)))
    im2 = im2 / 255
    
    X =np.array([im2])
      
    #cv2.imshow("Ekran", X[0])
 
    # 'q' tuşuna basıldığında döngüyü sonlandır
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
    
    X_r = X.reshape(X.shape[0], width, height, 1)
    
    r = model.predict(X_r)
    result = np.argmax(r)+1
    
    if result in hamle_list:
        while True:
            yeni_hamle = random.choice(tum_olasılık)
            if yeni_hamle not in hamle_list:
                result = yeni_hamle
                break
                
    
     
    hamle_list.append(result)

    x=cordinat_box["box {}".format(result)][0]
    y=cordinat_box["box {}".format(result)][1]
    time.sleep(1)
    
    
    box_data="box"+str(result)
    print("Box: ",box_data)
    
    if len(hamle_list)>5:
        hamle_list.clear()
        counter=0
    
    # if counter>3:
    #     print(box_data)
    #     #rec.record_screen(box_data)
    #     time.sleep(3)
  
    
    pyautogui.click(x, y)   
    
    counter+=1
   
    if flag==True:
        print("Liste: ",hamle_list)
        print("Counter:",counter)
        break
    

    
    
    