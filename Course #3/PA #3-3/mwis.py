def mwis(wts):
    mw = [0] * len(wts)
    mw[1] = wts[1]
    for i in range(len(wts)):
        if i == 0 or i == 1:
            continue
        mw[i] = max(mw[i-1], wts[i]+mw[i-2])

    # print(mw)
    maxWtIndSet = []
    j = len(mw) - 1
    while j >= 1:
        if mw[j-1] < (mw[j-2] + wts[j]):
            maxWtIndSet.append(j)
            j -= 2
        else:
            j -= 1
    return maxWtIndSet

#########Load File
wts = [0]
file=open('mwis.txt')
data=file.readlines()
for i,line in enumerate(data):
    if i == 0:
        continue
    wts.append(int(line.strip()))

maxWtIndSet = mwis(wts)

res = ''
for i in [1,2,3,4,17,117,517,977]:
    if i in maxWtIndSet:
        res += '1'
    else:
        res += '0'

print(res) #10100111
