def amplify(num):
    new_list=[]
    for i in range(num+1):
        if(i % 4 ==0):
            new_list.append(10*(i))
        else:
            new_list.append(i)
    new_list.remove(0)        
    return new_list 
print(amplify(4)) 
print(amplify(3))
print(amplify(25))          
            
	