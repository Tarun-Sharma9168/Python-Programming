def can_alternate(s):
 count_0=0
 count_1=0
 for i in s:
     if(i == "0"):
         count_0=count_0+1
     else:     
         count_1=count_1+1
     
     
 if((len(s) % 2) !=0):
         if(abs(count_0 -count_1)==1):
             return True
 else:
         if(abs(count_0 -count_1) ==0):
             return True
 return False        
     
         

print(can_alternate("0001111"))
print(can_alternate("01001"))
print(can_alternate("010001"))   
print(can_alternate("1111"))             
                     
     
       