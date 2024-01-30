def circularArrayRotation(a, k, queries):
    # Write your code here
    if k>len(a):
        k=k%len(a)
        lst=a[len(a)-k:]+a[:len(a)-k]
        result=[]
        for i in queries:
            result.append(lst[i])
        return result
    else:
        lst=a[len(a)-k:]+a[:len(a)-k]
        result=[]
        for i in queries:
            result.append(lst[i])
        return result
        





a=[1,2,3]
k=2
queries=[0,1,2]
sd =circularArrayRotation(a, k, queries)
print(sd)