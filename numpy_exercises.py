#!/usr/bin/env python
# coding: utf-8

# In[66]:


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


# In[67]:


# If you squared each number, what would the new mean and standard deviation be?

# PART 1 - SQUARE EACH NUMBER IN ORIGINAL ARRAY

# import math for later use
import math

# square each number in the array
squared = a ** 2

# PART 2 - FIND NEW MEAN

# use sum to get sum of all squared numbers
sum_squared = sum(squared)

# divide sum by amount of numbers to get mean
new_mean = sum_squared / len(squared)

# PART 3 - FIND NEW STANDARD DEVIATION

# subtract mean from squared array
subtract_mean_from_squared = squared - new_mean

# square array known as subtract_mean_from_squared
square_subtract_mean_from_squared = subtract_mean_from_squared ** 2

# calc mean of array known as square_subtract_mean_from_squared
avg_of_square_subtract_mean_from_squared = sum(square_subtract_mean_from_squared) / len(square_subtract_mean_from_squared)

# calc sdev by finding square root of new mean 
standard_dev = round(math.sqrt(avg_of_square_subtract_mean_from_squared))

# Print results
print(f'If each number were squared, the new mean would be {new_mean} and the new standard dev would be {standard_dev}.')


# In[86]:


# Center the dataset (sort?)

# calc mean
mean_of_a = sum(a) / len(a)

# subtract mean from each data point
centered_dataset = a - mean_of_a

# display results
print(f'If the dataset "a" were centered, it would appear as shown below\n\n{centered_dataset}')


# In[ ]:


# Calculate the z-score for each data point.

# To find the z-score for each data point we need the standard dev and mean of the data set

#STEP 1 - FIND MEAN

# 
mean_of_a = sum(a) / len(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




