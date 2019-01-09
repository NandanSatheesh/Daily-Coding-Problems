# #7
# This problem was asked by Facebook
# 
# Given the mapping a = 1, b = 2, ... z = 26, 
# and an encoded message, 
# count the number of ways it can be decoded.
# 
# For example, 
# the message '111' would give 3, 
# since it could be decoded as 'aaa', 'ka', and 'ak'.
# 
# You can assume that the messages are decodable. For example, '001' is not allowed.
# 
# 


dict = { i: str(chr(96+i)) for i in range(1,27)}
dict

def codeIt(text , code):

    if( text == ''):
        if(code not in allCodes):
            allCodes.append(code)
            
            for i in code:
                print(dict.get(int(i)),end='')
            print()
            
            return
    
    if( int(text[0]) in range(1,27) ):
        codeIt(text[1:] , code + [text[0]])
        
    if(len(text) > 1 and (int(text[:2]) in range(1,27) ) ):
        codeIt(text[2:] , code + [text[:2]])

allCodes = []
codeIt('111',code=[])
print(allCodes)
print(len(allCodes))

# Output
# aaa
# ak
# ka
# [['1', '1', '1'], ['1', '11'], ['11', '1']]
# 3