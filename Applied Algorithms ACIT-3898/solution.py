def our_shared_values(left, right):
    shared = []
    leftdict = {}
    rightdict = {}
    for item in list(set(left)):
        leftdict[item] = left.count(item)
    for item in list(set(right)):
        rightdict[item] = right.count(item)
    finaldict =  {k:min(leftdict[k],rightdict[k]) for k in leftdict if k in rightdict}
    for item in finaldict:
        temp = [item] * finaldict[item]
        shared.extend(temp)
    return shared
