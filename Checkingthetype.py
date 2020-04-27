def reverse(arg):
      if(type(arg) == bool):
          return not(arg)
      else:
          return ("boolean expected") 	
print(reverse(True))
print(reverse(1))    
print(reverse("Sachin"))      