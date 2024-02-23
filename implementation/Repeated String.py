def repeatedString(s, n):
    # Write your code here
    l=n//len(s)
    var = s.count('a')
    if n==l:
        result = var*n
        return result
    else:
        var1 = s[:n%len(s)].count('a')
        result = (var*l)+var1
        return result

print(repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm",736778906400))