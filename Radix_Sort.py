def counting_sort(a,n,p):
    count=[0 for i in range(10)]
    b=[0 for i in range(n)]
    for i in range(n):
        count[(a[i]//p)%10]+=1
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    for i in range(n-1,-1,-1):
        count[(a[i]//p)%10]-=1
        b[count[(a[i]//p)%10]]=a[i]
    for i in range(n):
        a[i]=b[i]
def radix_sort(a,n):
    m=max(a)
    m1=min(a)
    for i in range(n):
        a[i]+=abs(m1)
    pos=1
    while(m/pos>0):
        counting_sort(a,n,pos)
        pos*=10
    for i in range(n):
        a[i]-=abs(m1)
a=list(map(int,input().split()))
radix_sort(a,len(a))
print(*a)
