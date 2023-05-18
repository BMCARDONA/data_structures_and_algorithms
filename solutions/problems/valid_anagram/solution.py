# Time: O(s + t), where s and t are lengths of strings s and t, respectively.
# Space: O(s + t), where s and t are lengths of strings s and t, respectively.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        # As a default, use "for i in range(len(__))" 
        for i in range(len(s)):
            # The .get() method is a built-in function in Python that is used to
            # retrieve the value of a specified key from a dictionary. If the key 
            # is not found in the dictionary, it returns a default value that you
            # can specify as the second argument to the .get() method.
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        for c in s:
            # if key does not exist at index c in hashT, then set default to 0
            if hashS[c] != hashT.get(c, 0):
                return False
        return True