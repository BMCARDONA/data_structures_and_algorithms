# First attempt 
# O(n^3) time) | O(n) space

def longestPalindromicSubstring(string):
    longestPalindrome = ""
    for i in range(len(string)):
        for j in range(len(string)):
            substring = string[i : j + 1]
            if isPalindrome(substring):
                if len(substring) > len(longestPalindrome):
                    longestPalindrome = substring
    return longestPalindrome     
    

def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while (left < right):
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
