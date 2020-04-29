def split(txt):
 vowel="aeiou"
 s1=""
 s2=""
 for i in txt:
     if i in vowel:
         s1=s1+i
     else:
         s2=s2+i     
 return s1+s2
print(split("abcde"))
print(split("Hello!"))
print(split("What's the time?"))         
 