vowel="aeiou"
def count_vowels(txt):
     count=0;
     for i in txt:
         if i in vowel:
             count=count+1
     return count 
print(count_vowels('Palm'))
print(count_vowels('amma'))        

	