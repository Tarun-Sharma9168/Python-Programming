lst=[]
lst_new=[]
one_more=[]
n=int(input())
m=int(input())

for i in range(0,m):
    ele=int(input())
    lst.append(ele)
if(n==m):
    print(0)
    for i in range(0,n+1):
        
       for i in range(0,m+1):
          lst_new.append(i-lst[i])
     finding_min=min(lst_new)   
     one_more.append(finding_min)
answer=max(one_more)



