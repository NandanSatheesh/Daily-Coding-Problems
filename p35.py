# Problem 35
# This problem was asked by Google.
# 
# Given an array of strictly the characters 
# 'R', 'G', and 'B', segregate the values 
# of the array so that all the Rs come first, 
# the Gs come second, and the Bs come last. 
# 
# You can only swap elements of the array.
# 
# Do this in linear time and in-place.
# 
# For example, 
# given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
# 
# 

def onlySwap(i,letter):
    for j in range(len(arr)):
        if(arr[j] == letter):
            arr[j] , arr[i] = arr[i] , arr[j]
            i=i+1 
   
    return i 


arr = ['B','G','G','R','G','G','R','R','B']
nextPosition = onlySwap( 0 ,'R')
nextPositon = onlySwap(nextPosition , 'G')

print(arr)

# Outputs 
# ['R', 'R', 'R', 'B', 'G', 'G', 'G', 'G', 'B']
