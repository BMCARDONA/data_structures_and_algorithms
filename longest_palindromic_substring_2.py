
# Time: O(n) | Space: O(n)

def longestPalindromicSubstring(string):
    # The two numbers in currentLongest just represent the 
    # indices at which the string will be spliced

    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    # Since splicing is exclusive for second value,
    # we don't have to decrement rightIdx here
    return [leftIdx + 1, rightIdx]

