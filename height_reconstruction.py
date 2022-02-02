arr=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
l=[]
def height_reconstruction(arr):
    arr=sorted(arr,key=lambda x:(-x[0],x[1]))
    for i in arr:
        l.insert(i[1],i)
    return arr
print(height_reconstruction(arr))

