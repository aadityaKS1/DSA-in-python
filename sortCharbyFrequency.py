
# words=['apple','banana','cat']

# new_list=words.sort()
# print(words)
# print(new_list)


# pairs = [(2,'b'), (1,'a'), (3,'c')]
# pairs.sort()
# print(pairs)


# d={'b':12,'a':3,'c':4}
# d_new=sorted(d.items(),key=lambda x:x[1])
# print(d_new)


# sett={5,1,3}
# print(sorted(sett))



def sortCharbyFreq(s:str)->str:
    #storing frequency and character list of tuples
    freq=[(0,chr(i+ord('a'))) for i in range(26)]
    
    #counting the frequncy of each chareacter
    for ch in s:
        index=ord(ch)-ord('a')
        freq[index]=(freq[index][0]+1,ch)
    #sorting 
    freq.sort(key=lambda x:(-x[0],x[1]))
    
    #colleing non zero character
    result=[]
    # for  item in freq:
    #     f=item[0]
    #     ch=item[1]
    #     if f>0:
    #         result.append(ch)
    # return result
    
    for f,ch in freq:
        if f>0:
            result.append(ch)
    return result

word='tree'

print(sortCharbyFreq(word))