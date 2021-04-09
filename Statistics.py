# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 09:47:59 2021

@author: espin
"""
import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt #plotting library
#correlation between categories
#two-tail p-value testing for the null hyphotesis (both averages are equal)
#test to see if there is a difference in the rating values
#TEsting to see if ratings change based on soda flavor
#if p-value lower than our alpha thershold then ratings are differnt
#p-value of 5% (0.05) = 95% confidence 

#--> get only cream soda
df_cs = reviews_all[reviews_all['Category'] == 'Cream Soda']
df_cs.info() #check info
print(df_cs['Category'].unique()) #check that we only have cream soda
df_cs = df_cs.reset_index(drop=True) #reset index

#--> get only root beer
df_rb = reviews_all[reviews_all['Category'] == 'Root Beer']
df_rb = df_rb.reset_index(drop=True)
#run statistics

stats.ttest_ind(df_cs['RateNum'],df_rb['RateNum'], equal_var=False)

#obtain all unique names

unique_names = reviews_all.Category.unique().tolist()

#>------------------------
#plotting as histogram

#reviews_all.boxplot(column = 'Category', by = unique_names)

d = {} #dictate?
for name in unique_names:
    df = pd.DataFrame()
    text1 = '_' + name #finde the current name
    text2 = text1.replace(" ", "_") #remove blank spaces
    df = reviews_all[reviews_all['Category'] == name]
    d[text2] = pd.DataFrame(df) #creates an arrays with all the data frames 
    print(text2)

#shapiro-test for all categories 
for name in unique_names:
    df = pd.DataFrame()
    df = reviews_all[reviews_all['Category'] == name]
    shapiro_test = stats.shapiro(df['RateNum'])
    print(name)
    print(len(df['RateNum']))
    print(shapiro_test)

#one way Anova with all categories 
stats.f_oneway(reviews_all['RateNum'][reviews_all['Category'] == 'Cola'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Lime Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Ginger Ale'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cherry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cream Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Energy Drink'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Raspberry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Fruit Punch'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Grapefruit Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Blueberry Soda'],
               )


#-------------------------------------->ANOVA via StatsModel
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('RateNum ~ C(Category)', data=reviews_all).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

#running shapiro test and q-q plot
stats.shapiro(model.resid)

fig = plt.figure(figsize= (20, 20))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(model.resid, plot= plt, rvalue= True)
ax.set_title("Probability plot of model residual's", fontsize= 30)
ax.set

plt.show()

#levene test for equal variance
stats.levene(reviews_all['RateNum'][reviews_all['Category'] == 'Cola'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Lime Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Ginger Ale'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cherry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cream Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Energy Drink'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Raspberry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Fruit Punch'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Grapefruit Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Blueberry Soda'],
               )

#------------> Running boxplot
fig = plt.figure(figsize= (20, 20))
ax = fig.add_subplot(111)

ax.set_title("Box Plot of Rating by Category", fontsize= 20)
ax.set

data = [reviews_all['RateNum'][reviews_all['Category'] == 'Cola'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Lime Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Ginger Ale'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cherry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cream Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Energy Drink'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Raspberry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Fruit Punch'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Grapefruit Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Blueberry Soda'],
               ]
help(ax.boxplot)
ax.boxplot(data, showmeans = True)
           #labels= unique_names,
           #showmeans= True)

plt.xlabel("Flavor")
plt.ylabel("Rating")

plt.show()

#----------------------->Perform non-parametric test Kruskal-Wallis
#since data is not normal, perform a non-parametric test to compare means
stats.kruskal(reviews_all['RateNum'][reviews_all['Category'] == 'Cola'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Lime Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Ginger Ale'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cherry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Cream Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Energy Drink'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Root Beer'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Orange Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Raspberry Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Fruit Punch'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Grapefruit Soda'],
               reviews_all['RateNum'][reviews_all['Category'] == 'Blueberry Soda'],
               )