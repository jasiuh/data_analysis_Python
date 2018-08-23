
print "#, True, Predicted"    
import numpy as np

#2D array of floats for storing training example attribute values
trainAttribute = np.loadtxt('iris-training-data.csv', delimiter = ",", usecols = (0,1,2,3), dtype = float)
#2D array of floats for storing testing example attribute values
testAttribute = np.loadtxt('iris-testing-data.csv', delimiter = ",", usecols = (0,1,2,3), dtype = float)
#1D array of strings for storing training example class labels
trainLabel = np.loadtxt('iris-training-data.csv', delimiter = ",", usecols = [4], dtype = str)
#1D array of strings for storing testing example class labels
testLabel = np.loadtxt('iris-testing-data.csv', delimiter = ",", usecols = [4], dtype = str)

#New 1D array containing the predicted labels
predictedClassLabels = []
#This will be a counter for the number of matches we get.
numMatches = 0

#For loop that iterates over training example attribute values
for i in range(len(trainAttribute)):
        #Compute the distance.
	dist = np.sqrt(np.sum((testAttribute[i] - trainAttribute)**2, axis = 1))
	minimumDist = np.argmin(dist)#Return minimum indices (or minimum shortest distances)
	predictedClassLabels.append(trainLabel[minimumDist])

#For loop that iterates over testing example class labels
for i in range(len(testLabel)):
	print i+1,testLabel[i],predictedClassLabels[i]# Output the true and predicted class label to the screen 
	if testLabel[i] == predictedClassLabels[i]:#Compare the labels
		numMatches += 1 #Increment number of correct matches
#Compute the accuracy
accuracy = (numMatches/float(len(testLabel))) * 100
accuracy = str(accuracy)#Cast to string in order to remove space between float and '%'.

#Print the accuracy that was computed.
print "Accuracy:",accuracy+"%"