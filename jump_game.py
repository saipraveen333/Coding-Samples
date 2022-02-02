def min_jump(arr):
    def min_jump1(arr, ele, i):
        if i == len(arr) - 1:
            return True
        if i > len(arr) - 1:
            return
        for k in range(ele, 0, -1):
            if min_jump1(arr, arr[k], i + k) == True:
                return True
        return False
    return min_jump1(arr, arr[0], 0)
arr=[2,3,0,1,4]

print(min_jump(arr))
