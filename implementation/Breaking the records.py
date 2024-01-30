def breakingRecords(scores):
    # Write your code here
    n = len(scores)
    minimun = scores[0]
    values_minimun = 0
    maximum = scores[0]
    values_maximum = 0
    for i in scores:
        if i<minimun:
            minimun = i
            values_minimun += 1
        if i>maximum:
            maximum = i
            values_maximum += 1
    return values_maximum,values_minimun



scores = [3,4,21,36,10,28,35,5,24,42]
print(breakingRecords(scores))


