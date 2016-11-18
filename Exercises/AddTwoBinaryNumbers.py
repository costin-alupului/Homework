A=[1,0,1,1,0,1,1]
B=[1,1,1,0,1,1,1]
C=[0,0,0,0,0,0,0,0]

remainder=0
for i in range(len(A)-1,-1,-1):
    #print i, A[i], B[i], A[i]+B[i]+remainder,((A[i]+B[i]+remainder)%2) 
    C[i+1]=(A[i]+B[i]+remainder)%2
    remainder=(A[i]+B[i]+remainder)/2
C[0]=remainder
print "  ",A
print "  ",B
print C
    