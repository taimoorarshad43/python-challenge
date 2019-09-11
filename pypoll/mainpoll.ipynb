{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Objectives:\n",
    "# Total Number of Votes (df.count())\n",
    "# Complete list of candidates (probably need a dictionary)\n",
    "# Total votes for each candidate\n",
    "# Total percent of votes for each candidate\n",
    "# Winner of the election\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Voter ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12864552</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>17444633</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Correy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>19330107</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>19865775</td>\n",
       "      <td>Queen</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11927875</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Voter ID County Candidate\n",
       "0  12864552  Marsh      Khan\n",
       "1  17444633  Marsh    Correy\n",
       "2  19330107  Marsh      Khan\n",
       "3  19865775  Queen      Khan\n",
       "4  11927875  Marsh      Khan"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filepath = \"Resources/election_data.csv\"\n",
    "\n",
    "dforig = pd.read_csv(filepath)\n",
    "\n",
    "dfcopy = dforig.copy()\n",
    "\n",
    "dfcopy.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3521001, 3)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dfcopy.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Voter ID    3521001\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Total Votes\n",
    "\n",
    "dfvoterid = dfcopy[[\"Voter ID\"]]\n",
    "\n",
    "dfvoterid.head()\n",
    "dfvoterid.count()\n",
    "\n",
    "votercount = dfvoterid.count()\n",
    "\n",
    "votercount # Cast to int later"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Making dictionary of candidates\n",
    "# Takes forever to run through - ways to optimize?\n",
    "\n",
    "candidates = {}\n",
    "\n",
    "dfcand = dfcopy[[\"Candidate\"]]\n",
    "\n",
    "\n",
    "for i in range(int(dfcand.count())):\n",
    "    \n",
    "    item = dfcand.iloc[i, 0]\n",
    "    \n",
    "    if item not in candidates:\n",
    "        \n",
    "        candidates[item] = 1\n",
    "        \n",
    "    else:\n",
    "        \n",
    "        candidates[item] += 1\n",
    "        \n",
    "\n",
    "\n",
    "# Debug Statements\n",
    "\n",
    "# range(int(dfcand.count()))\n",
    "\n",
    "# dfcand.iloc[0,0]\n",
    "\n",
    "# dfcand.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan: 2218231\n",
      "Correy: 704200\n",
      "Li: 492940\n",
      "O'Tooley: 105630\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for i in candidates:\n",
    "    print(f\"{i}: {int(candidates[i])}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[63.00001050837531, 19.999994319797125, 13.999996023857989, 2.999999147969569]\n"
     ]
    }
   ],
   "source": [
    "# Percent votes\n",
    "# Strat: candidates[i]/(int(dfcopy.count()))\n",
    "\n",
    "percents = []\n",
    "\n",
    "# for i in range(len(candidates)):\n",
    "#     percent = candidates[i]/(int(dfcopy.count()))\n",
    "#     percents.append(percent)\n",
    "    \n",
    "# total = int(dfcand)\n",
    "\n",
    "for i in candidates:\n",
    "    percent = candidates[i]/(int(dfcand.count()))\n",
    "    percents.append(percent*100)\n",
    "    \n",
    "print(percents)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Khan'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Finding the winner (aka max function)\n",
    "\n",
    "maxcount = 0\n",
    "maxkey = None\n",
    "indexcount = 0\n",
    "\n",
    "for i in candidates:\n",
    "    \n",
    "    if candidates[i] > maxcount:\n",
    "        maxcount = candidates[i]\n",
    "        maxkey = i\n",
    "    else:\n",
    "        continue\n",
    "        \n",
    "winner = maxkey\n",
    "\n",
    "winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "--------------------------\n",
      "\n",
      "Total Votes: 3521001\n",
      "\n",
      "Khan: (63.00001050837531%) (2218231)\n",
      "Correy: (19.999994319797125%) (704200)\n",
      "Li: (13.999996023857989%) (492940)\n",
      "O'Tooley: (2.999999147969569%) (105630)\n",
      "\n",
      "--------------------------\n",
      "\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "# Putting it all together\n",
    "\n",
    "count = 0\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(f\"--------------------------\")\n",
    "print()\n",
    "print(f\"Total Votes: {int(votercount)}\")\n",
    "print()\n",
    "for i in candidates:\n",
    "    print(f\"{i}: ({percents[count]}%) ({candidates[i]})\")\n",
    "    count += 1\n",
    "print()\n",
    "print(f\"--------------------------\")\n",
    "print()\n",
    "print(f\"Winner: {winner}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Candidates</th>\n",
       "      <th>Number Votes</th>\n",
       "      <th>Percents</th>\n",
       "      <th>Winner</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Khan</td>\n",
       "      <td>2218231</td>\n",
       "      <td>63.000011</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Correy</td>\n",
       "      <td>704200</td>\n",
       "      <td>19.999994</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Li</td>\n",
       "      <td>492940</td>\n",
       "      <td>13.999996</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>O'Tooley</td>\n",
       "      <td>105630</td>\n",
       "      <td>2.999999</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Candidates  Number Votes   Percents Winner\n",
       "0       Khan       2218231  63.000011   Khan\n",
       "1     Correy        704200  19.999994   Khan\n",
       "2         Li        492940  13.999996   Khan\n",
       "3   O'Tooley        105630   2.999999   Khan"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Making dataframe to save externally\n",
    "# May need to make a list of candidates instead of a dictionary\n",
    "\n",
    "lcand = []\n",
    "candvotes = []\n",
    "\n",
    "for i in candidates:\n",
    "    lcand.append(i)\n",
    "    candvotes.append(candidates[i])\n",
    "\n",
    "dffinal = pd.DataFrame({\"Candidates\" : lcand, \"Number Votes\": candvotes , \"Percents\" : percents, \"Winner\" : winner})\n",
    "\n",
    "dffinal.head()\n",
    "\n",
    "# print(lcand)\n",
    "# print(candvotes)\n",
    "# print(percents)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "dffinal.to_csv(\"Election_Results.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
