def Strings_become_mutable(s,position,character):
    make_into_list=list(s)
    make_into_list[position]=character
    p="".join(make_into_list)
    return p
input_string=input()
p,c=input().split()
result=Strings_become_mutable(input_string,int(p),c)
print(result)
