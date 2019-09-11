{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import csv\n",
    "import os\n",
    "\n",
    "# Objectives:\n",
    "# Find total months\n",
    "# Find total Profit/Losses\n",
    "# Average Change\n",
    "# Greatest Increase: Date + Value\n",
    "# Greatest Decrease: Date + Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "filepath = \"Resources/budget_data.csv\"\n"
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
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses\n",
       "0  Jan-2010         867884\n",
       "1  Feb-2010         984655\n",
       "2  Mar-2010         322013\n",
       "3  Apr-2010         -69417\n",
       "4  May-2010         310503"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataframe = pd.read_csv(filepath)\n",
    "df = dataframe.copy()\n",
    "\n",
    "df.head()\n",
    "#86 rows by 2 columns\n",
    "\n",
    "# df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86\n",
      "38382578\n"
     ]
    }
   ],
   "source": [
    "# Total months and profits\n",
    "\n",
    "totalmonths = df[\"Date\"].count()\n",
    "totalprofit = df[\"Profit/Losses\"].sum()\n",
    "\n",
    "print(totalmonths)\n",
    "print(totalprofit)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2315.1176470588234"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Average Change\n",
    "# Strategy: Question wants the delta between each subsequent value in profits/losses and then the average\n",
    "# of those deltas\n",
    "\n",
    "# How to call next index in 'for' loop? Maybe use counter and have list[counter +1]?\n",
    "# Ans: Use for i in range(int(df[].count()))\n",
    "\n",
    "# Remember \"profits\" is a dataframe object not a list object. How to add individual elements into a list using a loop?\n",
    "# Or maybe use df.iloc[]?\n",
    "\n",
    "\n",
    "\n",
    "profits = df[[\"Profit/Losses\"]]\n",
    "deltas = []\n",
    "# index = 0\n",
    "\n",
    "# profits.head()\n",
    "\n",
    "\n",
    "for i in range(int(profits.count())-1): #Range should be to 85 not 86 as as there should be 85 \"changes\"/deltas\n",
    "    \n",
    "    delta = profits.iloc[i+1,0] - profits.iloc[i, 0]\n",
    "    \n",
    "    deltas.append(delta)\n",
    "    \n",
    "avgchange = sum(deltas) / len(deltas)\n",
    "\n",
    "float(avgchange)\n",
    "\n",
    "# Debug Statements\n",
    "    \n",
    "# delta = profits.iloc[0,0] - profits.iloc[1, 0]\n",
    "\n",
    "# print(int(profits.count()))\n",
    "\n",
    "# print(profits.iloc[0,0])\n",
    "# print(profits.iloc[1,0])\n",
    "\n",
    "# print(delta)\n",
    "\n",
    "# range(int(profits.count()))\n",
    "\n",
    "# print(len(deltas))\n",
    "\n",
    "# for i in deltas:\n",
    "    \n",
    "#     print(i)\n",
    "    \n"
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
      "1926159\n",
      "-2196167\n",
      "Feb-2012\n",
      "Sep-2013\n"
     ]
    }
   ],
   "source": [
    "# Looking for greatest/least delta in deltas list\n",
    "# Need to have corresponding dates with the change\n",
    "# Using i+1 index as deltas is the difference between two dates with the latter date \n",
    "# corresponding to the date the \"change\" occured\n",
    "\n",
    "dfdates = df[[\"Date\"]]\n",
    "\n",
    "maxdate = dfdates.iloc[deltas.index(max(deltas)) + 1, 0]\n",
    "maxprofit = (max(deltas))\n",
    "\n",
    "mindate = dfdates.iloc[deltas.index(min(deltas)) + 1, 0]\n",
    "minprofit = (min(deltas))\n",
    "\n",
    "print(maxprofit)\n",
    "print(minprofit)\n",
    "\n",
    "print(maxdate)\n",
    "print(mindate)\n",
    "\n",
    "# dfdates.head()\n",
    "# dfdates.shape\n",
    "# maxdate\n",
    "# mindate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Months: 86\n",
      "Total Profit: $38382578\n",
      "Greatest Change: Feb-2012: $1926159\n",
      "Least Change: Sep-2013 $-2196167\n",
      "Average Change: $-2315.1176470588234\n"
     ]
    }
   ],
   "source": [
    "# Putting it all together\n",
    "\n",
    "print(f\"Total Months: {totalmonths}\")\n",
    "print(f\"Total Profit: ${totalprofit}\")\n",
    "print(f\"Greatest Change: {str(maxdate)}: ${maxprofit}\")\n",
    "print(f\"Least Change: {str(mindate)} ${minprofit}\")\n",
    "print(f\"Average Change: ${avgchange}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Total Months                                     [86]\n",
       "Total Profits                              [38382578]\n",
       "Greatest Increase in Profits      [Feb-2012, 1926159]\n",
       "Greatest Decrease in Profits     [Sep-2013, -2196167]\n",
       "Average Change in Profits       [-2315.1176470588234]\n",
       "dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Storing final results in dataframe object\n",
    "\n",
    "# Dictionary of Lists for answer\n",
    "dffinal = pd.Series({\"Total Months\": [totalmonths],\n",
    "                     \"Total Profits\": [totalprofit],\n",
    "                     \"Greatest Increase in Profits\" : [maxdate, maxprofit],\n",
    "                     \"Greatest Decrease in Profits\": [mindate, minprofit],\n",
    "                     \"Average Change in Profits\" : [avgchange]\n",
    "                       })\n",
    "\n",
    "dffinal.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exporting dfffinal to .csv\n",
    "\n",
    "dffinal.to_csv(\"bankroll_report.csv\", index = False, header = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
