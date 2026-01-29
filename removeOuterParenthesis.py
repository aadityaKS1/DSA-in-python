def removeOuterParanthesis(s:str)->str:
    ans=""
    level=0
    for ch in s:
        if ch=="(":
            if level>0 :
                ans+=ch
            level+=1
        if ch==")":
            level-=1
            if level>0:
                ans+=ch
    return ans

st="(()()())"

print(removeOuterParanthesis(st))