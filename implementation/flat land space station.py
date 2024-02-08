# def flatlandSpaceStations(n, c):
#     if n == len(c):
#         return 0
#     c = sorted(c)
#     ans = []
#     for i,x in enumerate(c):
#         if i+1 < len(c):
#             if i == 0:
#                 left_dif = x
#                 right_dif = (c[i+1] - x)//2
#                 ans.append(max(left_dif, right_dif)) 
#             else:
#                 left_dif = (x - c[i-1])//2
#                 right_dif = (c[i+1] - x)//2
#                 ans.append(max(left_dif, right_dif)) 
#         elif len(c) == 1:
#             left_dif = x
#             right_dif = n - x - 1
#             ans.append(max(left_dif, right_dif)) 
#         else:
#             left_dif = (x - c[i-1])//2
#             right_dif = n - x - 1
#             ans.append(max(left_dif, right_dif)) 
#     return max(ans)


def flatlandSpaceStations(n, c):
    c.sort()
    value=max(c[0]-0,n-c[-1]-1)
    for i in range(1,len(c)):
        value=max(value,(c[i]-c[i-1])//2)
    return value
print(flatlandSpaceStations(5,[0,1,2,4,3,5]))