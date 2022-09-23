def algorithm_1(array):                             #Algorithm 1
    maxSoFar = 0
    for l in range(len(array)):
        for u in range(l, len(array)):
            sum = 0
            for i in range(l, u+1):
                sum += array[i]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar

def algorithm_2(array):                             #Algorithm 2
    maxSoFar = 0
    for x in range(len(array)):
        sum = 0
        for u in range(x, len(array)):
            sum += array[u]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar

def maxSum(array, L, U):                            #Algorithm 3
    if L > U:
        return 0
    if L == U:
        return max(0, array[L])
    M = int((L+U)/2)
    sum, maxToLeft, step = 0, 0, -1
    for I in range(M, L-1, step):
        sum += array[I]
        maxToLeft = max(maxToLeft, sum)
    sum, maxToRight = 0, 0
    for I in range(M+1, U+1):
        sum += array[I]
        maxToRight = max(maxToRight, sum)
    maxCrossing = maxToLeft + maxToRight

    maxInA = maxSum(array, L, M)
    maxInB = maxSum(array, M+1, U)
    return max(maxCrossing, maxInA, maxInB)

def algorithm_4(array):                             #Algorithm 4
    maxSoFar = 0
    maxEndingHere = 0
    for I in range(0, len(array)):
        maxEndingHere = max(0, maxEndingHere+array[I])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar