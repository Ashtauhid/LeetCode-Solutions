class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        This is a code that I started with (Brute-force method) but since it takes forever to run large inputs, we cannot submit this code in leetcode to expect an "Accepted".
            # result = 0
            # for i in range(len(height)):
            #     for j in range(i+1, len(height)):
            #         length = min(height[i], height[j])
            #         temp = length*(max(1,j-i))
            #         if temp <= result:
            #             continue
            #         else:
            #             result = temp
            # return result
        """
        i = 0
        j = len(height)-1
        areaMax = 0

        # Looping with two pointers from left and right
        while(i<j):

            # Calculating the area within the current two pointers
            area = min(height[i],height[j]) * (j-i)

            # Selecting the maximum area between the current area and the previous area
            areaMax = max(area, areaMax)

            # Comparing the left pointer and right pointer. If the value in smaller we increase/decrease that pointer
            if height[i] < height [j]:
                i += 1
            else:
                j -= 1
        return areaMax
