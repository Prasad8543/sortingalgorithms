def bubblesort(a,n):
    swap=1
    j=1
    while(swap!=0 and j<n):
        swap=0
        for i in range(n-j):
            if(a[i]>=a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]
                swap=1
        j+=1
a=[5,3,4,2,1]
n=5
bubblesort(a,n)
print(*a)