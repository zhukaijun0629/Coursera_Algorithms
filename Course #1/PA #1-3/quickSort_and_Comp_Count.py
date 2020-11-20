def quickSort_First(A):
    if len(A) <= 1:
        return A,0
    else:
        p = A[0]
        A,Count1,p1 = partition(A,0,len(A))
        B,Count2 = quickSort_First(A[:p1])
        C,Count3 = quickSort_First(A[p1+1:])
        return B+[p]+C , Count1+Count2+Count3

def quickSort_Last(A):
    if len(A) <= 1:
       return A,0
    else:
       p = A[-1]
       A[0],A[-1] = A[-1],A[0]
       A,Count1,p1 = partition(A,0,len(A))
       B,Count2 = quickSort_Last(A[:p1])
       C,Count3 = quickSort_Last(A[p1+1:])
       return B+[p]+C , Count1+Count2+Count3

def quickSort_Medium(A):
    if len(A) <= 1:
       return A,0
    else:
        p0 = get_Medium_Index(A)
        p = A[p0]
        A[0],A[p0] = A[p0],A[0]
        A,Count1,p1 = partition(A,0,len(A))
        B,Count2 = quickSort_Medium(A[:p1])
        C,Count3 = quickSort_Medium(A[p1+1:])
        return B+[p]+C , Count1+Count2+Count3

def get_Medium_Index(A):
    if (A[0]-A[(len(A)-1)//2]) * (A[0]-A[(len(A)-1)]) < 0:
        return 0
    elif (A[(len(A)-1)//2]-A[0]) * (A[(len(A)-1)//2]-A[(len(A)-1)]) < 0:
        return (len(A)-1)//2
    else:
        return len(A)-1


def partition(A,l,r):
    Count = 0
    p = A[l]
    i = l + 1
    for j in range(l+1,r):
        if A[j] < p:
            A[j],A[i] = A[i],A[j]
            i += 1
        Count += 1
    A[l],A[i-1] = A[i-1],A[l]
    return A,Count,i-1

####Load Data########
# A=[3,8,2,5,1,4,7,6]
# A=[8,3,1,2,5,4,7,6]
A=[]
with open ('QuickSort.txt') as file:
    for line in file:
        A.append(int(line))

import copy

print(quickSort_First(copy.deepcopy(A))[1]) # 162085
print(quickSort_Last(copy.deepcopy(A))[1]) # 164123
print(quickSort_Medium(copy.deepcopy(A))[1]) # 138382
