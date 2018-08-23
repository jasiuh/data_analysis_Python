import pandas as pd
import numpy as np

#Open/read the csv document.
pums = pd.read_csv('ss13hil.csv')

#Create DataFrame object from it.
df = pd.DataFrame(pums)

#Given for setting display parameters.
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#This one is additional - It widens columns to show full text in indices.
pd.set_option('max_colwidth',1000)

#######################################################################
#Print the header for the table.
print '*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***'

#Calculations for the columns.
mean=df.groupby('HHT')['HINCP'].mean()
std=df.groupby('HHT')['HINCP'].std()
count=df.groupby('HHT')['HINCP'].count()
#Min and max calculations are converted to int's with astype(int)
minimum=df.groupby('HHT')['HINCP'].min().astype(int)
maximum=df.groupby('HHT')['HINCP'].max().astype(int)

#Store these and concatenate along columns.     
calcs=[mean,std,count,minimum,maximum]
tableOne = pd.concat(calcs,axis=1)

#Create the columns by implementing grouping by index levels.
tableOne.columns = pd.MultiIndex.from_arrays([['mean','std','count','min','max'],
['','','','','']], names = ['','HHT - Household/family type'])

#Sort the table based on mean.
tableOne=tableOne.sort_values(['mean'],ascending=False)

#Generate the rest of the index grouped by HHT.
tableOne.index = [
'Married Couple Household',
'Nonfamily household:Male householder:Not living alone',
'Nonfamily household:Female householder:Not living alone',
'Other family household:Male householder, no wife present',
'Other family household:Female householder, no husband present',
'Nonfamily household:Male householder:Living alone',
'Nonfamily household:Female householder:Living alone']

print tableOne    
#######################################################################
print '*** Table 2 - HHL vs. ACCESS - Frequency Table ***'
tableTwo = pd.DataFrame(data=None, index=['English only', 'Spanish',
                                          'Other Indo-European languages',
                                          'Asian and Pacific Island Languages',
                                          'Other language'] ,
                                          columns=['Yes w/ Subsrc.', 
                                                   'Yes, wo/ Subsrc.',
                                                   'No',
                                                   'All'])
tableTwo.index.name = 'HHL - Household languages'
tableTwo = tableTwo.rename_axis("ACCESS", axis="columns")
                                                   
# Have to remove the rows not included by HHL and ACCESS resriction.
wgtp = df[np.isfinite(df['ACCESS'])]
wgtp = wgtp[np.isfinite(wgtp['HHL'])]
wgtp = float(wgtp['WGTP'].sum())

# English only - yes w/ Subsrc
Aone_Hone = df.loc[(df['ACCESS'] == 1) & (df['HHL'] == 1)]['WGTP']
Aone_Hone = float(Aone_Hone.sum())
total = Aone_Hone
Aone_Hone = Aone_Hone/ wgtp
# - yes wo/ Subsrc
Atwo_Hone = float(df.loc[(df['ACCESS'] == 2) & (df['HHL'] == 1)]['WGTP'].sum())
total = total + Atwo_Hone
Atwo_Hone = Atwo_Hone/ wgtp
# - no
Athree_Hone = float(df.loc[(df['ACCESS'] == 3) & (df['HHL'] == 1)]['WGTP'].sum())
total = total + Athree_Hone
Athree_Hone = Athree_Hone/ wgtp
# - all
total = total/wgtp
# Add to the table
tableTwo.loc['English only'] = pd.Series({'Yes w/ Subsrc.':"{0:.2f}%".format(Aone_Hone * 100), 
                                            'Yes, wo/ Subsrc.':"{0:.2f}%".format(Atwo_Hone * 100),
                                            'No':"{0:.2f}%".format(Athree_Hone * 100),
                                             'All':"{0:.2f}%".format(total * 100)})
total = 0

