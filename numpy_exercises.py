#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[8]:


# How many negative numbers are there?

# use len and numpy to count how many negative numbers there are
amount_of_negative_numbers = len(a[a < 0])

#print results
print(f'There are {amount_of_negative_numbers} negative numbers in the array')


# In[11]:


# How many positive numbers are there?

# use len and numpy to count how many positive numbers there are
amount_of_positive_numbers = len(a[a > 0])

# print results
print(f'There are {amount_of_positive_numbers} positive numbers in the array')


# In[23]:


# How many even positive numbers are there?

# use len and numpy to count how many positive even numbers there are
# must use & instead of and in order for this syntax to work
amount_of_positive_even_numbers = len(a[(a > 0) & (a % 2 == 0)])

print(f'The amount of positive even numbers in the array is {amount_of_positive_even_numbers}')


# In[39]:


# If you were to add 3 to each data point, how many positive numbers would there be?

# add 3 to each data point
plus_three = a + 3

# create variable to store the number of positive numbers
plus_three_positives_amount = (len(plus_three[(plus_three + 3) > 0]))

# print results
print(f'If 3 were added to each data point, there would be {plus_three_positives_amount} positive numbers')


# In[141]:


# If you squared each number, what would the new mean and standard deviation be?

# PART 1 - SQUARE EACH NUMBER IN ORIGINAL ARRAY

# import math for later use
import math

# square each number in the array to make new_array aka na
new_array = a ** 2

# PART 2 - FIND NEW MEAN

# sum the squared array then divide by length of array to get the mean
new_array_mean = sum(new_array) / len(new_array)

# PART 3 - FIND NEW STANDARD DEVIATION

# subtract mean from new_array then square it
new_array_minus_mean_squared = (new_array - new_array_mean) ** 2

# calc rounded sdev by finding the square root of the mean of the newly squared array
standard_dev = round(math.sqrt(sum(new_array_minus_mean_squared) / len(new_array_minus_mean_squared)),2)

# Print results
print(f'If each number were squared, the new mean would be {new_array_mean} and the new standard dev would be {standard_dev}.')


# In[86]:


# Center the dataset (sort?)

# calc mean
mean_of_a = sum(a) / len(a)

# subtract mean from each data point
centered_dataset = a - mean_of_a

# display results
print(f'If the dataset "a" were centered, it would appear as shown below\n\n{centered_dataset}')


# In[109]:


# Calculate the z-score for each data point.

# import math for later use, this was done in a previous exercise but we'll do it again for demonstration
import math

# To find the z-score for each data point we need the standard dev and mean of the data set

# STEP 1 - FIND MEAN

# calc mean using sum and len to divide sum of array by length of array
mean_of_a = sum(a) / len(a)

# STEP 2 - FIND STANDARD DEVIATION

# subtract mean from each data point then square each data point
sub_mean_from_a = (a - mean_of_a) ** 2

# find mean of newly squared array
new_mean = sum(sub_mean_from_a) / len(sub_mean_from_a)

# calc square root of the new mean to find the standard deviation
standard_deviation = math.sqrt(new_mean)

# STEP 3 - FIND Z SCORE 

# subtract mean from each data point then divide each data point by the sdev of the data set
zscores = (a - mean_of_a) / standard_deviation

# display results 
print(f'The zscores of the original array are shown below\n\n {zscores}')


# In[21]:


# MORE NUMPY PRACTICE EXERCISES - SECTION 1

# SETUP
# changing array name to b 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[22]:


# Exercise 1 - Make a variable called sum_of_b to hold the sum of all the numbers in above list

sum_of_a = sum(a)

print(sum_of_a)


# In[23]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

print(min_of_a)


# In[24]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

print(max_of_a)


# In[31]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a) / len(a)

print(mean_of_a)


# In[35]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

prod_of_a = 1

for x in a:
    prod_of_a *= x

print(prod_of_a)


# In[47]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squared = [x ** 2 for x in a]

print(squared)


# In[50]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [x for x in a if x % 2 == 1]

print(odds_in_a)


# In[52]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [x for x in a if x % 2 == 0 and x != 0]

print(evens_in_a)


# In[62]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[65]:


# sum of b

total = sum([sum(x) for x in b])

print(total)


# In[74]:


# min of b

row_minimum = []

for x in b:
    row_minimum.append(min(x))
    
overall_minimum = min(row_minimum)
    
print (overall_minimum)


# In[76]:


# max of b

row_maximum = []

for x in b:
    row_maximum.append(max(x))
    
overall_maximum = max(row_maximum)
    
print (overall_maximum)


# In[81]:


# average of b

one_row = []

for x in b:
    for i in x:
        one_row.append(i)
        
average = sum(one_row) / len(one_row)
    
print(average)
    


# In[ ]:


# product of b


# In[ ]:


# list of squares of b


# In[ ]:





# In[ ]:




