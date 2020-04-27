def one_odd_one_even(n):
    ones_digit=n%10;
    n=n//10;
    second_digit=n%10;
    if((ones_digit+second_digit) & 1):
        return True
    else:
        return False;
print(one_odd_one_even(12))
print(one_odd_one_even(21))
print(one_odd_one_even(51))
    	