from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    ans=[]
    strs.sort()
    first=strs[0]
    last=strs[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return ''.join(ans)
        ans.append(first[i])

    return ''.join(ans)
input_strs = ["interview", "internet", "internal", "interval"]
print(longestCommonPrefix(input_strs))