def permutationEquation(p):
    # Write your code here
    result=[]
    for i in range(1,n+1):
        for j in p:
            if i==p[j-1]:
                # print(j)
                for q in p:
                    if j==p[q-1]:
                        result.append(q)
    return result


n=5
p=[5,2,1,3,4]
permutationEquation(p,n)

