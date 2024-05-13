import cv2
import time
import keyboard
import glob
import mss
from PIL import Image
from skimage.metrics import structural_similarity as ssim

class ScreenRecorder:
    def __init__(self):
        self.monitor = {"top": 315, "left": 385, "width": 280, "height": 210}
        self.save_directory = "./img"
        self.flag = False
        self.sct = mss.mss()

    def resim_sayisi(self):
        jpg_files = glob.glob(self.save_directory + '/*.png')
        print("Toplam Resim Sayisi: ", len(jpg_files))
        return len(jpg_files) +3000

    def process_image(self, img_path):
        img = cv2.imread(img_path, 0)
        h, w= img.shape
   

        ret, threshol_img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY_INV)
        ret, threshol2_img = cv2.threshold(img, 95, 255, cv2.THRESH_BINARY)

        erged_img = cv2.bitwise_and(threshol_img, threshol2_img)
        
    
        
        cv2.imwrite(img_path,   erged_img  )

    def record_screen(self, key):
        img_count = self.resim_sayisi()
        img = self.sct.grab(self.monitor)
        im = Image.frombytes("RGB", img.size, img.rgb)
    
        im.save("./{}/{}_{}.png".format(self.save_directory,key,img_count))
        self.process_image("./{}/{}_{}.png".format(self.save_directory,key,img_count))
        

    def on_esc_press(self, e):
        if e.name == 'esc':
            self.flag = True

    def start_recording(self):
        """
        keyboard.on_press(self.on_esc_press)
        try:      
           if keyboard.is_pressed("q"):
               self.record_screen("box1")
               time.sleep(0.2)
           elif keyboard.is_pressed("w"):
               self.record_screen("box2")
               time.sleep(0.2)
           elif keyboard.is_pressed("e"):
               self.record_screen("box3")
               time.sleep(0.2)
           elif keyboard.is_pressed("a"):
               self.record_screen("box4")
               time.sleep(0.2)
           elif keyboard.is_pressed("s"):
               self.record_screen("box5")
               time.sleep(0.2)
           elif keyboard.is_pressed("d"):
               self.record_screen("box6")
               time.sleep(0.2)
           elif keyboard.is_pressed("z"):
               self.record_screen("box7")
               time.sleep(0.2)
           elif keyboard.is_pressed("x"):
               self.record_screen("box8")
               time.sleep(0.2)
           elif keyboard.is_pressed("c"):
               self.record_screen("box9")
               time.sleep(0.2)

        except RuntimeError:
            print("")
            
        """
        
        while not self.flag:
            try:      
                if keyboard.is_pressed("q"):
                    self.record_screen("box1")
                    time.sleep(0.2)
                elif keyboard.is_pressed("w"):
                    self.record_screen("box2")
                    time.sleep(0.2)
                elif keyboard.is_pressed("e"):
                    self.record_screen("box3")
                    time.sleep(0.2)
                elif keyboard.is_pressed("a"):
                    self.record_screen("box4")
                    time.sleep(0.2)
                elif keyboard.is_pressed("s"):
                    self.record_screen("box5")
                    time.sleep(0.2)
                elif keyboard.is_pressed("d"):
                    self.record_screen("box6")
                    time.sleep(0.2)
                elif keyboard.is_pressed("z"):
                    self.record_screen("box7")
                    time.sleep(0.2)
                elif keyboard.is_pressed("x"):
                    self.record_screen("box8")
                    time.sleep(0.2)
                elif keyboard.is_pressed("c"):
                    self.record_screen("box9")
                    time.sleep(0.2)

            except RuntimeError:
                continue
            
        










