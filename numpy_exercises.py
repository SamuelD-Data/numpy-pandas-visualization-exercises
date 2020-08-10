#!/usr/bin/env python
# coding: utf-8

# In[210]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[211]:


# How many negative numbers are there?

# use len and numpy to count how many negative numbers there are
amount_of_negative_numbers = len(a[a < 0])

#print results
print(f'There are {amount_of_negative_numbers} negative numbers in the array')


# In[212]:


# How many positive numbers are there?

# use len and numpy to count how many positive numbers there are
amount_of_positive_numbers = len(a[a > 0])

# print results
print(f'There are {amount_of_positive_numbers} positive numbers in the array')


# In[213]:


# How many even positive numbers are there?

# use len and numpy to count how many positive even numbers there are
# must use & instead of and in order for this syntax to work
amount_of_positive_even_numbers = len(a[(a > 0) & (a % 2 == 0)])

print(f'The amount of positive even numbers in the array is {amount_of_positive_even_numbers}')


# In[214]:


# If you were to add 3 to each data point, how many positive numbers would there be?

# create list of numbers in a that if 3 were added to, would be positive, use len to get amount of numbers, store in variable
plus_three_positives_amount = len(a[(a + 3) > 0])

# print results
print(f'If 3 were added to each data point, there would be {plus_three_positives_amount} positive numbers')


# In[215]:


# If you squared each number, what would the new mean and standard deviation be?

# PART 1 - SQUARE EACH NUMBER IN ORIGINAL ARRAY

# square the array via numpy then round
squared_array_mean_via_nmpy = round(np.average(a ** 2),2)

# find sdev using numpy std then round
squared_array_standard_dev_via_nmpy = round(np.std(a ** 2),2)

# print results
print(f'If each number were squared, the new mean would be {squared_array_mean_via_nmpy} and the new standard dev would be {squared_array_standard_dev_via_nmpy}.')


# In[216]:


# Center the dataset

# calc mean
mean_of_a = np.average(a)

# subtract mean from each data point
centered_dataset = a - mean_of_a

# display results
print(f'If the dataset "a" were centered, it would appear as shown below\n\n{centered_dataset}')


# In[217]:


# Calculate the z-score for each data point.

# import math for later use, this was done in a previous exercise but we'll do it again for demonstration
import math

# To find the z-score for each data point we need the standard dev and mean of the data set

# STEP 1 - FIND MEAN

# calc mean using numpy average
mean_of_a = np.average(a)

# STEP 2 - FIND STANDARD DEVIATION

# find sdev using numpy std
standard_deviation = np.std(a)

# STEP 3 - FIND Z SCORE 

# subtract mean from each data point then divide each data point by the sdev of the data set
zscores = (a - mean_of_a) / (standard_deviation)

# display results 
print(f'The zscores of the original array are shown below\n\n {zscores}')


# In[218]:


#~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# LIFE WITHOUT NUMPY

# SETUP
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[219]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# get sum of a using sum and store as variable
sum_of_a = sum(a)

# display results
print(sum_of_a)


# In[220]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# get min of a using min and store as variable
min_of_a = min(a)

# display results
print(min_of_a)


# In[221]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# get max of a using max and store as variable
max_of_a = max(a)

# display results
print(max_of_a)


# In[222]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# get avg of a using sum and len then store as variable
mean_of_a = sum(a) / len(a)

# display results
print(mean_of_a)


# In[223]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# create variable with value of 1
prod_of_a = 1

#iterate through a
for x in a:
    # multiply prod_of_a by each number in a and store for later
    prod_of_a *= x

# display results
print(prod_of_a)


# In[224]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# use list iteration to square each number in a and store as variable
squared = [x ** 2 for x in a]

# display results
print(squared)


# In[225]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# use list iteration to find each odd number in a and store as variable
odds_in_a = [x for x in a if x % 2 == 1]

# display results
print(odds_in_a)


# In[226]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# use list iteration to find each even number in a and store as variable
# 0 is not in a but we're adding code to exclude it for demonstration purposes
evens_in_a = [x for x in a if x % 2 == 0 and x != 0]

# display results
print(evens_in_a)


# In[227]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Although instructions say to only "consider" what it would take to find the values listed,
# we're going to find them anyway in the cells below
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# LIFE WITHOUT NUMPY

b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[228]:


# sum of b

# using sum to sum each row and then summing those numbers to find the overall sum
total = sum([sum(x) for x in b])

# display results
print(total)


# In[229]:


# min of b

# creating empty list
row_minimum = []

# iterate over each row of b
for x in b:
    # take the minimum of each row and store it in list
    row_minimum.append(min(x))

# use min to find minimum in list and store as variable
overall_minimum = min(row_minimum)

# display results
print (overall_minimum)


# In[230]:


# max of b

# create empty list
row_maximum = []

# iterate over each row of b
for x in b:
    # take the max of each row and store in list
    row_maximum.append(max(x))

# find the max in new list and store as variable
overall_maximum = max(row_maximum)

# display results
print (overall_maximum)


# In[231]:


# average of b

# create empty list
one_row = []

