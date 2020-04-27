def count_ones(num):
    one=1
    count=0
    while(num):
        if(num & 1):
            count=count+1
        num=num>>1
        one=one<<1    
    return count  
print(count_ones(2))
print(count_ones(7))    	