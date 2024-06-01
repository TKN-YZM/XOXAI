# XOX (Tic-Tac-Toe) Bot: Görüntü İşleme ve Derin Öğrenme (CNN) ile

Bu proje, görüntü işleme ve derin öğrenme tekniklerini kullanarak XOX (tic-tac-toe) oyununu Google'ın orta ve kolay seviye botlarına karşı otomatik olarak oynayan bir sistem geliştirmeyi amaçlamaktadır. Convolutional Neural Networks (CNN) kullanarak eğitilmiş bu bot, oyun tahtasının durumunu analiz eder ve en iyi hamleyi belirler.


<div align="center">
  <img  src="https://github.com/TKN-YZM/XOXAI/blob/main/pic.jpg" alt="Proje Kod">
</div>


## Özellikler

- **Görüntü İşleme:** Oyun tahtasının durumunu algılar ve analiz eder.
- **CNN Tabanlı Karar Verme:** Derin öğrenme modeli kullanarak en iyi hamleyi belirler.
- **Otomatik Oynama:** Google'ın XOX botuna karşı otomatik olarak oynar. (pyautogui kütüphanesi ile)
- **Seviye Desteği:** Hem orta hem de kolay seviye botlarına karşı oynayabilir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılım ve kütüphanelere ihtiyacınız olacak:

- Python 3.8+
- OpenCV (PIL vb)
- TensorFlow / Keras
- NumPy
- Pyautogui / PIL 

## Kurulum

1. **Depoyu Klonlayın:**

    ```bash
    git clone https://github.com/TKN-YZM/XOXAI.git
    cd xox-bot
    ```

2. **Gereksinimleri Yükleyin:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Modelleri İndirin veya Eğitin:**
    - Eğer hazır modelleriniz varsa, bunları `models/` klasörüne yerleştirin.
    - Eğer modeli kendiniz eğitmek istiyorsanız, [Model Eğitimi](#train_cnn) bölümüne göz atın.

## Kullanım

1. **Botu Başlatın:**

    ```bash
    python otomouse.py
    ```

2. **Oyun Ekranı:** Google'ın XOX oyun ekranını açın ve botun oynamasını izleyin.


## Model Eğitimi

1. **Veri Hazırlama:**
   - `im3/` klasörlerine görüntü verilerini yerleştirin.
   
2. **Modeli Eğitme:**
   - `train/` klasöründe bulunan dosyalarını kullanarak modeli eğitin.
   
3. **Hamle Kaydetme:**
   - Eğitilmiş modeli `record/` klasörüne kaydedin.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için `LICENSE` dosyasına bakın.

