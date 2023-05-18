# Time: O(m * nlogn); m is the number of strings in strs, n is the number of chars in each string.
# Space: O(m); m is the number of strings in strs.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in dict:
                dict[sorted_s].append(s)
            else:
                dict[sorted_s] = [s]
        return dict.values() 



