# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:26:54 2021

@author: espin
"""
#import the require libraries
import pandas as pd 
import time
import glob

#item and invoice data is in \Team-5\data_code\data_code

filenames = glob.glob('*.dat') #create a list with all the .dat filenames

mydf = pd.DataFrame(columns = ['FileName', 'CostumerID', 'InvoiceID', 
                               'Review', 'Stars', 'Mstars'])
#mydf is a blank frame to capture all the data from all the .dat files

t1 = time.time() #initial time stamp

y1 = len("Customer ID: ") #obtain the length of these strings
y2 = len("Invoice ID: ")
y3 = len("Product Rating: ")

#--------------------------------------------------->
for i in range(len(filenames)): #the loop is as long as the number or filenames
    
    print(filenames[i]) #print current filename
    
    # the option below will import all the text as 1 string, better to use 'lines'
    #with open(filenames[i], 'r') as file: #statement to open the file and read the text
    #    text = file.read() #text hold the intire content of the n-th .dat file
    #    print(text)
    #x1 = text.find("Customer ID: ") #find where these strings start
    #x2 = text.find("Invoice ID: ")  #within the .dat file contents
    #x3 = text.find("Product Rating: ")
    
    with open(filenames[i], 'r') as file: #statement to open the file and read the text
        lines = file.readlines() #text hold the intire content of the n-th .dat file
    
    #lenght of each line includes 1 additional charater which is the break \n
    
    # obtain a substring with only the customer, invoice, and rating values
    temp = lines[0]
    customer = temp[y1:len(temp)-1]
    temp = lines[1]
    invoice = temp[y2:len(temp)-1]
    temp = lines[2]
    rating = temp[y3:len(temp)] #the last line doesn't have \n as break
   
    
    stars = int(rating[:rating.find('/')]) #obtain the number of stars as int
    
    #append mydf by adding all the values to a new row
    mydf = mydf.append({'FileName':filenames[i], 'CostumerID':customer,
                    'InvoiceID':invoice, "Review":rating, "Stars":stars,
                    'Mstars':5}, ignore_index=True)
    
    #Reset variables
    del file
    #del x1, x2, x3
    del temp, customer, invoice, rating, stars
    del lines

t2 = time.time()-t1 #final time stamp
print(round(t2/60,2),' min') #print the elapsed time
del t1, t2 #delete time stamps
del y1, y2, y3 #delete temp variables
del i           #delete counter

mydf.to_csv(r'C:\Users\espin\Desktop\Python Local\reboot-project\Team-5\reviews.csv',
            sep=',', header=True, index=False)
#export the data frame to csv

