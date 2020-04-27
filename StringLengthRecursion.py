def length(str):
    if(str == ''):
        return 0
    return 1+length(str[1:])
print(length("Tarun Sharma"))