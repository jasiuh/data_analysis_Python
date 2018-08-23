# This project utilizes the Auto MPG Data Set from the UCI Machine Learning Repository.
# This is a regression problem. I predict how may miles per gallon(mpg) a car will 
# consume based on its cylinders, displacement, horsepower, weight, and acceleration.
# Download Link: https://archive.ics.uci.edu/ml/datasets/auto+mpg


import pandas as pd
import numpy as np
#These will be for RMSE calculations.
from sklearn.metrics import mean_squared_error
from math import sqrt

# Data is saved as a .csv
# Read it using Pandas
data = pd.read_csv('auto.csv')

#Store in dataframe
df = pd.DataFrame(data)

# There are a few '?' in the Horsepower column so I remove them.
df = df[df.horsepower != '?']

#Print the top of the data.
print df.head()

##################################################################

#Now, we plot the cylinders, displacement, horsepower, weight, and acceleration vs. mpg to see relationships.
import matplotlib.pyplot as plt 


plt.scatter(df['cylinders'], df['mpg'])
plt.title("MPG vs Number of Cylinders")
plt.xlabel('Cylinders')
plt.ylabel('MPG')
plt.show()

plt.scatter(df['displacement'], df['mpg'])
plt.title("MPG vs Displacement")
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.show()


plt.scatter(df['horsepower'], df['mpg'])
plt.title("MPG vs Horsepower")
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.show()

plt.scatter(df['weight'], df['mpg'])
plt.title("MPG vs Weight")
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

plt.scatter(df['acceleration'], df['mpg'])
plt.title("MPG vs Acceleration")
plt.xlabel('Acceleration')
plt.ylabel('MPG')
plt.show()

###########################################################

#Split dataset into training and testing sets.
from sklearn.model_selection import train_test_split

#Set the x's and y's for the model.
y = ['mpg']

#How do these affect MPG of car?
x = ['cylinders','displacement','horsepower','weight','acceleration']
Y = df[y]
X = df[x]

# Test size = 20% of dataset (other 80% is for training)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=5)

print "Training set samples: ", len(X_train)
print "Testing set samples:  ", len(X_test)

###########################################################

#Linear Regression
from sklearn.linear_model import LinearRegression

regression = LinearRegression()
regression.fit(X_train,Y_train)
Y_predict = regression.predict(X_test)

#RMSE
rmse = sqrt(mean_squared_error(y_true=Y_test,y_pred=Y_predict))
print 'RMSE:  ', rmse
print 'Score: ', regression.score(X_train,Y_train)

########################################################

#Gradient Boost
from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor()
gbr.fit(X_train,Y_train)
Y_predict = gbr.predict(X_test)

#RMSE
rmse = sqrt(mean_squared_error(y_true=Y_test,y_pred=Y_predict))
print 'RMSE:  ', rmse
print 'Score: ', gbr.score(X_train,Y_train)

########################################################

#Support Vector Machine
from sklearn.svm import LinearSVR

svm = LinearSVR()
svm.fit(X_train,Y_train)
Y_predict = svm.predict(X_test)

#RMSE
rmse = sqrt(mean_squared_error(y_true=Y_test,y_pred=Y_predict))
print 'RMSE:  ', rmse
print 'Score: ', svm.score(X_train,Y_train)

#########################################################

#Decision Tree
from sklearn.tree import DecisionTreeRegressor

tree = DecisionTreeRegressor()
tree.fit(X_train,Y_train)
Y_predict = tree.predict(X_test)

#RMSE
rmse = sqrt(mean_squared_error(y_true=Y_test,y_pred=Y_predict))
print 'RMSE:  ', rmse
print 'Score: ', tree.score(X_train,Y_train)

########################################################

#Let's do some testing and compare the four techniques.

#Mazda RX3 - actual MPG is 18.
rx3 = [[3,70,90,2124,13.5]]

rx3_regression = regression.predict(rx3)
rx3_gbr = gbr.predict(rx3)
rx3_svm = svm.predict(rx3)
rx3_tree = tree.predict(rx3)

#Let's see which model is most accurate:
print 'MPG predictions for Mazda RX3:'
print 'Regression: ', rx3_regression
print 'Gradient Boost: ', rx3_gbr
print 'Support Vector Machine: ', rx3_svm
print 'Decision Tree: ', rx3_tree


