def steps_to_convert(txt):
 count_upper=0
 count_lower=0
 for i in txt:
     if(i.islower()):
         count_lower=count_lower+1
     else:
         count_upper=count_upper+1
 ans=min([count_lower,count_upper]) 
 return ans
print(steps_to_convert("abC"))
print(steps_to_convert("abCBA"))
print(steps_to_convert("aba"))
print(steps_to_convert("abaCCC"))         
         
         
        
	