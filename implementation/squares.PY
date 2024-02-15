def squares(a, b):
    # Write your code here
    lst = [i for i in range(int(a**0.5),int(b**0.5)+1)]
    result = [i for i in lst if i**2>=a and i**2<=b]
    return len(result)


print(squares(3,9))