# Spanish - yes w/
Aone_Htwo = df.loc[(df['ACCESS'] == 1) & (df['HHL'] == 2)]['WGTP']
Aone_Htwo = float(Aone_Htwo.sum())
total = Aone_Htwo
Aone_Htwo = Aone_Htwo/ wgtp
# - yes wo/
Atwo_Htwo = float(df.loc[(df['ACCESS'] == 2) & (df['HHL'] == 2)]['WGTP'].sum())
total = total + Atwo_Htwo
Atwo_Htwo = Atwo_Htwo/ wgtp
# - no
Athree_Htwo = float(df.loc[(df['ACCESS'] == 3) & (df['HHL'] == 2)]['WGTP'].sum())
total = total + Athree_Htwo
Athree_Htwo = Athree_Htwo/ wgtp
# - all
total = total/wgtp
# Add to the table
tableTwo.loc['Spanish'] = pd.Series({'Yes w/ Subsrc.':"{0:.2f}%".format(Aone_Htwo * 100), 
                                            'Yes, wo/ Subsrc.':"{0:.2f}%".format(Atwo_Htwo * 100),
                                            'No':"{0:.2f}%".format(Athree_Htwo * 100),
                                             'All':"{0:.2f}%".format(total * 100)})
total = 0

# Other Indo-European languages - yes w/
Aone_Hthree = df.loc[(df['ACCESS'] == 1) & (df['HHL'] == 3)]['WGTP']
Aone_Hthree = float(Aone_Hthree.sum())
total = Aone_Hthree
Aone_Hthree = Aone_Hthree/ wgtp
# - yes wo/
Atwo_Hthree = float(df.loc[(df['ACCESS'] == 2) & (df['HHL'] == 3)]['WGTP'].sum())
total = total + Atwo_Hthree
Atwo_Hthree = Atwo_Hthree/ wgtp
# - no
Athree_Hthree = float(df.loc[(df['ACCESS'] == 3) & (df['HHL'] == 3)]['WGTP'].sum())
total = total + Athree_Hthree
Athree_Hthree = Athree_Hthree/ wgtp
# - all
total = total/wgtp
# Add to the table
tableTwo.loc['Other Indo-European languages'] = pd.Series({'Yes w/ Subsrc.':"{0:.2f}%".format(Aone_Hthree * 100), 
                                            'Yes, wo/ Subsrc.':"{0:.2f}%".format(Atwo_Hthree * 100),
                                            'No':"{0:.2f}%".format(Athree_Hthree * 100),
                                             'All':"{0:.2f}%".format(total * 100)})
total = 0

# Asian and Pacific Island Languages
Aone_Hthree = df.loc[(df['ACCESS'] == 1) & (df['HHL'] == 4)]['WGTP']
Aone_Hthree = float(Aone_Hthree.sum())
total = Aone_Hthree
Aone_Hthree = Aone_Hthree/ wgtp
# - yes wo/
Atwo_Hthree = float(df.loc[(df['ACCESS'] == 2) & (df['HHL'] == 4)]['WGTP'].sum())
total = total + Atwo_Hthree
Atwo_Hthree = Atwo_Hthree/ wgtp
# - no
Athree_Hthree = float(df.loc[(df['ACCESS'] == 3) & (df['HHL'] == 4)]['WGTP'].sum())
total = total + Athree_Hthree
Athree_Hthree = Athree_Hthree/ wgtp
# - all
total = total/wgtp
# Add to the table
tableTwo.loc['Asian and Pacific Island Languages'] = pd.Series({'Yes w/ Subsrc.':"{0:.2f}%".format(Aone_Hthree * 100), 
                                            'Yes, wo/ Subsrc.':"{0:.2f}%".format(Atwo_Hthree * 100),
                                            'No':"{0:.2f}%".format(Athree_Hthree * 100),
                                             'All':"{0:.2f}%".format(total * 100)})
total = 0

# Other language
Aone_Hthree = df.loc[(df['ACCESS'] == 1) & (df['HHL'] == 5)]['WGTP']
Aone_Hthree = float(Aone_Hthree.sum())
total = Aone_Hthree
Aone_Hthree = Aone_Hthree/ wgtp
# - yes wo/
Atwo_Hthree = float(df.loc[(df['ACCESS'] == 2) & (df['HHL'] == 5)]['WGTP'].sum())
total = total + Atwo_Hthree
Atwo_Hthree = Atwo_Hthree/ wgtp
# - no
Athree_Hthree = float(df.loc[(df['ACCESS'] == 3) & (df['HHL'] == 5)]['WGTP'].sum())
total = total + Athree_Hthree
Athree_Hthree = Athree_Hthree/ wgtp
# - all
total = total/wgtp
# Add to the table
tableTwo.loc['Other language'] = pd.Series({'Yes w/ Subsrc.':"{0:.2f}%".format(Aone_Hthree * 100), 
                                            'Yes, wo/ Subsrc.':"{0:.2f}%".format(Atwo_Hthree * 100),
                                            'No':"{0:.2f}%".format(Athree_Hthree * 100),
                                             'All':"{0:.2f}%".format(total * 100)})
total = 0

# All
Aone_Hthree = df.loc[(df['ACCESS'] == 1) & ((df['HHL'] == 1) | (df['HHL'] == 2) | (df['HHL'] == 3) | (df['HHL'] == 4) | (df['HHL'] == 5))]['WGTP']
Aone_Hthree = float(Aone_Hthree.sum())
total = Aone_Hthree
Aone_Hthree = Aone_Hthree/ wgtp
# - yes wo/
Atwo_Hthree = float(df.loc[(df['ACCESS'] == 2) & ((df['HHL'] == 1) | (df['HHL'] == 2) | (df['HHL'] == 3) | (df['HHL'] == 4) | (df['HHL'] == 5))]['WGTP'].sum())
total = total + Atwo_Hthree
Atwo_Hthree = Atwo_Hthree/ wgtp
# - no
Athree_Hthree = float(df.loc[(df['ACCESS'] == 3) & ((df['HHL'] == 1) | (df['HHL'] == 2) | (df['HHL'] == 3) | (df['HHL'] == 4) | (df['HHL'] == 5))]['WGTP'].sum())
total = total + Athree_Hthree
Athree_Hthree = Athree_Hthree/ wgtp
# - all
total = total/wgtp
# Add to the table
tableTwo.loc['All'] = pd.Series({'Yes w/ Subsrc.':"{0:.2f}%".format(Aone_Hthree * 100), 
                                            'Yes, wo/ Subsrc.':"{0:.2f}%".format(Atwo_Hthree * 100),
                                            'No':"{0:.2f}%".format(Athree_Hthree * 100),
                                             'All':"{0:.2f}%".format(total * 100)})                                          
                                             
print '                                              sum'
print '                                             WGTP'
print tableTwo
#######################################################################
# Quantile Analysis of HINCP - Household income
'''
- Rows Should correspond to different quantiles of HINCP: low(0-1/3), medium, high
'''
# Print Table 3 Title
print ''
print '*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***'


# Grab HINCP data
hincp_data = df['HINCP']

#Create group and index
labels = ['low','medium','high']
hincp_data_group = pd.qcut(hincp_data, 3, labels=labels)
hincp_data_grouped = hincp_data.groupby(hincp_data_group)

# WGPT : Household weight for generating statistics on housing units and housholds 
# (such as average household income).  -PUMS README

hincp_data_grouped_weight = df.WGTP.groupby(hincp_data_group)

# get needed values for quantile analysis
def calc_stats(data):
    return {'min': data.min(),'max':data.max(),
    'mean':data.mean(), 'std':data.std(),'count':data.count()}

# apply calcstats function for the quantile dataframe
q_df = hincp_data_grouped.apply(calc_stats).unstack()
# filter column data
q_df = q_df[['min','max','mean']]
# add weighted counts column data
q_df.loc[:,'household_count'] = hincp_data_grouped_weight.sum()

print q_df