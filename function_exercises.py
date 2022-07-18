#!/usr/bin/env python
# coding: utf-8

# # Exercises
# ### Create a file named function_exercises.py for this exercise. 
# * After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[1]:


def is_two(x):
    '''
    is_two is a function that accepts one input 
    and returns True if the passed input is 
    either the number or the string 2,
    False otherwise
    '''
    return x == '2' or x == 2


# In[3]:


x = input('Enter 2 ')
is_two(x)


# In[7]:


for i in range (5):
    x = i
    print(i, ' ', is_two(x))


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[198]:


def is_vowel(x):
    x = str(x)
    if x in 'aeiouAEIOU' and len(x) == 1:
        return True
    else: return False


# In[199]:


a = input('Enter a vowel ')
print(is_vowel(a))


# In[200]:


is_vowel(2)


# #### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[201]:


def is_consonant(x):
    x = str(x)
    if x in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM' and len(x) == 1:
        return True
    else: return False


# In[205]:


a = input('Enter a consonant ')
print(is_consonant(a))


# #### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[207]:


def cap_that_con(x):
#     if x[:1] in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM':
    if is_consonant(x[:1]):
        x = x.capitalize()
    return x


# In[208]:


i = 'while'
while i.lower() != 'quit':
    i = input('Enter a word, any word! ')
    print('\n', cap_that_con(i), '\n')


# #### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[195]:


# use def to define the function with two inputs:
#     The tip percentage as a decimal >> tip - which will be a float
#     The amount of the tab >> tab - entered as a float or int
def calculate_tip(tip, tab):
#     if the tab is entered as an int it is changed to a float:
#         this will be used for formating purposes in the output string discussed below
    tab = float(tab)
#     the tip amount is calculated by multipling the input percentage by the input tab:
#         round is used to get a whole cent value as we're used to with money
    tip_amount = round(tip * tab, 2)
#     the tip and tab are added together, and again we round to 2 digits so the output isn't broken by float errors
    total_with_tip = round(tab + tip_amount, 2)
#     the next three if statements do the same thing to our three variables for display:
#         first check to see if the value is equivalent to the round value
#             this would be the case if the float is equivalent to an int
#         second check to see if the value times 10 is equivalent to the round value times 10
#             this would be the case if the number of cents is a multiple of 10
    if tip_amount == round(tip_amount) or tip_amount * 10 == round(tip_amount * 10): 
#         if either of the foregoing conditions are true we convert the float to a str and add a '0'
#             as such, the decimal will be displayed as 2 digits
        tip_amount = str(tip_amount) + '0'
    if tab == round(tab) or tab * 10 == round(tab * 10):
        tab = str(tab) + '0'
    if total_with_tip == round(total_with_tip) or total_with_tip * 10 == round(total_with_tip * 10):
        total_with_tip = str(total_with_tip) + '0'
#         finally we return a string as a sentence detailing:
#             the tip percentage, original tab, the tip in dollars, and the total
#             this is formated so that used in a loop the data is nearly tabular 
    return f'If you tip {round(tip*100):>3}% on ${tab:>5} the tip amount is ${tip_amount:>5} for a total of ${total_with_tip}'


# In[176]:


print(calculate_tip(.2, 50))


# In[196]:


import random
for x in range (100):
    x += 1
    x /= 100
    y = float(''.join (random.sample([str(x) for x in range(10)], 4))) / 100
    print(calculate_tip(x,y))


# In[90]:


import random
for x in range(1, 101):
    x /= 100
    y = float(''.join (random.sample([str(x) for x in range(10)], 4))) / 100
    print(f'if you tip {round(x*100)}% on ${y} the tip and total are {calculate_tip(x,y)}')


# #### 6. Define a function named apply_discount. It should accept an original price, and a discount percentage, and return the price after the discount is applied.

# In[209]:


def apply_discount(oprice, discount = 0.0):
    dprice = oprice - oprice * discount
    return dprice


# In[211]:


print(apply_discount(50, .2))
print(apply_discount(10, .5))
print(apply_discount(1000, .3))
print(apply_discount(70))


# #### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[106]:


def handle_commas(string_o_nums_with_commas):
    x = string_o_nums_with_commas.replace(',','')
    return int(x)


# In[107]:


print(handle_commas('1,000,000'))
print(handle_commas('1,2,3,5,4,8,6,9,7,1'))


# #### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[214]:


def get_letter_grade(z):
    if z == 42: print(z, '! That\'s the meaning of everything!')
    elif z >= 90: print(z,'is an A')
    elif z >= 80: print(z,'is a B')
    elif z >= 70: print(z, 'is a C')
    elif z > 60: print(z, 'is a D')
    elif z <= 60: print(z, 'is an F')


# In[215]:


get_letter_grade(100)
get_letter_grade(93)
get_letter_grade(87)
get_letter_grade(80)
get_letter_grade(74)
get_letter_grade(70)
get_letter_grade(66)
get_letter_grade(61)
get_letter_grade(60)
get_letter_grade(42)


# #### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[133]:


def remove_vowels(this_string):
    return ''.join([l for l in this_string if l not in 'aeiouAEIOU'])


# In[134]:


i = input('Type a sentence for vowel removal... ')
print(remove_vowels(i))


# #### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#   * anything that is not a valid python identifier should be removed
#   * leading and trailing whitespace should be removed
#   * everything should be lowercase
#   * spaces should be replaced with underscores
#   * for example:
#    * Name will become name
#    * First Name will become first_name
#    * % Completed will become completed

# In[216]:


get_ipython().run_line_magic('pinfo', 'str.isidentifer')


# In[153]:


def normalize_name(string_here):
    string_here = ((string_here.strip()).lower()).replace(' ', '_')
    string_here = ''.join([c for c in string_here if c in 'qwertyuiopasdfghjklzxcvbnm1234567890_'])
    string_here = string_here.strip('_')
    return string_here 


# In[154]:


print(normalize_name(' %$ Happy times aRE HERE!  '))


# #### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#    * cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#    * cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[161]:


def cumulative_sum(num_list):
    start = 0
    sum_num_list = []
    for num in num_list:
        start = num + start
        sum_num_list.append(start)
    return sum_num_list


# In[164]:


print(cumulative_sum([1,2,3,4,5]))
print(cumulative_sum([3,6,1,7,3,6,8]))
print(cumulative_sum([1,5,2,3,2,2,2]))


# ### Additional Exercise
#   #### * Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# ### Bonus
# #### 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# #### 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#   * col_index('A') returns 1
#   * col_index('B') returns 2
#   * col_index('AA') returns 27
