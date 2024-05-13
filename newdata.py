import os
from PIL import Image, ImageOps

# Dosya yolunu belirtin
dosya_yolu = "img"

# Hedef klasörü oluşturun
hedef_klasör = "im3"
if not os.path.exists(hedef_klasör):
    os.makedirs(hedef_klasör)

# Dosya yolundaki tüm dosyaları alın
dosya_listesi = os.listdir(dosya_yolu)

# Box5 ile başlayan resimleri seçin ve işleyin
for dosya in dosya_listesi:
    box_name="box9"
    if dosya.startswith(box_name):
        dosya_yolu = os.path.join("IMG", dosya)
        img = Image.open(dosya_yolu)
        # Resmi 90 derece döndürün
        döndürülmüş_img = img.rotate(270, fillcolor="white",resample=Image.BILINEAR)
        width, height = döndürülmüş_img.size
        #döndürülmüş_img = döndürülmüş_img.crop((0, -10, width, height))
        döndürülmüş_img= ImageOps.expand(döndürülmüş_img, border=(0, 10), fill='white')
        
        # Resmi kırpın (üstten 8, sağdan 3, soldan 2, aşağıdan 5)
        #genişlik, yükseklik = döndürülmüş_img.size
        #genişlik, yükseklik = img.size
        
        #img = img.crop((80,0, genişlik, yükseklik))
        
        #1-7 2-4  3-1 4-8 5-5 6-2 7-9 8-6 9-3
        #1-9 
        # Yeni dosya adını oluşturun
        yeni_dosya_adı = ((dosya_yolu[4:].split(".")[0])).replace(box_name,"box7")+"_270"+".png"
        yeni_dosya_yolu = os.path.join(hedef_klasör, yeni_dosya_adı)
        print(yeni_dosya_adı)
        # Döndürülmüş ve kırpılmış resmi kaydedin
        döndürülmüş_img.save(yeni_dosya_yolu)

print("İşlem tamamlandı.")
