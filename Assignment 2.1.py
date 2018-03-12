# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:55:07 2018

@author: zabiulla.khan

Problem Statement 1:
Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()

Problem Statement 2:
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

"""
#### Problem solution 1: ####
# define sample lists to check the output
list1 = [47,11,42,13]
list2 = [2,4,6,8]

# Create myreduce function 
def myreduce(func, list1):  
    # Store the 1st item in the list in total
	total = list1[0]
    
    #Loop through the list of all items after 1st item
	for next in list1[1:]:
        #Pass the next sequence number using 'next'
		total = func(total, next)
	return total

# create func function to sum up two numbers and return the result
def func(a,b):
    return a+b

#print the output by invoking func & myreduce
print(myreduce( func,list1))
#print the output by invoking lamda and myreduce
print(myreduce( (lambda x, y: x * y),list2))


##### Problem Solution 2: #####
# Create even_check
def even_check(num):
    if num%2 ==0:
        return True
    
# define sample lists to check the output
lst =range(20)
lst2 = range(5)

#Create myfilter function
def myfilter(even_check,lst):
    #create an empty list to store the filtered items
    lst1=[]
    #loop all the items in the list
    for i in lst:
        # append the list lst1 if the number is even
       isTrue = even_check(i) 
       if (isTrue == True):
           lst1.append(i)
    return lst1

# display the output using myfilter and even_check functions
print(list(myfilter(even_check,lst)))

# display the output using myfilter and lamda functions
lst3 = list(myfilter(lambda x: x%2==0,lst2))
print(lst3)