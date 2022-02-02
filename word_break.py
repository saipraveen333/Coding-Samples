input1 = 'ilikeicecreamandmango'
def wor_brk(input1,d):
    s=''
    l=[]
    def wor_brk2(input,s):
        for i in range(len(input)):
            for j in range(len(input)-1,-1,-1):
                if checker(input[i:j+1]):
                    if input[i:j+1] not in l:
                        l.append(input[i:j + 1])
                        wor_brk2(input[j + 1:], '')
    def checker(word):
        if word in d:
            return True
    wor_brk2(input1,s)
    return l
d = {"i", 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'}


print(wor_brk(input1,d))