# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 23:43:19 2017

@author: WesleySiow
"""

# Use an import statement at the top

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
    import random as r
    import string as s
    
    password = []
    
    result = ''
    
    
    
    password = r.sample(word_list, 3)
    print(password)
    
    #result = ''.join(password)
    #print("result = {}".format(result))
    print(str().join(password))
        
    
    #return result
    return str().join(password)

generate_password()