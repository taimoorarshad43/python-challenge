#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Objectives:
# Total Number of Votes (df.count())
# Complete list of candidates (probably need a dictionary)
# Total votes for each candidate
# Total percent of votes for each candidate
# Winner of the election


# In[4]:


filepath = "Resources/election_data.csv"

dforig = pd.read_csv(filepath)

dfcopy = dforig.copy()

dfcopy.head()


# In[3]:


dfcopy.shape


# In[4]:


# Total Votes

dfvoterid = dfcopy[["Voter ID"]]

dfvoterid.head()
dfvoterid.count()

votercount = dfvoterid.count()

votercount # Cast to int later


# In[5]:


# Making dictionary of candidates
# Takes forever to run through - ways to optimize?

candidates = {}

dfcand = dfcopy[["Candidate"]]


for i in range(int(dfcand.count())):
    
    item = dfcand.iloc[i, 0]
    
    if item not in candidates:
        
        candidates[item] = 1
        
    else:
        
        candidates[item] += 1
        


# Debug Statements

# range(int(dfcand.count()))

# dfcand.iloc[0,0]

# dfcand.shape


# In[6]:



for i in candidates:
    print(f"{i}: {int(candidates[i])}")


# In[7]:


# Percent votes
# Strat: candidates[i]/(int(dfcopy.count()))

percents = []

# for i in range(len(candidates)):
#     percent = candidates[i]/(int(dfcopy.count()))
#     percents.append(percent)
    
# total = int(dfcand)

for i in candidates:
    percent = candidates[i]/(int(dfcand.count()))
    percents.append(percent*100)
    
print(percents)


# In[8]:


# Finding the winner (aka max function)

maxcount = 0
maxkey = None
indexcount = 0

for i in candidates:
    
    if candidates[i] > maxcount:
        maxcount = candidates[i]
        maxkey = i
    else:
        continue
        
winner = maxkey

winner


# In[9]:


# Putting it all together

count = 0

print("Election Results")
print(f"--------------------------")
print()
print(f"Total Votes: {int(votercount)}")
print()
for i in candidates:
    print(f"{i}: ({percents[count]}%) ({candidates[i]})")
    count += 1
print()
print(f"--------------------------")
print()
print(f"Winner: {winner}")


# In[10]:


# Making dataframe to save externally
# May need to make a list of candidates instead of a dictionary

lcand = []
candvotes = []

for i in candidates:
    lcand.append(i)
    candvotes.append(candidates[i])

dffinal = pd.DataFrame({"Candidates" : lcand, "Number Votes": candvotes , "Percents" : percents, "Winner" : winner})

dffinal.head()

# print(lcand)
# print(candvotes)
# print(percents)


# In[11]:


dffinal.to_csv("Election_Results.csv")


# In[ ]:




