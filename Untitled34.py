#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

*  =  Expression

'hello'= Value

-87.8 = Value

-  =  Expression

(=, Expression)

+  =  Expression

6  =  Value


# In[ ]:


#2. What is the difference between string and variable?

string in python are identified as a contiguous set of character represented in the quotataion marks.
eg:-'hello',"rise"

variables are nothing but reserved memory locationsto store values.This means that you create a variable you reserve some some space in memory.


# In[ ]:


#3. Describe three different data types.

String :- string in python are identified as a contiguous set of character represented in the quotataion marks.
     eg:-'hello',"rise"

List :- List is used for storing multiple data items in a single variable.It contains items separated by commas and enclosed within square bracket([ ])
    eg:- a_list =[1,3,'hello']
    
Dictionary :- Dictionaries are used to store data values in key:value pairs.
        eg :- b = {'name':'avhi','code':8,'dept':'cse'}
            


# In[ ]:


#4. What is an expression made up of? What do all expressions do?
An expression is a combination of operators, constants and variables. An expression may consist of one or more operands, and zero or more operators to produce a value.
eg:- a = 2 * 3
    


# In[ ]:


#5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

An expression is a combination of values, variables, operators, and calls to functions where as a statement is an instruction that the Python interpreter can execute.


# In[ ]:


#6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1


# In[1]:


bacon = 22
bacon +1


# In[ ]:


#7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3


# In[2]:


'spam' + 'spamspam'


# In[3]:


'spam' * 3


# In[ ]:


#8. Why is eggs a valid variable name while 100 is invalid?
 
100 is invalid because we cannot give variable as integer where as eggs is valid because it is a string.


# In[ ]:


#9. What three functions can be used to get the integer, floating-point number, or string version of a value?

int()
float()
str()


# In[ ]:


#10. Why does this expression cause an error? How can you fix it?
    'I have eaten' + 99 + 'burritos' 

Here 99 is an integer it cannot be concatenated with strings, if we have to concatenate it we need to do typecasting.


# In[10]:


'I have eaten' + '99' + 'burritos' 


# In[ ]:




