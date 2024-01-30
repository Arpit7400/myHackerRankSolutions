def appendAndDelete(s, t, k):
    count=0
    for i in range(min(len(s),len(t))):
        if s[i]!=t[i]:
            ss=s[i:]
            tt=t[i:]
            count+=len(ss)+len(tt)
            break
    if len(s)!=len(t) and count==0:
        count=max(len(s),len(t))-min(len(s),len(t))
    if count<=k and len(s)>=len(t) :
        return "Yes"
    elif count<=k and set(list(s))==set(list(t)):
        return "Yes"
    else:
        return "No"
    
print(appendAndDelete("y","yu",))
