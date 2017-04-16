from keras.models import Sequential
from keras.layers import Dense
from keras import metrics

import numpy as np

np.random.seed(2)

dataset= np.loadtxt("allfkndata.csv",delimiter=",")

x= dataset[:,15:]
y= dataset[:,0:15]



print x
print "Okay\n"
print y

model= Sequential()
model.add(Dense(20,input_dim=33,activation='relu'))
model.add(Dense(15,activation='relu'))
model.add(Dense(15,activation='relu'))

model.compile(loss = 'mean_squared_error', optimizer='adam',  metrics=[metrics.mae, metrics.categorical_accuracy])

model.fit(x,y,epochs=2000,batch_size=70)

#scores = model.evaluate(x, y)
#print scores

predictions = model.predict(x)
# round predictions
#rounded = [round(p) for t in tt for tt in predictions]

jobs= {0:"",1:"",2:"",3:" Internet",4:" Software",5:"",6:" Medicine",7:"",8:" Artist",9:"",10:" Music",11:" Sportsman",12:" Science and Technology",13:" Theatre/Actor",14:" Human Resource"}

print(predictions)
print y

#for i in range(0,20):
	#index=predictions.np.index(max(predictions[i]))
	#print (index," : ", max(predictions[i]))
#	print predictions[i]


#print "\n\n\n"

print "According to my algorithm, you should be a: \n"
for i in range(0,500):
	#max_value = max(predictions[i])
	#max_index = predictions.index(max_value)
	#print(max_value,"  ",max_index)

	import operator
	index, value = max(enumerate(predictions[i]), key=operator.itemgetter(1))
	#predition[i][index]=0;
	print(index," : ",value," : ",jobs[index])
	#index, value = max(enumerate(predictions[i]), key=operator.itemgetter(1))
	

	
