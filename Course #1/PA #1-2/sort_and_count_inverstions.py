def Sort_and_CountInv(A):
    if len(A)==1:
        return A,0
    else:
        m=len(A)//2
        B,X=Sort_and_CountInv(A[:m])
        C,Y=Sort_and_CountInv(A[m:])
        D,Z=Merge_and_CountSplitInv(B,C)
    return D,X+Y+Z


def Merge_and_CountSplitInv(B,C):
    D=[]
    Z=0
    while B and C:
        if B[0]<C[0]:
            D.append(B.pop(0))
        else:
            D.append(C.pop(0))
            Z+=len(B)
    D.extend(B or C)
    return D,Z

#A=[3,1,6,5,4,2]
A=[]
with open ("ints.txt") as file:
    for line in file:
        A.append(int(line))



print(Sort_and_CountInv(A)[1])
