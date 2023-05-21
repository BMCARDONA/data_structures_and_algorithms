# Time: O(n), where n is the number of elements in nums
# Space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        res = [1] * len(nums)
        prefix = 1 # initialize to 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # update prefix
        postfix = 1 # initialize to 1
        for i in range(len(nums) - 1, -1, -1): # iterate array in reverse order
            res[i] *= postfix 
            postfix *= nums[i]
        return res
