def greet_people(names):
 s=""
 comma=len(names)-1
 for i in names:
     s=s+"Hello "+i
     for k in range(comma):
         s=s+','
         comma=comma-1
         break
 return s        
print(greet_people(["Joe"]))
print(greet_people(["Angela", "Joe"]))
print(greet_people(["Frank", "Angela", "Joe"]))          
     