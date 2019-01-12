# This problem was asked by Amazon.
# 
# Given an integer k and a string s, 
# find the length of the longest substring that contains at most k distinct characters.
# 
# For example,
# given s = "abcba" and k = 2, 
# the longest substring with k distinct characters is "bcb"
# 
# 

import math

def longestNonRepeatingSequence(str):
    
    visited = [-1] * 256 
    visited[ord(str[0])] = 0 
    previndex = -1 
    maxlen = 0
    curlen = 1 
    
    for i in range(1 , len(str)):
        
        prev_index = visited[ord(str[i])]
        
        if( prev_index == -1 or i - curlen > prev_index):
            curlen += 1 
        else:
            
            if(curlen > maxlen):
                maxlen = curlen 
                
            curlen = i-prev_index
        visited[ord(str[i])] = i
    
    return max(curlen,maxlen)
    
    
longestNonRepeatingSequence("NANDAN")    
 
 
 
 
 
 
