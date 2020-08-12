#!/usr/bin/env python
# coding: utf-8

# In[416]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[417]:


# How many negative numbers are there?

# use len and numpy to count how many negative numbers there are
amount_of_negative_numbers = len(a[a < 0])

#print results
print(f'There are {amount_of_negative_numbers} negative numbers in the array')


# In[418]:


# How many positive numbers are there?

# use len and numpy to count how many positive numbers there are
amount_of_positive_numbers = len(a[a > 0])

# print results
print(f'There are {amount_of_positive_numbers} positive numbers in the array')


# In[419]:


# How many even positive numbers are there?

# use len and numpy to count how many positive even numbers there are
amount_of_positive_even_numbers = len(a[(a > 0) & (a % 2 == 0)])

print(f'The amount of positive even numbers in the array is {amount_of_positive_even_numbers}')


# In[420]:


# If you were to add 3 to each data point, how many positive numbers would there be?

# create list of numbers in a that if 3 were added to, would be positive, use len to get amount of numbers, store in variable
plus_three_positives_amount = len(a[(a + 3) > 0])

# print results
print(f'If 3 were added to each data point, there would be {plus_three_positives_amount} positive numbers')


# In[421]:


# If you squared each number, what would the new mean and standard deviation be?

# square the array via numpy then round
squared_array_mean_via_nmpy = round(np.average(a ** 2),2)

# find sdev using numpy std then round
squared_array_standard_dev_via_nmpy = round(np.std(a ** 2),2)

# print results
print(f'If each number were squared, the new mean would be {squared_array_mean_via_nmpy} and the new standard dev would be {squared_array_standard_dev_via_nmpy}.')


# In[422]:


# Center the dataset

# calc mean using numpy average
mean_of_a = np.average(a)

# subtract mean from each data point
centered_dataset = a - mean_of_a

# display results
print(f'If the dataset "a" were centered, it would appear as shown below\n\n{centered_dataset}')


# In[423]:


# Calculate the z-score for each data point.

# To find the z-score for each data point we need the standard dev and mean of the data set

# calc mean using numpy average
mean_of_a = np.average(a)

# find sdev using numpy std
standard_deviation = np.std(a)

# find zscores by subtracting mean from each data point then divide each data point by the sdev of the data set
zscores = (a - mean_of_a) / (standard_deviation)

# display results 
print(f'The zscores of the original array are shown below\n\n {zscores}')


# In[424]:


#~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# LIFE WITHOUT NUMPY

# SETUP 1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[425]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# get sum of a using sum and store as variable
sum_of_a = sum(a)

# display results
print(sum_of_a)


# In[426]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# get min of a using min and store as variable
min_of_a = min(a)

# display results
print(min_of_a)


# In[427]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# get max of a using max and store as variable
max_of_a = max(a)

# display results
print(max_of_a)


# In[428]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# get avg of a using sum and len then store as variable
mean_of_a = sum(a) / len(a)

# display results
print(mean_of_a)


# In[429]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# create variable with value of 1
prod_of_a = 1

# iterate through a
for x in a:
    # multiply prod_of_a by each number in a and store for later
    prod_of_a *= x

# display results
print(prod_of_a)


# In[430]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# use list iteration to square each number in a and store as variable
squared = [x ** 2 for x in a]

# display results
print(squared)


# In[431]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# use list iteration to find each odd number in a and store as variable
odds_in_a = [x for x in a if x % 2 == 1]

# display results
print(odds_in_a)


# In[432]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# use list iteration to find each even number in a and store as variable
# 0 is not in a but we're adding code to exclude it for demonstration purposes
evens_in_a = [x for x in a if x % 2 == 0]

# display results
print(evens_in_a)


# In[433]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Although instructions say to only "consider" what it would take to find the values listed,
# we're going to find them anyway in the cells below
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# LIFE WITHOUT NUMPY - continued

# SETUP 2

b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[434]:


# sum of b

