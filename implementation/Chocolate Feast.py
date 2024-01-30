#Chocolate Feast
def chocolateFeast(n, c, m):
    # Write your code here
    # k= n//c
    # s= k//m
    # if s-m>0:
    #     l=k%m
    #     q=(s+l)%m
    #     count=k+s+l+q
    # else:
    #     p=((k%m)+s)//m
    #     count=k+s+p
    count=0
    while n>=c:
        n-=c
        count+=1
        if count%m==0:
            count+=1
    return count

print(chocolateFeast(84223, 76506, 29699))