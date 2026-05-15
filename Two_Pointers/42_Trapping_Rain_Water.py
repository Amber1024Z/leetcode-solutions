class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        time: O(n) because we traverse the height array once with two pointers.
        space: O(1) 
        """
        ans = 0
        l,r = 0, len(height) - 1
        left_max, right_max = 0, 0

        while l < r:
            if height[l] < height[r]:
                # if curr height[l] >= left_max, only update left_max, can't store water
                if height[l] >= left_max:
                    left_max = height[l]
                # when curr height[l] < left_max, means we can trap water
                # since height[l] < height[r], height[l] will be shorter
                else:
                    ans += left_max - height[l]

                l += 1
            # when height[l] >= height[r]
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans += right_max - height[r]
                
                r -= 1

        return ans
                

        
        