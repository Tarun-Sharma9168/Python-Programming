def is_in_order(txt):
 old_list=list(txt)
 new_list=sorted(txt)
 
 if new_list == old_list:
     return True
 else:
     return False
print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))
print(is_in_order("xyzz")) 