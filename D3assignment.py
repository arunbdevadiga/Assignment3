#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Assignment-3
# 

# #  Q1 write a python function to find the max of three numbers

# In[7]:


a= int(input("Enter a first number"))
b= int(input("Enter a second number"))
c= int(input("Enter a third number"))
x=max(a,b,c)
print("Maximum Number is",x)


# In[ ]:





# # Q2  write a python function that checks whether a passed string is palindrome or not

# In[11]:


def ispalindrome(s):
    return s==s[::-1]
s=input("enter a string  ")
ans = ispalindrome(s)

if ans:
    print("yes, passed string is palindrome")
else:
    print("no, passed string is not palindrome")


# In[ ]:





# # Q3  write a python function that accepts a string and calculate the number of uppercase  letters and lowercase letters

# In[9]:


print("Enter a sentence: ")
sentence = input()
 
uppercase_lowercase = {"Upper":0, "Lower":0}
 
for x in sentence:
    if x.isupper():
        uppercase_lowercase["Upper"]+=1
    elif x.islower():
        uppercase_lowercase["Lower"]+=1
    else:
        pass
 
print("Upper", uppercase_lowercase["Upper"])
print("Lower", uppercase_lowercase["Lower"])


# In[ ]:





# # Q4  write a python function to sum all the numbers in the list

# In[2]:


list1 = [10,20,45,78,13,64,97]
total= sum(list1)
print('sum of all the numbers in a list is  :',total)


# In[ ]:





# # Q5 write a python function to multiply all the numbers in a list

# In[5]:


import math
list1 = [1,3,4,2,6]
multiple= math.prod(list1)
print('Multiplication of all the numbers in a list is  :',multiple)


# In[ ]:





# # Q6 write a python function that takes a list and return a new list with unique elements of the first list
# 

# In[6]:


def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print('unique elements are')
print(unique_list([1,2,4,5,4,5,6,9,10])) 


# In[ ]:





# In[ ]:




