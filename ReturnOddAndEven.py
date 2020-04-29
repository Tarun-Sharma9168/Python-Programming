def odds_vs_evens(num):
 sum_odd=0
 sum_even=0
 while(num):
     p=num%10
     if(p & 1 ):
         sum_odd=sum_odd+p
     else:
         sum_even=sum_even+p
     num=num//10
 if(sum_odd > sum_even):
     return "odd"
 elif(sum_even > sum_odd):
     return "even"
 else:
     return "equal"
 
print(odds_vs_evens(97428))
print(odds_vs_evens(81961))
print(odds_vs_evens(54870)) 
 
             