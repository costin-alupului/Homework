A=[5,2,4,6,1,3]
print A

for i in range(0,len(A)):
    minIndex=i
    for j in range(i,len(A)):
        if (A[j]<A[minIndex]):
            minIndex=j
    tmp=A[i]
    A[i]=A[minIndex]
    A[minIndex]=tmp
    print A