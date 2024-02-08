def jumpingOnClouds(c,n):
    count=0
    position=1
    while position != n:
        k=c[position:]
        if len(k)>=2 and k[1]==0:
            position+=2
            count+=1
        elif k[0]==0:
            position+=1
            count+=1
    return count

s=[0,0,0,1,0,0]
print(jumpingOnClouds(s,6))