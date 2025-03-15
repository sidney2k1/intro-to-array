def arraymean(arr,arr_size):
    totalsum=0
    for i in range(0,arr_size):
        totalsum+=arr[i]
    return float(totalsum/arr_size)
def arraymedian(arr,arr_size):
    sorted(arr)
    if arr_size%2!=0:
        return float(arr[int(arr_size/2)])
    
    return float((arr[int((arr_size-1)/2)]+arr[int(arr_size/2)])/2.0)
arr=[1,4,7,5,9,8,6,2]
arr_size=len(arr)
print("mean=",arraymean(arr,arr_size))
print("median=",arraymedian(arr,arr_size))