# using sum to sum each row and then summing those numbers to find the overall sum
total = sum([sum(x) for x in b])

# display results
print(total)


# In[435]:


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


# In[436]:


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


# In[437]:


# average of b

# create empty list
one_row = []

# iterate over each row of b
for x in b:
    # iterate through each number in each row of b
    for i in x:
        # store each number in new list so that we now have 1 list of numbers
        one_row.append(i)

# divide sum of numbers by len of numbers to calc average
average = sum(one_row) / len(one_row)

# display results
print(average)
    


# In[438]:


# product of b

# create variable with value of 1
total_product = 1

# iterate over each row of b
for x in b:
    # iterate through each number in each row
    for i in x:
        # keep a running total that gets multiplied by each number in the array
        total_product *= i

# display results        
print(total_product)
    


# In[439]:


# list of squares of b

# create empty lists to store squared lists
square1 = []
square2 = []

# iterate over first row of b
for i in b[0]:
    # square each number, store in list
    square1.append(i**2)
# iterate over second row of b
for i in b[1]:
    # square each number, store in list
    square2.append(i**2)

# create third empty list
square3 = []

# append both of the previous lists to create a new list that holds 2 lists in order to preserve original form of array
square3.append(square1)
square3.append(square2)

# display results
print(square3)


# In[440]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SETUP 3

# convert b to numpy array using array
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])


# In[441]:


"""
Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = 0
for row in b:
   sum_of_b += sum(row)
"""

# refactored using numpy to find sum
sum_of_b = np.sum(b)

# print results
print()


# In[442]:


"""
Exercise 2 - refactor the following to use numpy. 

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 
"""

# refactored using numpy to find min in array
min_of_b = np.min(b)

# display results
print(min_of_b)


# In[443]:


"""
Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
"""

# refactored using numpy to find max in array
max_of_b = np.max(b)

# display results
print(max_of_b)


# In[444]:


"""
# Exercise 4 - refactor the following using numpy to find the mean of b

# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
"""

# refactored to find average via numpy average
mean_of_b = np.average(b)

# display results
print(mean_of_b)


# In[445]:


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


# In[446]:


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


# In[447]:


"""
Exercise 7 - refactor using numpy to determine the odds_in_b

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
"""

# refactoring using numpy to create list with only odds by filtering out numbers that if divided by 2, will not have a remainder of 0
odds_in_b = b[(b % 2 != 0)]

# display results
print(odds_in_b)


# In[448]:


"""
Exercise 8 - refactor the following to use numpy to filter only the even numbers
 
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
"""

# refactored using numpy to filter in even numbers ie. numbers that if divided by 2 would have a remainder of 0
# although 0 is not in array, its filtered out for completion sake
evens_in_b = b[b % 2 == 0]

# display results
print(evens_in_b)


# In[449]:


# Exercise 9 - print out the shape of the array b.

# using .shape to print out shape of b, 2 rows 3 columns
shape_of_b = b.shape

# display results
print(shape_of_b)


# In[450]:


# Exercise 10 - transpose the array b.

# using transpose to transpose b
b_transpose = np.transpose(b)

# display results
print(b_transpose)


# In[451]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# using reshape to make a single list with 6 numbers
b_reshape_one_list = b.reshape(1,6)

# display results
print(b_reshape_one_list)


# In[452]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# using reshape to make 6 lists held within 1 list
b_reshape_six_lists = b.reshape(6,1)

# display results
print(b_reshape_six_lists)


# In[453]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Setup 4

# use array to convert c to numpy array
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.


# In[454]:


# Exercise 1 - Find the min, max, sum, and product of c.

# using numpy min to find min of c 
minimum_c = np.min(c)

# using numpy max to find max of c
maximum_c = np.max(c)

# using numpy sum to find sum of c
total_c = np.sum(c)

# using numpy prod to find product of c
product_c = np.prod(c)

# printing results
print(f'The min of c is {minimum_c}')
print(f'The max of c is {maximum_c}')
print(f'The sum of c is {total_c}')
print(f'The product of c is {product_c}')


