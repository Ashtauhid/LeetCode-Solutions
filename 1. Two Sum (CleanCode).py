class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                return (i, i+nums[i+1:].index(temp)+1) # Since we sliced the nums array into a sub array of nums[i+1:],
                                                       # we have a new initial position of value 0. Hence we have add 1
                                                       # with the sliced list. And since we skipped first i elements,
                                                       # we have to add i to the total value.
