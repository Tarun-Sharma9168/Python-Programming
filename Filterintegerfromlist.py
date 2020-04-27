def filter_list(l):
 new_list=[]
 for i in l:
    if(type(i) == int):
        new_list.append(i)
 return new_list
print(filter_list([1, 2, 3, "a", "b", 4]))       
print(filter_list(['A', 0, 'Edabit', 1729, 'Python', '1729']))
print(filter_list(['Nothing', 'here']))
        
         