# In[455]:


# Exercise 2 - Determine the standard deviation of c.

# using numpy std to get the standard deviation of c, round it, store as variable
standard_dev_c = round(np.std(c),2)

# display results
print(standard_dev_c)


# In[456]:


# Exercise 3 - Determine the variance of c.

# use numpy var to get the variance of c, round it, store as variable
variance_c = round(np.var(c),2)

# display results
print(variance_c)


# In[457]:


# Exercise 4 - Print out the shape of the array c

# using numpy shape to get the shape of c, store as variable
shape_c = np.shape(c)

# display results
print(shape_c)


# In[458]:


# Exercise 5 - Transpose c and print out transposed result.

# using numpy transpose to get the transpose of c and store as variable
transposed_c = np.transpose(c)

# display results
print(transposed_c)


# In[459]:


# Exercise 6 - Get the dot product of the array c with c. 

# using numpy dot to get the dot product of c, store as variable
dot_c = np.dot(c, c)

# display results
print(dot_c)


# In[460]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# using numpy transpose to transpose c, multiply by c, then using numpy sum to add all numbers and store as variable
sum_c_times_c_transposed = np.sum(c * (np.transpose(c)))

# display results
print(sum_c_times_c_transposed)


# In[461]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# using numpy transpose to transpose c, multiply by c, then using numpy prod to multiply all numbers and store as variable
prod_c_times_c_transposed = np.prod(c * (np.transpose(c)))

# display results
print(prod_c_times_c_transposed)


# In[462]:


# ~~~~~~~~~~~~~~~~~~~~ MORE NUMPY PRACTICE EXERCISES - SECTION 5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Setup 5

# covert array to numpy array
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])


# In[463]:


# Exercise 1 - Find the sine of all the numbers in d

# find sine for each numbers using numpy sin, store as variable
sin_d = np.sin(d)

# display results
print(sin_d)


# In[464]:


# Exercise 2 - Find the cosine of all the numbers in d

# find cosine for each number using numpy cos, store as variable
cos_d = np.cos(d)

# display results
print(cos_d)


# In[465]:


# Exercise 3 - Find the tangent of all the numbers in d

# find tangent of all numbers in d using numpy tan
tan_d = np.tan(d)

# display results
print(tan_d)


# In[466]:


# Exercise 4 - Find all the negative numbers in d

# using numpy to create list of negative numbers from array
negative_d = d[d < 0]

# display results
print(negative_d)


# In[467]:


# Exercise 5 - Find all the positive numbers in d

# use numpy to create an array that contains all positive number in d
positive_d = d[d > 0]

# display results
print(positive_d)


# In[468]:


# Exercise 6 - Return an array of only the unique numbers in d.

# use numpy unique to create array of unique values in d and store as variable 
unique_d = np.unique(d)

# display results
print(unique_d)


# In[469]:


# Exercise 7 - Determine how many unique numbers there are in d.

# use np unique to count unique values in d then use len to count amount of unique numbers 
unique_d_count = len(np.unique(d))

# display results
print(unique_d_count)


# In[470]:


# Exercise 8 - Print out the shape of d.

# use numpy shape to gather dimensions of d and store as variable
d_shape = np.shape(d)

# display results
print(d_shape)


# In[471]:


# Exercise 9 - Transpose and then print out the shape of d.

# use numpy transpose to transpose d and store as variable
transpose_d = np.transpose(d)

#use numpy shape to get dimensions of transposed array and store as variable
transpose_d_shape = np.shape(transpose_d)

# display results
print(f'Once transposed, d will have a shape of {transpose_d_shape} and look as shown below\n')
# display results
print(transpose_d)


# In[472]:


# Exercise 10 - Reshape d into an array of 9 x 2

# numpy reshape to change dimensions of array to 9x2 and store as variable
d_reshape = d.reshape(9,2)

# display results
print(d_reshape)


# In[ ]:




