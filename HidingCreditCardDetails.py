#only showing the last four digits
def card_hide(card):
 s=''
 for i in range(len(card)):
     if(len(card)-i >4):
         s=s+'*'
     else:
         s=s+card[i]    
 return s    
print(card_hide("1234123456785678"))
print(card_hide("8754456321113213"))
print(card_hide("35123413355523"))
	