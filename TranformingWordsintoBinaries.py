def convert_binary(string):
    string =string.lower()
    s=''
    for i in string:
        if(i >= 'a' and i<='m'):
            s=s+'0'
        elif(i >='n' and i<='z'):
            s=s+'1'    
    return s 
print(convert_binary("house") )
print(convert_binary("excLAIM"))
print(convert_binary("moon"))        
              