def cutTheSticks(arr):
    lst=arr[:]
    result=[]
    while len(lst)!=0:
        result.append(len(lst))
        var =[]
        minn=min(lst)
        for i in lst:
            a=i-minn
            if a>0:
                var.append(a)
        lst=var[:]
    return result

print(cutTheSticks([5,4,4,2,2,8]))