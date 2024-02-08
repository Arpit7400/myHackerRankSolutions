def findDigits(n):
    # Write your code here
    lst=[]
    count=0
    for i in str(n):
        if int(i)!=0:
            lst.append(int(i))
    for i in lst:
        if n%i==0:
            count+=1
    return count

print(findDigits(12))