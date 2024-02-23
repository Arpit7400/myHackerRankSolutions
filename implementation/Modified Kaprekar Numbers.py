def kaprekarNumbers(p, q):
    # Write your code here
    lst=[]
    for i in range(p,q+1):
        s=i**2
        s=str(s)
        l=len(str(i))
        if len(s)!=1:
            if (l-1)==0:
                _1=int(s[0])
                _2=int(s[1])
            else:
                _1=int(s[:l])
                _2=int(s[l:])
            f=_1+_2
        # f=eval((_1)+(_2))
            if f==i:
                lst.append(i)
    if len(lst)==0:
        return "INVALID RANGE"
    else:
        return lst
    

print(kaprekarNumbers(45,100))