#Pontiac Grand Prix - actual MPG is 16.
gp = [[8,400,230,4278,9.50]]

gp_regression = regression.predict(gp)
gp_gbr = gbr.predict(gp)
gp_svm = svm.predict(gp)
gp_tree = tree.predict(gp)

#Let's see which model is most accurate:
print 'MPG predictions for Pontiac Grand Prix:'
print 'Regression: ', gp_regression
print 'Gradient Boost: ', gp_gbr
print 'Support Vector Machine: ', gp_svm
print 'Decision Tree: ', gp_tree


#Honda Civic - actual MPG is 44.6.
civic = [[4,91,67,1850,13.8]]

civic_regression = regression.predict(civic)
civic_gbr = gbr.predict(civic)
civic_svm = svm.predict(civic)
civic_tree = tree.predict(civic)

#Let's see which model is most accurate:
print 'MPG predictions for Honda Civic:'
print 'Regression: ', civic_regression
print 'Gradient Boost: ', civic_gbr
print 'Support Vector Machine: ', civic_svm
print 'Decision Tree: ', civic_tree


#Plymouth Duster - actual MPG is 22.
duster = [[6,198,95,2833,15.5]]

duster_regression = regression.predict(duster)
duster_gbr = gbr.predict(duster)
duster_svm = svm.predict(duster)
duster_tree = tree.predict(duster)

#Let's see which model is most accurate:
print 'MPG predictions for Plymouth Duster:'
print 'Regression: ', duster_regression
print 'Gradient Boost: ', duster_gbr
print 'Support Vector Machine: ', duster_svm
print 'Decision Tree: ', duster_tree



#Now we'll try with data that isn't in the original dataset.
#Taken from https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C3)
#1980 Chevy Corvette - actual MPG is ~12.3
corvette = [[8,350,230,3520,7.9]]
corvette_regression = regression.predict(corvette)
corvette_gbr = gbr.predict(corvette)
corvette_svm = svm.predict(corvette)
corvette_tree = tree.predict(corvette)
#Let's see which model is most accurate:
print 'MPG predictions for Chevy Corvette (12.3 MPG):'
print 'Regression: ', corvette_regression
print 'Gradient Boost: ', corvette_gbr
print 'Support Vector Machine: ', corvette_svm
print 'Decision Tree: ', corvette_tree
print ""


#Taken from http://www.classicandperformancecar.com/jaguar/xjs/1750/1975-1981-jaguar-xj-s
#1975 Jaguar XJ-S - actual MPG is ~14
jaguar = [[12,326,285,3858,6.9]]
jaguar_regression = regression.predict(jaguar)
jaguar_gbr = gbr.predict(jaguar)
jaguar_svm = svm.predict(jaguar)
jaguar_tree = tree.predict(jaguar)
#Let's see which model is most accurate:
print 'MPG predictions for Jaguar XJ-S (14 MPG):'
print 'Regression: ', jaguar_regression
print 'Gradient Boost: ', jaguar_gbr
print 'Support Vector Machine: ', jaguar_svm
print 'Decision Tree: ', jaguar_tree

########################################################################################

#Neural Network

#set "KERAS_BACKEND=theano"
#set “MKL_THREADING_LAYER=GNU”
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2, l1
from keras.optimizers import SGD

# We normalize our features before applying neural network.
# StandardScaler() will normalize so that each column
# will have mean = 0 and standard deviation = 1.
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = Sequential()
model.add(Dense(5, activation = 'sigmoid', input_dim = X_train.shape[1]))
model.add(Dense(1, kernel_initializer='normal'))

sgd = SGD(lr=1)
model.compile(loss='mean_squared_error', optimizer='sgd')  
model.fit(X_train, Y_train, verbose=2)
Y_predict = model.predict(X_test)

rmse = sqrt(mean_squared_error(y_true=Y_test,y_pred=Y_predict))
print "RMSE: ", rmse


#Let's test it.

#Mazda RX3 - actual MPG is 18.
rx3 = [[3,70,90,2124,13.5]]
rx3_nn = model.predict([rx3])
print "Neural Network - Mazda RX3 (18 MPG): ", rx3_nn


#Pontiac Grand Prix - actual MPG is 16.
gp = [[8,400,230,4278,9.50]]
gp_nn = model.predict([gp])
print "Neural Network - Pontiac Grand Prix (16 MPG): ", gp_nn

