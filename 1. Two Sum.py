class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):

            # Checking is the complement of the current value is present in the rest of the list
            if target-nums[i] in nums[i+1:]:

                # When there are no repeating values in the list (like [1,3,2,5])
                if nums[i] != target-nums[i]:
                    return nums.index(nums[i]), nums.index(target-nums[i])

                # When there are repeating values in the list (like [1,2,2,5])
                else:

                    # Finding the index of the first value of the repeating values
                    firstVal = nums.index(nums[i])

                    # Slicing the list from the value after first recurring value to the end of the list
                    newNums = nums[i+1:]

                    # Since 2nd list starts with another 0, we add 1 to the current index of the sliced list and the index of the first value to get the index of the 2nd value
                    secondVal = newNums.index(nums[i])+firstVal+1
                    return firstVal, secondVal
