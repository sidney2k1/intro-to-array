def print2largest(a,a_size):
    largest=secondlargest=21435678
    for i in range(a_size):
        if a[i]>largest:
            secondlargest=largest
            largest=a[i]
        elif a[i]>secondlargest and a[i]!=largest:
            secondlargest=a[i]
    print(secondlargest)
a=[1,2,3,4,5,6,7,8,9]
a_size=len(a)
print("secondlargest number=",print2largest(a,a_size))
