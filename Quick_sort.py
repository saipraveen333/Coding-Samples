from collections import deque
a=[2,6,7,6,4,6,9,8,6,7,9,8,6]
def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()
    i = []
    j = []
    for k in a:
        if k < pivot:
            i.append(k)
        else:
            j.append(k)
    return quick_sort(i) + [pivot] + quick_sort(j)
print(quick_sort(a))
