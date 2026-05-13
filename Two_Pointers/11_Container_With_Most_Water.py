class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        time: O(n), will stop when l and r meet, so overall time is O(n)
        space: O(1), only use constant extra space
        """
        
        l, r = 0, len(height) - 1

        max_water = 0

        while l < r:
            # ans depends on shorter height
            water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, water)

            # if left is shorter, move l to find next higher height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water
        