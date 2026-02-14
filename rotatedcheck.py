# def checkRotated(s:str,t:str)->bool:
#     n=len(s)
#     if len(s)!=len(t):
#         return False
#     for i in range(len(s)):
#         rotated=s[i:]+s[:i]
#         if rotated==t:
#             return True
    
#     return False
    
def checkRotated(s:str,t:str)->bool:
    n=len(s)
    double=s+s
    if len(s)!=len(t):
        return False
    return t in double
    
    
s="rotation"
t="tionrotw"
print(checkRotated(s,t))