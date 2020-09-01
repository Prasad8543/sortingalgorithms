def shellsort(a,n):
    gap=n//2
    while(gap>=1):
        for j in range(gap,n,1):
            for i in range(j-gap,-1,-gap):
                if(a[i+gap]>a[i]):
                    break
                else:
                    a[i+gap],a[i]=a[i],a[i+gap]
        gap=gap//2
a=list(map(int,input().split()))
shellsort(a,len(a))
print(*a)