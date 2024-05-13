import glob
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

imgs=glob.glob("./im3/*.png")

width=125
height=50

X=[]
Y=[]

for img in imgs:
    
    filename=os.path.basename(img)
    label=filename.split("_")[0] #["box 1","sayı",".png"]
    im=np.array(Image.open(img).convert("L").resize((width,height)))
    im=im/255
    X.append(im)
    Y.append(label)

X=np.array(X)
X=X.reshape(X.shape[0],width,height,1)

#8 farklı olası durumu 1-0 yapma (box1,box2,...box8)
def onehot_labels(values):
    lb=LabelEncoder()
    int_encoder=lb.fit_transform(values)
    onehot_encoder=OneHotEncoder(sparse=False)
    int_encoder=int_encoder.reshape(len(int_encoder),1)
    onehot_encoder=onehot_encoder.fit_transform(int_encoder)
    
    return onehot_encoder
            
        
Y=onehot_labels(Y)

x_Train,x_Test,y_Train,y_Test=train_test_split(X,Y,test_size=0.25,random_state=2)

#cnn model
model=Sequential()

model.add(Conv2D(32,kernel_size=(3,3),activation="relu",input_shape=(width,height,1)))
model.add(Conv2D(64,kernel_size=(3,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))  
model.add(Flatten())

model.add(Dense(128,activation="relu"))
model.add(Dropout(0.4)) 
model.add(Dense(9,activation="softmax"))



model.compile(loss="categorical_crossentropy",optimizer="Adam",metrics=["accuracy"])

model.fit(x_Train,y_Train,epochs=100,batch_size=64)

score_train=model.evaluate(x_Train,y_Train)
print("Eğitim Doğruluğu: %",score_train[1]*100)


score_test=model.evaluate(x_Test,y_Test)
print("Test Doğruluğu: %",score_test[1]*100)
            

open("model_json.json","w").write(model.to_json())
model.save_weights("xox_model.h5")   
    

            
            
            
            
            
            
            
            
            
            
            