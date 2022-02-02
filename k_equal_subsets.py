arr=[2,1,4,5,6]
def k_equal_subsets1(arr,k):
    div_sum = sum(arr) // k
    r = []
    def k_equal_subsets(arr, div_sum, l):
        if sum(l) == div_sum:
            r.append(l.copy())
            return
        elif sum(l) > div_sum:
            return
        for i in range(len(arr)):
            l.append(arr[i])
            k_equal_subsets(arr[i+1:], div_sum, l)
            l.pop()
    k_equal_subsets(arr, div_sum, [])
    return r
print(k_equal_subsets1(arr,3))

