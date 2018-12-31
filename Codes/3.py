# This problem was asked by Facebook
# 
# Given a string of round, curly, and square open and closing brackets,  
# return whether the brackets are balanced (well-formed).  
#   
# For example, given the string "([])[]({})", you should return true.  
# Given the string "([)]" or "((()", you should return false.  
# 
# 


def balancedBrackets(s):
    stack = []
    for i in s:
        if(len(stack) == 0 and (i ==')' or i =='}' or i ==']' )):
            return False 
        
        if( i == '{' or i == '[' or i=='(' ):
            stack.append(i)
        else:
            if(i ==')' and stack[-1] == '('):
                stack.pop()
            elif(i =='}' and stack[-1] == '{'):
                stack.pop()
            elif(i ==']' and stack[-1] == '['):
                stack.pop()    
            else:
                return False 
    
    if( len(stack) == 0 ):
        return True 
    else:
        return False 
    



balancedBrackets('[][]'))
balancedBrackets('[][')
balancedBrackets('[]]')
balancedBrackets('[][()]')
balancedBrackets('[][{()}]')
balancedBrackets('][][]')
balancedBrackets('[][]][]')






