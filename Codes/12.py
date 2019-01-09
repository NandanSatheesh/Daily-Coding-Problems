# 
# 
# #12
# 
# This was asked by Amazon
# 
# There exists a staircase with N steps,
# and you can climb up either 1 or 2 steps at a time.
# 
# Given N, 
# write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
# 
# For example, if N is 4, then there are 5 unique ways:
#     1, 1, 1, 1
#     2, 1, 1
#     1, 2, 1
#     1, 1, 2
#     2, 2
# 
# 


ways = []


def getAllWays(n,steps,sequence):
    if( n == 0 ):
        if(sequence not in ways):
            ways.append([sequence])
        print(sequence)
    else:
        
        for i in steps:
            
            if( n - i >= 0 ):
                getAllWays(n-i , steps , sequence +[i])
        
    
    

possibleValues =[1,2]
ways = []
getAllWays(4 , possibleValues , [])
print(len(ways))

# Output
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# 5
