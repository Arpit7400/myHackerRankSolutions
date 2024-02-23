import math
def pickingNumbers(a):
    a_set =sorted(set(a))
    result =0
    if len(a)!=len(a_set):
        for i in a_set:
            if a.count(i)>=1 and a.count(i+1)>0:
                count=(a.count(i)+a.count(i+1))
                if result<count:
                    result=count
    if len(a)>=100 and len(a_set)<=4:
        for i in a_set:
            count=a.count(i)
            if result<count:
                result=count
    return result



# a = [4,6,5,3,3,1]
# a = [1,2,2,3,1,2]
# a = [98,3,99,1,97,2]
a = [4,97,5,97,97,4,97,4,97,97,97,97,4,4,5,5,97,5,97,99,4,97,5,97,97,97,5,5,97,4,5,97,97,5,97,4,97,5,4,4,97,5,5,5,4,97,97,4,97,5,4,4,97,97,97,5,5,97,4,97,97,5,4,97,97,4,97,97,97,5,4,4,97,4,4,97,5,97,97,97,97,4,97,5,97,5,4,97,4,5,97,97,5,97,5,97,5,97,97,97]
#,a.split(" ")
# print(a.split())
print(pickingNumbers(a))