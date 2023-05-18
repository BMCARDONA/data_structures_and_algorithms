class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for letter in s:
            if letter not in hash:
                hash[letter] = 0
            hash[letter] += 1
        for letter in t:
            if (letter not in hash) or hash[letter] == 0:
                return False
            hash[letter] -= 1
        return True
