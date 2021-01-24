#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import os
import string
import random


# In[2]:


#M = ["Starbuck", "Stubb", "Flask"]   
#L = [hashlib.sha256(x.encode('utf-8')).hexdigest() for x in M] 
#print(L)


# In[3]:


#str = "Hello World"
#byte_str = str.encode('utf-8')
#print(byte_str)


# 1. Hash Collisions
# Use a brute-force algorithm to find a partial collision.
# Using the template “hash_collision.py” write a function called “hash_collision” that takes a single input, k, where k is an integer. The function “hash_collision” should return two variables, x and y, such that that the SHA256(x) and SHA256(y) match on their final k bits. The return variables, x and y, should be encoded as bytes.
# To encode a string as bytes
# str = "Hello World"
# byte_str = str.encode('utf-8')
# Your algorithm should be randomized, i.e., hash_collision(k) should not always return the same colliding pair.
# 
#     You need to get around 20 bits worth of collisions

# In[4]:


def get_key(val,mydict):
    for key, value in mydict.items():
        if val == value:
            return key
    return "key doesn't exist"


# In[5]:


def randomString(N):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(N))
  


# In[6]:


def my_to_bin(string):
    res = ''
    for char in string:
        tmp = (bin(int(char,16))[2:])
        tmp = '%08d' %int(tmp)
        res += tmp
    return res


# In[7]:


def getbytes(bits):
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        yield byte


# In[17]:


[x,y] = hash_collision(16)
#print("this is x:",x)
#print("this is y:",y)

print("\n")

colissionXY = [x, y]   
#[myX,myY] = [hashlib.sha256(x).hexdigest() for x in colissionXY] 
print("sha256(x)=", x)
print("sha256(y)=", y)


# 1. Partial preimages
# Use a brute-force algorithm to find a partial preimage.
# Using the template “hash_preimage.py” write a function called “hash_preimage” that takes a single input, target_string, where target_string is a string of bits. The function “hash_preimage” should return a single variable x such that the trailing bits of SHA256(x) matches the target string (not the hash of the target string).
# Your algorithm should be randomized, i.e., hash_preimage(target_string) should not always return the same partial preimage
# 
#     Example: If our target string was 101 and the hash(x)=01000101 then this would be a match because the least significant bits (rightmost) completely match the target string.

# In[39]:


def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k <=0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here


    mydict = {}
    n=10
    print("this is k=", k)
    i=1
    
    while True:
        msgX_str = randomString(n)
        msgY_str = randomString(n)
       
        digX_bin = my_to_bin(hashlib.sha256(msgX_str.encode('utf-8')).hexdigest())
        digY_bin = my_to_bin(hashlib.sha256(msgY_str.encode('utf-8')).hexdigest())
        
        valueX = digX_bin[-k:]
        valueY = digY_bin[-k:]
        keyX = msgX_str
        keyY = msgY_str
        
    
        if valueY in mydict.values():
            if msgX_str==msgY_str:
                continue
            else:
                x_str = get_key(valueY,mydict)
                
                print("this is i",i)
                myX_bin = my_to_bin(hashlib.sha256(x_str.encode('utf-8')).hexdigest())
                myY_bin = my_to_bin(hashlib.sha256(msgY_str.encode('utf-8')).hexdigest())
                print("myX_bin =", myX_bin)
                print("myY_bin =", myY_bin)
                
                y = keyY.encode('utf-8')
                x = x_str.encode('utf-8')
                return( x, y )
        
        if valueX not in mydict.values():
            mydict.update({keyX:valueX})           

    
        if valueY not in mydict.values():
            mydict.update({keyY:valueY})
        i=i+1
        
    
    x = b'\x00'
    y = b'\x00'
    
    return( x, y )


# In[41]:



[x,y] = hash_collision(14)
print("x_bytes", x)
print("y_bytes", y)


# In[ ]:




