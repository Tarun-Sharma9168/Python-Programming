def get_only_evens(nums):
 new_list=[]
 for i in range(len(nums)):
     if(i%2 == 0 and nums[i]%2==0):
         new_list.append(nums[i])
 return new_list        
print(get_only_evens([1, 3, 2, 6, 4, 8]))
print(get_only_evens([0, 1, 2, 3, 4]))
print(get_only_evens([1, 2, 3, 4, 5]) )         