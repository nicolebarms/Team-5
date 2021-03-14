# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:21:59 2021

@author: espin
"""
# Import Pandas
import pandas as pd 

#import all the csv's
invoices = pd.read_csv('invoice.csv')
items = pd.read_csv('item.csv')
reviews = pd.read_csv('reviews.csv')

#create an empty list and populate it with the review number as float
RateNum = list()
for i in range(len(reviews['FileName'])):
    temp = float(reviews.iloc[i,4]/5)
    RateNum.append(temp)    
del temp, i

#add the numerical value of the rating to a new column in reviews.df
reviews['RateNum'] = RateNum


#joining item info into invoice dataframe
invoices_all = pd.merge(invoices, items, how="left", on=['Item_id'])

#joining invoice info into review dataframe
reviews_all = pd.merge(reviews, invoices_all, how="left", 
                       left_on = 'InvoiceID', right_on = 'Invoice_id')

#some work code to check types and column labels
reviews.columns
invoices.columns
type(reviews.loc[1,'InvoiceID'])
type(invoices.loc[1,'Invoice_id'])

#--> get only cream soda
df_cs = reviews_all[reviews_all['Category'] == 'Cream Soda']
df_cs.info() #check info
print(df_cs['Category'].unique()) #check that we only have cream soda

#--> get only root beer
df_rb = reviews_all[reviews_all['Category'] == 'Root Beer']

#run statistics

from scipy import stats
#correlation between categories
stats.ttest_ind(df_cs['RateNum'],df_rb['RateNum'], equal_var=False)

