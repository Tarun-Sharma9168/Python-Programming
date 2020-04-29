def count(deck):
 dict={2:1,3:1,4:1,5:1,6:1,7:0,8:0,9:0,10:-1,'J':-1,'Q':-1,'K':-1,'A':-1}
 count=0
 for i in deck:
     count=count+dict[i]
 return count    
print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
print(count(["A", "A", "K", "Q", "Q", "J"]))
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))