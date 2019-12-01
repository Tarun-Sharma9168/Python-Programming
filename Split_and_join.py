def split_and_join(s):
    p=s.split(" ")
    s="-".join(p)
    return s
p=input()
result=split_and_join(p)
print(result)
