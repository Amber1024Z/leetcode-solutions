class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        instead of count 1, count curr window contains how many 0, as long as number of 0 < k,
        we can extend right boundary. If number of 0 > k, we should shrink from left 

        time: O(n)
        sapce: O(1)
        """

        zero = 0
        ans = 0

        l = 0
        

        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1
            # if zero > k, shrink from left until zero <= k
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                # if zero > k, no matter nums[l] is 0 or 1, we should shrink from left
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans