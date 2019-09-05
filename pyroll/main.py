#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import os

# Objectives:
# Find total months
# Find total Profit/Losses
# Average Change
# Greatest Increase: Date + Value
# Greatest Decrease: Date + Value


# In[2]:


filepath = "C:/Users/Taimoor/RU-SOM-DATA-PT-08-2019-U-C/homework/03-python/Instructions/PyBank/Resources/budget_data.csv"


# In[3]:


dataframe = pd.read_csv(filepath)
df = dataframe.copy()

df.head()
#86 rows by 2 columns

# df.shape


# In[4]:


# Total months and profits

totalmonths = df["Date"].count()
totalprofit = df["Profit/Losses"].sum()

print(totalmonths)
print(totalprofit)


# In[5]:


# Average Change
# Strategy: Question wants the delta between each subsequent value in profits/losses and then the average
# of those deltas

# How to call next index in 'for' loop? Maybe use counter and have list[counter +1]?
# Ans: Use for i in range(int(df[].count()))

# Remember "profits" is a dataframe object not a list object. How to add individual elements into a list using a loop?
# Or maybe use df.iloc[]?



profits = df[["Profit/Losses"]]
deltas = []
# index = 0

# profits.head()


for i in range(int(profits.count())-1): #Range should be to 85 not 86 as as there should be 85 "changes"/deltas
    
    delta = profits.iloc[i+1,0] - profits.iloc[i, 0]
    
    deltas.append(delta)
    
avgchange = sum(deltas) / len(deltas)

float(avgchange)

# Debug Statements
    
# delta = profits.iloc[0,0] - profits.iloc[1, 0]

# print(int(profits.count()))

# print(profits.iloc[0,0])
# print(profits.iloc[1,0])

# print(delta)

# range(int(profits.count()))

# print(len(deltas))

# for i in deltas:
    
#     print(i)
    


# In[6]:


# Looking for greatest/least delta in deltas list
# Need to have corresponding dates with the change
# Using i+1 index as deltas is the difference between two dates with the latter date 
# corresponding to the date the "change" occured

dfdates = df[["Date"]]

maxdate = dfdates.iloc[deltas.index(max(deltas)) + 1, 0]
maxprofit = (max(deltas))

mindate = dfdates.iloc[deltas.index(min(deltas)) + 1, 0]
minprofit = (min(deltas))

print(maxprofit)
print(minprofit)

print(maxdate)
print(mindate)

# dfdates.head()
# dfdates.shape
# maxdate
# mindate


# In[7]:


# Putting it all together

print(f"Total Months: {totalmonths}")
print(f"Total Profit: ${totalprofit}")
print(f"Greatest Change: {str(maxdate)}: ${maxprofit}")
print(f"Least Change: {str(mindate)} ${minprofit}")
print(f"Average Change: ${avgchange}")


# In[8]:


# Storing final results in dataframe object

# Dictionary of Lists for answer
dffinal = pd.Series({"Total Months": [totalmonths],
                     "Total Profits": [totalprofit],
                     "Greatest Increase in Profits" : [maxdate, maxprofit],
                     "Greatest Decrease in Profits": [mindate, minprofit],
                     "Average Change in Profits" : [avgchange]
                       })

dffinal.head()


# In[9]:


# Exporting dfffinal to .csv

dffinal.to_csv("bankroll_report.csv", index = False, header = True)


# In[ ]:




