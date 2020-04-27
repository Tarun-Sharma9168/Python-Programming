def missing_num(lst):
	#sum=(10*(10+1))//2;new_sum=0
    new_sum=0
    for i in lst:
        new_sum=new_sum+i
    sum=(10*11)//2
    return abs(new_sum-sum)
print(missing_num([1,2,3,4,5,6,7,8,10]))    
        
         
    
    
    