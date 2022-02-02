import math

def prime(n):
    for i in range(2,n):
        j=2
        not_prime=False
        sqroot = int(math.sqrt(n))
        while j<=sqroot:
             if i%j==0:
                not_prime=True
                break
             j=j+1
        if not_prime==False:
            print(i)
prime(20)




def nthprime(N):
    num=1
    count=0
    while(True):
        num=num+1
        if prime(num):
            count=count+1
        if count==N:
            break
    return num
#print(nthprime(10))






