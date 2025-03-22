def reversearray(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[1,2,3,4,5,6,7,8,9]
size=len(arr)
print("original array:")
print(arr)
print("Reversed array:",reversearray(arr,0,size-1))
print(arr)