import textwrap

def wrap(string, max_width):
    split = 0
    l = len(string)
    result = ""
    while split <= l:
        result += string[split:split+max_width]+"\n"
        split+=max_width
    return result

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4))
