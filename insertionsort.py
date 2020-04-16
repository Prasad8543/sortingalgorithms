def insertionsort(a,n):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while(j>=0 and key<a[j]):
            a[j],a[j+1]=a[j+1],a[j]
            j-=1
        a[j+1],key=key,a[j+1]
a=[5,6,2,10,1,4,8,9,7,3]
n=10
insertionsort(a,n)
print(*a)