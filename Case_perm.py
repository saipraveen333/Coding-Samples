def letterCasePermutation(s):
    output=['']
    for i in range(len(s)):
        c=[]
        for j in range(len(output)):
            if s[i].isdigit():
                c.append(output[j]+s[i])
            else:
                c.append(output[j]+s[i].lower())
                c.append(output[j]+s[i].upper())
        output=c
    return output

print(letterCasePermutation('3zh'))

def letterCasePermutation(s):
    if s.isnumeric():
        return [s]
    if len(s)==1:
        return [s,s.upper()]
    val=letterCasePermutation(s[1:])
    l=[]
    first=s[0]
    for i in val:
        if first+i not in l:
            l.append(first+i)
            l.append(first.upper()+i)
    return l
print(letterCasePermutation('1'))
