
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Open/read the csv document.
pums = pd.read_csv('ss13hil.csv')

#Create DataFrame object from it.
frame = pd.DataFrame(pums)

#########################################################
#These are to count the occurence of each language.
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

#Iterate through language column, count
#occurence of each language and store in
#respective variables.
for lang in frame['HHL']:
    if lang == 1.0:
        count1 += 1
        english = count1
    if lang == 2.0:
        count2 += 1
        spanish = count2
    if lang == 3.0:
        count3 += 1
        indo = count3
    if lang == 4.0:
        count4 += 1
        asian = count4
    if lang == 5.0:
        count5 += 1
        other = count5

#List languages, colors, and labels for plotting
languages = [english, spanish, indo, asian, other]
colors = ['b', 'g', 'r', 'c', 'tab:purple']
labels = ['English only', 'Spanish', 'Other Indo_European',
'Asian and Pacific Island Languages', 'Other']

#Create a figure with 2x2 subplots.
#Change background color from grey to white.
fig = plt.figure(facecolor='white')

#This is to utilize older version of matplotlib to match
#assignment output.
plt.style.use('classic')

#Plot in upper left
ax1 = fig.add_subplot(2,2,1)
plt.pie(languages, colors = colors, counterclock = True,
shadow = False, startangle = 243)
plt.legend(labels, loc="upper left", fontsize = 'xx-small')
plt.axis('equal')
plt.title('Household Languages', fontsize = 'x-small')
plt.tight_layout()
#########################################################
#Plot in upper right
ax2 = fig.add_subplot(2,2,2)

#Set x-axis to log
plt.gca().set_xscale("log")

#Use logspace for scale in x-axis
bins = np.logspace(1, 7, 100,  endpoint=True, base=10.0, dtype=None)

#Plot histogram
frame['HINCP'].plot.hist(bins = bins, color = 'mediumseagreen', normed = True, fontsize = 'x-small')

#Plot KDE line
frame['HINCP'].plot.kde(color = 'black', style = '--')

#Set the grid
plt.grid(color='black', linestyle='dotted', linewidth=.5)
plt.style.use('classic')

#Label histogram and show
ax2.set_xlabel('Household income ($) - Log Scaled', fontsize = 'x-small')
plt.title('Distribution of Household Income', fontsize = 'x-small')
plt.show()
#########################################################
# Plot in lower left
ax3 = fig.add_subplot(2,2,3)

# Get WGTP values to count how many househoulds are represented by each record for VEH
# Group together and take the sum then divide by 1000
car_house_val = frame.groupby('VEH')['WGTP']
car_house_map = car_house_val.sum()/(1000)

# map data to bar graph by index vs value
ax3.bar(car_house_map.index,car_house_map.values, width=0.85,color='r',align='center')

#Set title
ax3.set_title('Vehicles Availible in Households', fontsize='x-small')

#Set ylabel
ax3.set_ylabel('Thousands of Households',fontsize='x-small')

#Set xlabel
ax3.set_xlabel('# of Vehicles', fontsize=0.4)
ax3.xaxis.label.set_size(7)
#For some reason it wont let me go smaller
#Set xaxis
ax3.set_xticks(car_house_map.index)
#########################################################
ax4 = fig.add_subplot(2,2,4)

property_taxes = frame['TAXP']
property_taxes = property_taxes.reindex()
property_taxes = property_taxes.dropna()
# convert TAXP into the appropriate numeric value, using the lower bound of the range.
for i in range(int(property_taxes.size)):
    if property_taxes.iloc[i] == 1:
        property_taxes.iloc[i] = 0
    elif property_taxes.iloc[i] == 2:
        property_taxes.iloc[i] = 1
    elif 2<=property_taxes.iloc[i]<=22:
        property_taxes.iloc[i] = property_taxes.iloc[i] - 2
        property_taxes.iloc[i] = property_taxes.iloc[i] * 50
    elif 23<=property_taxes.iloc[i]<=62:
        property_taxes.iloc[i] = property_taxes.iloc[i] - 2
        property_taxes.iloc[i] = (property_taxes.iloc[i] * 100) - 1000
    elif 63<=property_taxes.iloc[i]<=64:
        property_taxes.iloc[i] = property_taxes.iloc[i] - 2
        property_taxes.iloc[i] = (property_taxes.iloc[i] * 500) - 2500
    elif 65<=property_taxes.iloc[i]<=68:
        property_taxes.iloc[i] = property_taxes.iloc[i] - 2
        property_taxes.iloc[i] = (property_taxes.iloc[i] * 1000) - 56000
property_values = frame['VALP']
# use the weight for the size of the points.
weight = frame['WGTP']
# use firtst payment for the color of the points
first_payment = frame['MRGP']
df2 = pd.concat([property_values, property_taxes, weight,first_payment], axis=1)
df2 = df2.dropna()
ax4.set_xlim([0,1200000])
ax4.set_ylim([0,10000])
# We need to save teh sublot to pass it to the colorbar function later on.
im = ax4.scatter(df2['VALP'], df2['TAXP'],c = df2['MRGP'], linewidths = 0, s = df2['WGTP'], alpha = 0.2, cmap='bwr')
ax3.set_ylabel('Thousands of Households',fontsize='x-small')
fig.colorbar(im,ax=ax4)
# set color limits
im.set_clim(df2['MRGP'].min(), df2['MRGP'].max())
# Label and limit the axies
ax4.set_title('Property taxes vs. Property Values', fontsize='x-small')
ax4.set_ylabel('Taxes ($)',fontsize='x-small')
ax4.set_xlabel('Property Value ($)',fontsize='x-small')