def partition(a,si,ei):
    i=si+1
    key=a[si]
    j=ei
    while(i<=j):
        while(i<=ei and a[i]<=key):
            i+=1
        while(j>si and a[j]>key):
            j-=1
        if(i<j):
            a[i],a[j]=a[j],a[i]
    if(i>j):
        a[j],a[si]=a[si],a[j]
        return j
def quicksort(a,si,ei):
    if(si<=ei):
        j=partition(a,si,ei)
        quicksort(a,si,j-1)
        quicksort(a,j+1,ei)
a=list(map(int,input().split()))
quicksort(a,0,len(a)-1)
print(*a)
