# 
# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.
# 
# For example,
# given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# 

def findsubsets(l1 , allsum , subsetsum , partialsum):
    

    if(  subsetsum == sum(partialsum) and len(partialsum) == 2  ):
        print(partialsum)
        return 
     
  
    if( len(l1) == 0):
        return 

    if(sum(partialsum) + l1[0] <= subsetsum ):
        findsubsets(l1[1:] , allsum - l1[0] , subsetsum , partialsum+[l1[0]])
    
    findsubsets(l1[1:] , allsum - l1[0] , subsetsum , partialsum )
    
 
    
all = [1,2,3,4,5,6,7,8,9,10]
findsubsets(all ,sum(all), 12 ,[])




