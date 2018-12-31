# 
# 
# This probelm was asked by Snapchat   
#   
# Given an array of time intervals (start, end)  
# for classroom lectures (possibly overlapping),  
# find the minimum number of rooms required.  
#   
# For example,   
# given [(30, 75), (0, 50), (60, 150)],  
# you should return 2.
# 
# 

def getClassesRequired(time):

    events = [] 
    for i in time:
        events.append([i[0],'start'])
        events.append([i[1],'end'])
    events.sort()
    classRequired = 0 
    maxClassRequired = 0 
    
    for i in events:
        if(i[1] == 'start'):
            classRequired += 1 
        elif(i[1] == 'end'):
            classRequired -= 1 
        
        if( classRequired > maxClassRequired):
            maxClassRequired = classRequired
        
    return maxClassRequired



timeIntervals = [(0,10),(2,12),(3,14)]
getClassesRequired(timeIntervals)

