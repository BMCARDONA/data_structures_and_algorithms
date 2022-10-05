def fourNumberSum(array, targetSum):
    result = []
    array.sort()
    # for i in range(len(array)) is the range from 0 to len(array), non-inclusive! 
    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            left = j + 1
            right = len(array) - 1
            while left < right:
                quadrupletSum = array[i] + array[j] + array[left] + array[right]
                if quadrupletSum == targetSum:
                    result.append([array[i], array[j], array[left], array[right]])
                    right -= 1
                    left += 1
                elif quadrupletSum > targetSum:
                    right -= 1
                else:
                    left += 1
    return result