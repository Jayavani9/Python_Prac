Easy way to reverse a string in Python 

def revStr(str):
    return str[::-1]
    ''' 
    res = ""
    for i in range(len(str)-1, -1,-1):
        res += str[i]
    return res
    '''


ans = revStr("Hello, Beautyyyy!!!")
print(ans)
