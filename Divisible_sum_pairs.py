def divisibleSumPairs(n, k, ar):
    # Write your code here
    result = 0
    for i in range(n):
        for j in range(n):
            if i<j and (ar[i]+ar[j])%k==0:
                result+=1
    return result

