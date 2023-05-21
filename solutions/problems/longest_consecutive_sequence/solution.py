# Time: O(n), where n is len(nums)
# Space: O(n), where n is len(nums)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_consecutive_seq = 0
        for num in nums:
            if (num - 1) not in numSet: # If num is start of sequence
                counter = 0
                while (num + counter) in numSet:
                    counter += 1
                    longest_consecutive_seq = max(longest_consecutive_seq, counter)
        return longest_consecutive_seq
                

            
            