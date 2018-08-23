# Initialize sample mean and variance.
sampleMean = 0
sampleVariance = 0
# Initalize counter - this increments "n".
counter = 0

# Ask user for inputs
userInputs = int(raw_input("Enter a number: "))

# While loop - continues until user inputs negative integer
while userInputs >= 0:
    #Begin to increment counter
    counter = counter + 1
    #Keep previous mean to be used in sampleVariance calculation.
    prevMean = sampleMean 
    #Calculation for the sample mean
    sampleMean = float(sampleMean) + ((float(userInputs) - float(sampleMean)) / counter)
    if (counter > 1):#If statement to avoid division by zero
        #Calculation for the sample variance
        sampleVariance = ((float(counter-2) / float(counter-1)) * float(sampleVariance)) + (((float(userInputs) - float(prevMean)) ** 2) / counter)
    #Condition to exactly match the output of the sample program given in the assignment (variance == 0, not 0.0)
    if (sampleVariance == 0):
        print "Mean is ", float(sampleMean), " variance is ", int(sampleVariance)
        print ""
    else:
        print "Mean is ", float(sampleMean), " variance is ", float(sampleVariance)
        print ""
    #Ask user for all other inputs within while loop
    userInputs = int(raw_input("Enter a number: "))
 
	