def serviceLane(width, cases):
    # Write your code here
    # result = []
    # for i in cases:
    #     a=n[i[0]:i[1]+1]
    #     result.append(min(a))
    result = [min(width[i[0]:i[1]+1]) for i in cases]
    return result

width=[1,2,2,2,1]
cases=[[2, 3], [1,4], [2,4], [2,4], [2,3]]
print(serviceLane(width,cases))