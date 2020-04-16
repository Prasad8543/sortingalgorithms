def selectionsort(a,n):
    for i in range(n-1):
        min=a[i]
        pos=i
        for j in range(i,n):
            if(a[j]<min):
                min=a[j]
                pos=j
        a[i],a[pos]=a[pos],a[i]
a=[4,5,2,3,1]
n=5
selectionsort(a,n)
print(*a)