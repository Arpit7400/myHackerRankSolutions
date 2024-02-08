import sys
sys.set_int_max_str_digits(9999)
def extraLongFactorials(n):
    # Write your code here
    # result=1
    # value=n
    # while value!=1:
    #     result=result*value
    # return result
    if n == 0 or n == 1:
        return 1
    return n * extraLongFactorials(n-1)
print(extraLongFactorials(95))


