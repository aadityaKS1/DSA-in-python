# def checkAnagram(s:str,t:str)->bool:
#     if len(s)!=len(t):
#         return False
#     if sorted(s)==sorted(t):
#         return True
#     return False
# optimal
def checkAnagram(s:str,t:str)->bool:
    if len(s)!=len(t):
        return False
    m=[0]*26
    for char in s:
        m[ord(char)-ord('A')]+=1
    for char in t:
        m[ord(char)-ord('A')]-=1
    for count in m:
        if count!=0:
            return False
    return True   
        
        
        
s="ABCDEF"
t="BCEFMD"
print(checkAnagram(s,t))     