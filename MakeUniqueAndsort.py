def unique_sort(lst):
        
        lst=list(set(lst))
        lst.sort()
        return lst
print(unique_sort([6,5,4,3,5,4,1]))    