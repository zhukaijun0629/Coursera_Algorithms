def sort_and_CountInv(A):
    # Base Case: if length of array A is 1, then no need to sort
    # Return A itself as the sorted array and 0 as the number of inversions happened
    if len(A) == 1:
        return A,0

    # Genearl Case: divide and conquer
    # Recursively split array A evenly into two arrays and sort separately
    # 1st half yields B as the sorted array and X as the number of inversions happened
    # 2nd half yields C as the sorted array and Y as the number of inversions happened
    # Then merge B&C to D as the final sorted array and Z as the number of inversions happened
    else:
        m = len(A) // 2
        B,X = sort_and_CountInv(A[:m])
        C,Y = sort_and_CountInv(A[m:])
        D,Z = merge_and_CountSplitInv(B,C)
    return D , X + Y + Z


def merge_and_CountSplitInv(B,C):
    # Merge two halves of the sorted arrays B and C
    # Everytime when the first number of C >= first number of B
    # THe number of inversions needs to add the length of the remaining array B
    D = []
    Z = 0
    while B and C:
        if B[0] < C[0]:
            D.append(B.pop(0))
        else:
            D.append(C.pop(0))
            Z += len(B)
    D.extend(B or C)
    return D,Z

####Load Data########
#A=[3,1,6,5,4,2]
A = []
with open ("IntegerArray.txt") as file:
    for line in file:
        A.append(int(line))

print(sort_and_CountInv(A)[1])
# 2407905288
