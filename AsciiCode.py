def counterpartCharCode(char):
    res = ord(char)
    
    if(res >= 65 and res<=90 ):
        res=res+32
        return res
    elif( res>=97 and res<=122 ):
        res=res-32
        return res
    else:
        return ord(char)    
            
        
print(counterpartCharCode('Z'))
print(counterpartCharCode('A'))
print(counterpartCharCode('a'))
print(counterpartCharCode('z'))



            

