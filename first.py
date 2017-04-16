from keras.models import Sequential
from keras.layers import Dense

import numpy as np

np.random.seed(1)

dataset= np.loadtxt("lel.csv",delimiter=",")

x= dataset[:,0:3]
y= dataset[:,3]

#print x
#print "Okay\n"
#print y

model= Sequential()
model.add(Dense(8,input_dim=3,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss = 'mean_squared_error', optimizer='adam',metrics=['accuracy'])

model.fit(x,y,epochs=5000)

#scores = model.evaluate(x, y)
#print scores

predictions = model.predict(x)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
