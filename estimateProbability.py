
import pandas as pd

#Assign empty dict to data variable
data = {}
#Ask user for number of instances
instances = int(raw_input("Enter the number of car instances: "))

#Iterate through number of instances, store each instance in dict.
for x in range (instances):
	#Ask user for input.
    instance = str(raw_input("Enter the make,model,type,rating: "))
	#Parse the input
    line = instance.split(',')
	#Store the input string into data dictionary
    data[x] = line
    
print ""

#Assign the data dictionary to a dataframe.
frame = pd.DataFrame(data)

#Transpose the dataframe to switch columsn and rows.
frame = frame.T

#Assign the appropriate names to each column.
frame.columns = ['make', 'model', 'type', 'rating']

#Print the dataframe.
print frame
print ""

#Initialize counter for ratings to zero
countA = 0
countB = 0
countC = 0
countD = 0
countF = 0

#Iterate over ratings and count occurence of each rating
for numRatings in frame['rating']:
    if numRatings == 'A':
        countA +=1
    if numRatings == 'B':
        countB +=1
    if numRatings == 'C':
        countC +=1
    if numRatings == 'D':
        countD +=1
    if numRatings == 'F':
        countF +=1   

#Here is the probability calculation for each rating:
calcA = float(countA)/float(instances)
calcB = float(countB)/float(instances)
calcC = float(countC)/float(instances)
calcD = float(countD)/float(instances)
calcF = float(countF)/float(instances)

#If any rating exists, print its repsective probability:
#These are formatted to print to six decimal places with format()
if countA != 0:
    print "Prob(rating=A) = ",format(calcA, '.6f')
if countB != 0:
    print "Prob(rating=B) = ",format(calcB, '.6f')
if countC != 0:
    print "Prob(rating=C) = ",format(calcC, '.6f')
if countD != 0:
    print "Prob(rating=D) = ",format(calcD, '.6f')
if countF != 0:
    print "Prob(rating=F) = ",format(calcF, '.6f')
    
print ""

#These are to count the number of instances
#for x and f in Prob(x,f). 
countCoupeA = 0
countCoupeB = 0
countCoupeC = 0
countCoupeD = 0
countCoupeF = 0
countSedanA = 0
countSedanB = 0
countSedanC = 0
countSedanD = 0
countSedanF = 0
countSUVA = 0
countSUVB = 0
countSUVC = 0
countSUVD = 0
countSUVF = 0

#Iterate through columns "type" and "rating".
for a,b in zip(frame['type'], frame['rating']):    
    if a=='coupe' and b=='A':
        countCoupeA += 1
    if a=='sedan' and b=='A':
        countSedanA += 1
    if a=='SUV' and b=='A':
        countSUVA += 1
    if a=='coupe' and b=='B':
        countCoupeB += 1
    if a=='sedan' and b=='B':
        countSedanB += 1
    if a=='SUV' and b=='B':
        countSUVB += 1
    if a=='coupe' and b=='C':
        countCoupeC += 1
    if a=='sedan' and b=='C':
        countSedanC += 1
    if a=='SUV' and b=='C':
        countSUVC += 1
    if a=='coupe' and b=='D':
        countCoupeD += 1
    if a=='sedan' and b=='D':
        countSedanD += 1
    if a=='SUV' and b=='D':
        countSUVD += 1
    if a=='coupe' and b=='F':
        countCoupeF += 1
    if a=='sedan' and b=='F':
        countSedanF += 1
    if a=='SUV' and b=='F':
        countSUVF += 1

#This will be used for a test to check if
#a specific "type" exists. The variables will
#then be used in the conditionals below.
countCoupe = 0
countSedan = 0
countSUV = 0

for numType in frame['type']:
    if numType == "coupe":
        countCoupe += 1
    if numType == "sedan":
        countSedan += 1
    if numType == "SUV":
        countSUV += 1
        
#Here are the conditionals for calculating and printing the
#conditional probabilities in order of rating.
#The counts cannot equal zero to avoid division by zero.

if countCoupe and countA != 0:
    calcCA = float(countCoupeA)/float(countA)
    print "Prob(type=coupe|rating=A) = ",format(calcCA, '.6f')   
if countSedan and countA != 0:
    calcSA = float(countSedanA)/float(countA)
    print "Prob(type=sedan|rating=A) = ",format(calcSA, '.6f')
if countSUV and countA != 0:
    calcSUVA = float(countSUVA)/float(countA)
    print "Prob(type=SUV|rating=A) = ",format(calcSUVA, '.6f')
if countCoupe and countB != 0:
    calcCB = float(countCoupeB)/float(countB)
    print "Prob(type=coupe|rating=B) = ",format(calcCB, '.6f')
if countSedan and countB != 0:
    calcSB = float(countSedanB)/float(countB)
    print "Prob(type=sedan|rating=B) = ",format(calcSB, '.6f')
if countSUV and countB != 0:
    calcSUVB = float(countSUVB)/float(countB)
    print "Prob(type=SUV|rating=B) = ",format(calcSUVB, '.6f')
if countCoupe and countC != 0:    
    calcCC = float(countCoupeC)/float(countC)
    print "Prob(type=coupe|rating=C) = ",format(calcCC, '.6f')
if countSedan and countC != 0:    
    calcSC = float(countSedanC)/float(countC)
    print "Prob(type=sedan|rating=C) = ",format(calcSC, '.6f')
if countSUV and countC != 0:
    calcSUVC = float(countSUVC)/float(countC)
    print "Prob(type=SUV|rating=C) = ",format(calcSUVC, '.6f')
if countCoupe and countD != 0:
    calcCD = float(countCoupeD)/float(countD)
    print "Prob(type=coupe|rating=D) = ",format(calcCD, '.6f') 
if countSedan and countD != 0: 
    calcSD = float(countSedanD)/float(countD)
    print "Prob(type=sedan|rating=D) = ",format(calcSD, '.6f')
if countSUV and countD != 0:
    calcSUVD = float(countSUVD)/float(countD)
    print "Prob(type=SUV|rating=D) = ",format(calcSUVD, '.6f')
if countCoupe and countF != 0:
    calcCF = float(countCoupeF)/float(countF)
    print "Prob(type=coupe|rating=F) = ",format(calcCF, '.6f')
if countSedan and countF != 0: 
    calcSF = float(countSedanF)/float(countF)
    print "Prob(type=sedan|rating=F) = ",format(calcSF, '.6f')    
if countSUV and countF != 0:
    calcSUVF = float(countSUVF)/float(countF)
    print "Prob(type=SUV|rating=F) = ",format(calcSUVF, '.6f')   