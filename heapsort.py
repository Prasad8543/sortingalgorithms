def heapify(a,n,i):
    parent=i
    left=2*i+1
    right=2*i+2
    if(left<n and a[left]>a[parent]):
        parent=left
    if(right<n and a[right]>a[parent]):
        parent=right
    if(i!=parent):
        a[i],a[parent]=a[parent],a[i]
        heapify(a,n,parent)
def heapsort(a,n):
    for i in range(n//2,-1,-1):
        heapify(a,n,i)
    for j in range(n-1,-1,-1):
        a[j],a[0]=a[0],a[j]
        heapify(a,j,0)
a=list(map(int,input().split()))
heapsort(a,len(a))
print(*a)