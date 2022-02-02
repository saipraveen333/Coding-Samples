
def nth_fibanocci(n):
    if n==2:
        return 1
    elif n==1:
        return 0
    else:
        return nth_fibanocci(n-1)+nth_fibanocci(n-2)

print(nth_fibanocci(7))
