#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[2]:


# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)
print (numbers_plus_one)


# In[3]:


# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]
print (numbers_plus_one)


# In[4]:


# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
print(output)


# In[5]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
#     Make a variable named uppercased_fruits to hold the output of the list comprehension. 
#     Output should be ['MANGO', 'KIWI', etc...]
output = [fruit.upper() for fruit in fruits]
print(output)


# In[7]:


# Exercise 2 - create a variable named capitalized_fruits 
#     and use list comprehension syntax to produce output like 
#     ['Mango', 'Kiwi', 'Strawberry', etc...]

output = [fruit.capitalize() for fruit in fruits]

print(output)


# In[11]:


# Exercise 3 - Use a list comprehension to make a variable named 
#     fruits_with_more_than_two_vowels. 
#     Hint: You'll need a way to check if something is a vowel.
# vowels = 'aeiouAEIOU'
fruits_with_more_than_two_vowels = [f for f in fruits if sum([1 for char in f if char in 'aeiouAEIOU']) > 2]

print(fruits_with_more_than_two_vowels)


# In[13]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. 
#     The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [f for f in fruits if sum([1 for char in f if char in 'aeiouAEIOU']) == 2]
print(fruits_with_only_two_vowels)


# In[15]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_5_letters = [f for f in fruits if len(f) > 5]

print(more_than_5_letters)


# In[17]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
just_5 = [f for f in fruits if len(f) == 5]
print(just_5)


# In[18]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
under_5 = [f for f in fruits if len(f) < 5]
print(under_5)


# In[19]:


# Exercise 8 - Make a list containing the number of characters in each fruit. 
#     Output would be [5, 4, 10, etc... ]
num_char = [len(f) for f in fruits]
print(num_char)


# In[26]:


# Exercise 9 - Make a variable named fruits_with_letter_a that 
#     contains a list of only the fruits that contain the letter "a"
if_a_in = [f for f in fruits if 'a' in f]
print(if_a_in)


# In[28]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# In[29]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)


# In[30]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)


# In[31]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)


# In[33]:


# Exercise 14 - use a list comprehension w/ a conditional in order to 
#     produce a list of numbers with 2 or more numerals
output = [n for n in numbers if int(n/10) > 0]
print(output)


# In[34]:


# Exercise 15 - Make a variable named numbers_squared that 
#     contains the numbers list with each element squared. 
#     Output is [4, 9, 16, etc...]
numbers_squared = [n ** 2 for n in numbers]
print(numbers_squared)


# In[35]:


# Exercise 16 - Make a variable named odd_negative_numbers that 
#     contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 == 1]
print(odd_negative_numbers)


# In[36]:


# Exercise 17 - Make a variable named numbers_plus_5. 
#     In it, return a list containing each number plus five. 
numbers_plus_5 = [n + 5 for n in numbers]
print(numbers_plus_5)


# In[44]:


# BONUS Make a variable named "primes" that is a list containing 
#     the prime numbers in the numbers list. 
#     *Hint* you may want to make or find a helper function that 
#     determines if a given number is prime or not.
def isPrime(n):
    if n < 0: return False 
    for num in range (2,n):
        if n % num == 0:
            return False
    return True

primes = [n for n in numbers if isPrime(n)]
print(primes)

