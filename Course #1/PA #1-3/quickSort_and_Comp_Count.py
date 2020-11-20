# def QuickSort(A,p0):
#    if len(A)==1:
#        return A,0
#    else:
#        p=A[p0]
#        A,Count1,p1=Partition(A,0,len(A))
#        B,C=[],[]
#        Count2,Count3=0,0
#        if p1>0:
#            B,Count2=QuickSort(A[:p1],p0)
#        if p1<len(A)-1:
#            C,Count3=QuickSort(A[p1+1:],p0)
#        return B+[p]+C,Count1+Count2+Count3

def QuickSort_First(A):
    if len(A)==1 or len(A)==0:
        return A,0
    else:
        p=A[0]
        A,Count1,p1=Partition(A,0,len(A))
        B,Count2=QuickSort_First(A[:p1])
        C,Count3=QuickSort_First(A[p1+1:])
        return B+[p]+C,Count1+Count2+Count3

def QuickSort_Last(A):
    if len(A)==1 or len(A)==0:
       return A,0
    else:
       p=A[-1]
       A[0],A[-1]=A[-1],A[0]
       A,Count1,p1=Partition(A,0,len(A))
       B,Count2=QuickSort_Last(A[:p1])
       C,Count3=QuickSort_Last(A[p1+1:])
       return B+[p]+C,Count1+Count2+Count3

def QuickSort_Medium(A):
    if len(A)==1 or len(A)==0:
       return A,0
    else:
        p0=Get_Medium_Index(A)
        p=A[p0]
        A[0],A[p0]=A[p0],A[0]
        A,Count1,p1=Partition(A,0,len(A))
        B,Count2=QuickSort_Medium(A[:p1])
        C,Count3=QuickSort_Medium(A[p1+1:])
        return B+[p]+C,Count1+Count2+Count3

def Get_Medium_Index(A):
    if (A[0]-A[(len(A)-1)//2])*(A[0]-A[(len(A)-1)])<0:
        return 0
    elif (A[(len(A)-1)//2]-A[0])*(A[(len(A)-1)//2]-A[(len(A)-1)])<0:
        return (len(A)-1)//2
    else:
        return len(A)-1


def Partition(A,l,r):
    Count=0
    p=A[l]
    i=l+1
    for j in range(l+1,r):
        if A[j]<p:
            A[j],A[i]=A[i],A[j]
            i+=1
        Count+=1
    A[l],A[i-1]=A[i-1],A[l]
    return A,Count,i-1

# A=[3,8,2,5,1,4,7,6]
# A=[8,3,1,2,5,4,7,6]
A=[]
with open ('QuickSort.txt') as file:
    for line in file:
        A.append(int(line))


# print(Partition(A,0,8))
# print(QuickSort_First(A)[1])
# print(QuickSort_Last(A)[1])
print(QuickSort_Medium(A)[1])
