import sys                                      
height = int(sys.stdin.readline())              
counter = 1                                     
shrinking = False                               
for i in range(height):                         
    a = '*' * counter                           
    space = " " * ((height * 2) - (2 * len(a))) 
    print(a + space + a)                        
    if space == '':                             
        shrinking = True                        
    if shrinking:                               
        counter -= 2                            
    else:                                       
        counter += 2                            
