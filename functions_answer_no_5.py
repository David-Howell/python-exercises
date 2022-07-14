#!/usr/bin/env python
# coding: utf-8

# #### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# 

# In[ ]:


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


# In[ ]:


import random
for x in range (100):
    x += 1
    x /= 100
    y = float(''.join (random.sample([str(x) for x in range(10)], 4))) / 100
    print(calculate_tip(x,y))

