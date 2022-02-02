def non_overlap_interval(arr):
    arr=sorted(arr)
    def rem_overlap(arr, i, count):
        while arr[i][1] <= arr[i + 1][0] and i != len(arr) - 1:
            i += 1
            if i == len(arr) - 1:
                return count
        arr.pop(i + 1)
        count += 1
        return rem_overlap(arr, i, count)
    return rem_overlap(arr,0,0),arr
print(non_overlap_interval(([[3,4],[8,9],[4,5],[6,7],[4,6],[3,5],[1,2],[2,3],[1,3]])))