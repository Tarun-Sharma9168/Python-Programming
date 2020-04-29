def is_automorphic(n):
 square_number=n**2
 while(n):
     k=square_number%10
     t=n%10
     if(k!=t):
         return False
     n=n//10
     square_number=square_number//10
 return True     
print(is_automorphic(5))
print(is_automorphic(8))
print(is_automorphic(76))
   