# iterate over each row of b
for x in b:
    # iterate through each number in each row of b
    for i in x:
        # store each number in new list so that we now have 1 list of numbers
        one_row.append(i)

# divide sum of number by len of numbers to calc average
average = sum(one_row) / len(one_row)

# display results
print(average)
    


# In[232]:


# product of b

# create variable with value of 1
total_product = 1

# iterate over each row of b
for x in b:
    # iterate through each number in each row
    for i in x:
        # keep a running total that gets multiplied by each number
        total_product *= i

# display results        
print(total_product)
    


# In[233]:


# list of squares of b

# use list iteration to iterate over each number and square them then store as variable
squares = [i ** 2 for x in b for i in x]

# display results
print(squares)


# In[234]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# convert b to numpy array using array
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

"""
Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = 0
for row in b:
   sum_of_b += sum(row)
"""

# refactored using numpy to find sum
sum_of_b = np.sum(b)

# print results
print(sum_of_b)


# In[235]:


"""
Exercise 2 - refactor the following to use numpy. 

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 
"""

# refactored using numpy to find min in array
min_of_b = np.min(b)

# display results
print(min_of_b)


# In[236]:


"""
Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
"""

# refactored using numpy to find max in array
max_of_b = np.max(b)

# display results
print(max_of_b)


# In[254]:


"""
# Exercise 4 - refactor the following using numpy to find the mean of b

# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
"""

# refactored to find average by dividing sum of b (found via sum) by the amount of numbers of b (found via size )
mean_of_b = np.average(b)

# display results
print(mean_of_b)


# In[238]:


"""
Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
"""

# refactored using prod to multiply each number and store as variable
product_of_b = np.prod(b)

# display results
print(product_of_b)


# In[255]:


"""
Exercise 6 - refactor the following to use numpy to find the list of squares 

squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
"""

# refactoring using numpy square to square each number
squares_of_b = np.square(b)

# display results
print(squares_of_b)


# In[258]:


"""
Exercise 7 - refactor using numpy to determine the odds_in_b

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
"""

# refactoring using numpy to create list with only odds
odds_in_b = b[(b % 2 != 0)]

# display results
print(odds_in_b)


# In[241]:


"""
Exercise 8 - refactor the following to use numpy to filter only the even numbers
 
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
"""

# refactored using numpy to filter even numbers, although 0 is not in array, its filtered out for completion sake
evens_in_b = b[(b % 2 == 0) & (b != 0)]

# display results
print(evens_in_b)


# In[242]:


# Exercise 9 - print out the shape of the array b.

# using .shape to print out shape of b, 2 rows 3 columns
shape_of_b = b.shape

# display results
print(shape_of_b)


# In[243]:


# Exercise 10 - transpose the array b.

# using transpose to transpose b
b_transpose = np.transpose(b)

# display results
print(b_transpose)


# In[244]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# using reshape to make a single list with 6 numbers
b_reshape_one_list = b.reshape(1,6)

# display results
print(b_reshape_one_list)


# In[245]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# using reshape to make 6 lists held within 1 list
b_reshape_six_lists = b.reshape(6,1)

# display results
print(b_reshape_six_lists)


# In[246]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Setup 3

# use array to convert c to numpy array
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

# Exercise 1 - Find the min, max, sum, and product of c.

# using numpy min, max, sum, and prod to get their respective values from c
minimum_c = np.min(c)

maximum_c = np.max(c)

total_c = np.sum(c)

product_c = np.prod(c)

# printing results
print(f'The min of c is {minimum_c}')

print(f'The max of c is {maximum_c}')

print(f'The sum of c is {total_c}')

print(f'The product of c is {product_c}')


# In[263]:


# Exercise 2 - Determine the standard deviation of c.

# using numpy std to get the standard deviation of c, round it, store as variable
standard_dev_c = round(np.std(c),2)

# display results
print(standard_dev_c)


# In[265]:


# Exercise 3 - Determine the variance of c.

# use numpy var to get the variance of c, round it, store as variable
variance_c = round(np.var(c),2)

# display results
print(variance_c)


# In[267]:


# Exercise 4 - Print out the shape of the array c

# using numpy shape to get the shape of c, store as variable
shape_c = np.shape(c)

# display results
print(shape_c)


# In[272]:


# Exercise 5 - Transpose c and print out transposed result.

# using numpy transpose to get the transpose of c and store as variable
transposed_c = np.transpose(c)

# display results
print(transposed_c)


# In[271]:


# Exercise 6 - Get the dot product of the array c with c. 

# using numpy dot to get the dot product of c, store as variable
dot_c = np.dot(c, c)

# display results
print(dot_c)


# In[275]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# using numpy transpose to transpose c, multiply by c, then using numpy sum to add all numbers and store as variable
sum_c_times_c_transposed = np.sum(c * (np.transpose(c)))

# display results
print(sum_c_times_c_transposed)


# In[277]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# using numpy transpose to transpose c, multiply by c, then using numpy prod to multiply all numbers and store as variable
prod_c_times_c_transposed = np.prod(c * (np.transpose(c)))

# display results
print(prod_c_times_c_transposed)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



