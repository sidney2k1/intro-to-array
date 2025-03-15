def minelement(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=min(temp,a[i])
    return temp
def maxelement(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=max(temp,a[i])
    return temp
a=[12,1234,235,43,89]
size=len(a)
print("smalllest element=",minelement(a,size))
print("largest element=",maxelement(a,size))
