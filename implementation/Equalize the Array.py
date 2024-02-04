def equalizeArray(arr):
    s=set(arr)
    count=[arr.count(i) for i in s]
    result=len(arr)-max(count)
    return result

