
import pandas as pd
import numpy as np

#Open/read the csv document.
energy = pd.read_csv('energy.csv')

#Create DataFrame object from it.
frame = pd.DataFrame(energy)

#Remove the data for aggregate values by
#their index.
frame.drop(frame.index[34], inplace=True)
frame.drop(frame.index[34], inplace=True)
frame.drop(frame.index[40], inplace=True)

#Set the appropriate parameter (NaN) when reading
#the file to recognize n/a values as such.
frame.replace('..', np.nan, inplace = True)

#Calculate mean of each row.
means = frame.mean(axis=1)

frame.set_value(7,'1971',means[7])
frame.set_value(27,'1971',means[27])
frame.set_value(36,'2010',means[36])
frame.set_value(37,'2010',means[37])
frame.set_value(38,'2010',means[38])
frame.set_value(39,'2010',means[39])
frame.set_value(40,'1971',means[40])
frame.set_value(40,'2010',means[40])
frame.set_value(41,'2010',means[41])

#Hardcode continent mapping.
continents = {'Australia':'Australia',
'Austria':'Europe',
'Belgium':'Europe',
'Canada':'North America',
'Chile':'South America',
'CzechRepublic':'Europe',
'Denmark':'Europe',
'Estonia':'Europe',
'Finland':'Europe',
'France':'Europe',
'Germany':'Europe',
'Greece':'Europe',
'Hungary':'Europe',
'Iceland':'Europe',
'Ireland':'Europe',
'Israel':'Asia',
'Italy':'Europe',
'Japan':'Asia',
'Korea':'Asia',
'Luxembourg':'Europe',
'Mexico':'North America',
'Netherlands':'Europe',
'NewZealand':'Oceania',
'Norway':'Europe',
'Poland':'Europe',
'Portugal':'Europe',
'SlovakRepublic':'Europe',
'Slovenia':'Europe',
'Spain':'Europe',
'Sweden':'Europe',
'Switzerland':'Europe',
'Turkey':'Asia',
'UnitedKingdom':'Europe',
'UnitedStates':'North America',
'Brazil':'South America',
'China':'Asia',
'India':'Asia',
'Indonesia':'Asia',
'RussianFederation':'Europe',
'SouthAfrica':'Africa'}

#Add new column, 'Continent', and fill
#it in with continent that corresponds to each country.
frame['Continent']= frame['Unnamed: 0'].map(continents)

#Create new dataframe with continent name as the index.
newFrame = pd.DataFrame(columns = ['num_countries', 'mean', 'small', 'avg', 'large' ],
index = ['Europe', 'Asia', 'North America', 'South America', 'Australia', 'Africa', 'Oceania'])

#Column - number of countries for each continent
newFrame['num_countries'] = frame.groupby('Continent').agg(['size'])

#Column - mean energy production of countries in each continent.
newFrame['mean'] = frame.groupby('Continent').agg(['mean'])

'''
#Correct mean values hardcoded in for testing.
newFrame.set_value('Europe','mean',161.572326)
newFrame.set_value('Asia','mean',607.983830)
newFrame.set_value('North America','mean',1560.438095)
newFrame.set_value('South America','mean',199.148901)
newFrame.set_value('Australia','mean',218.021429)
newFrame.set_value('Africa','mean',213.846154)
newFrame.set_value('Oceania','mean',39.378571)
'''
#Calculate the mean of all countries.
meanAllCountries = newFrame['mean'].mean()

#Calculate the standard deviation.
standardDeviation = newFrame['mean'].std()

minus = meanAllCountries - standardDeviation
plus = meanAllCountries + standardDeviation

#Loops to iterate over mean values, compare them to mean of all
#countries and standard deviation, and to designate production size.  

for x in newFrame.index:
    for cellMean in newFrame['mean']:
        if cellMean < (minus):
            newFrame.set_value(x,'small',1)
        else: 
            newFrame.set_value(x,'small',0)
            
for x in newFrame.index:
    for cellMean in newFrame['mean']:
        if cellMean > (minus) and cellMean < (plus):
            newFrame.set_value(x,'avg',1)
        else: 
            newFrame.set_value(x,'avg',0)
            
for x in newFrame.index:
    for cellMean in newFrame['mean']:
        if cellMean > (plus):
            newFrame.set_value(x,'large',1)
        else: 
            newFrame.set_value(x,'large',0)

print newFrame

  