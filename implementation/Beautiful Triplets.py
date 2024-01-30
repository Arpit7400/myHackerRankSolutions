def beautifulTriplets(d, arr):
    count=0
    for i in arr:
        for j in arr:
            if i<j and j-i==d:
                for k in arr:
                    if j<k and k-j==d:
                        count+=1
    return count