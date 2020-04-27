def find_even_nums(num):
    vals=[value for value in range(2,num+1) if (value%2 == 0)]
    return vals
print(find_even_nums(10))
print(find_even_nums(20))
	