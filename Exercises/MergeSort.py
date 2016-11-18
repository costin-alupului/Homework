A=[2,65,4,7,23,5,1,20,3,2,6,10]

def merge(A,p,q,r):
    L=A[p:q+1]
    R=A[q+1:r+1]
#     L[len(L)-1]=65535
#     R[len(R)-1]=65535
    L.append(65535)
    R.append(65535)
    j=0
    i=0
#     print 'Merge:'
#     print L, R, len(L), len(R)
    for k in range(p,r+1):
        if L[i]>R[j]:
            A[k]=R[j]
            j+=1
        else:
            A[k]=L[i]
            i+=1 
    return

def mergeSort(A,p,r):
#     print A[p:r+1]
#     print p, r
    if p==r:
        return
    else:
        q=(r+p)/2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
        
mergeSort(A,0,len(A)-1)
print A