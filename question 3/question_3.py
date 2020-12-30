#Name : AnnieoYang
#Finished Date:17/12/2020
#Using tensorflow keras as the predict method

from tensorflow.keras.layers import Input,Dense,Activation
from tensorflow.keras.models import Model
from tensorflow.keras.metrics import MeanSquaredError

def createModel():
  """
  Initialization of the model 3 hidden layer activation relu, loss mean squared error
  """
  inp = Input(shape=(3,))
  x = Dense(4,activation='relu',use_bias=False)(inp)
  x = Dense(4,activation='relu',use_bias=False)(x)
  x = Dense(1,activation='relu',use_bias=False)(x)
  model = Model(inp,x)
  model.compile(loss="mean_squared_error",optimizer='sgd',metrics=[MeanSquaredError()])
  return model
#model initilation
mod = createModel()

mod.summary()

import pandas as pd
#reading data

x_train = pd.read_csv('train_data.txt',sep='\t')
x_test = pd.read_csv('test_data.txt',sep="\t")[:2]

y_train = pd.read_csv('train_truth.txt',sep='\t')
y_test  = pd.read_csv('test_predicted_example.txt',sep='\t')
#Training
mod.fit(x_train,y_train,batch_size=512,epochs=100,validation_data=(x_test,y_test),shuffle=True)

test_valid = pd.read_csv('test_data.txt',sep="\t")
#making predictions
y = mod.predict(test_valid)
w = open("test_predicted.txt","w")
w.write("y\n")
for i in y:
  w.write(str(i[0])+"\n")
w.close()

