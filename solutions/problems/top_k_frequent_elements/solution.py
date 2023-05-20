class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {} # n --> count
        for n in nums:
            hash[n] = 1 + hash.get(n, 0) # Learned
        freq = [[] for i in range(len(nums) + 1)] 
        for n, count in hash.items():
            freq[count].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1): # Learned
            for num in freq[i]:
                res.append(num)
                if len(res) == k: # Learned (counter is unnecessary)
                    return res



