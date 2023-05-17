# My first solution

def fourNumberSum(array, targetSum):
    hashMap = []
    ans = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            hashMap.append([array[i], array[j]])
    for k in range(len(hashMap) - 1):
        for l in range(k + 1, len(hashMap)):
            firstPair = hashMap[k]
            secondPair = hashMap[l]
            first = firstPair[0]
            second = firstPair[1]
            third = secondPair[0]
            fourth = secondPair[1]
            if first != third and first != fourth and second != third and second != fourth: 
                quadrupletSum = hashMap[k][0] + hashMap[k][1] + hashMap[l][0] + hashMap[l][1]
                if quadrupletSum == targetSum:
                    quadruplet = [hashMap[k][0], hashMap[k][1], hashMap[l][0], hashMap[l][1]]
                    quadruplet.sort()
                    if quadruplet not in ans: 
                       ans.append(quadruplet) 
    return ans

