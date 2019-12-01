#!/bin/python3
# Complete the pangrams function below.

def pangrams(s):
    new_set=set()
    for i in s:
        if(i.lower() in new_set or i.upper() in new_set):
            pass   
        else: 
           new_set.add(i)
   # print(new_set)    
    if(len(new_set) == 27):
       print("pangram")
    else:
       print("not pangram")            

s = input()

pangrams(s)
