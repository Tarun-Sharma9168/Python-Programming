def find_odd(lst):
    new_set=set(lst)
    
    for i in new_set:
        pp=lst.count(i)
        if(pp & 1):
            return i
print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))        
	