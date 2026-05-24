class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        time: O(nlogn) for sorting
        space: O(n) for timsort(python)
        """
        ans = 0
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                ans += 1
                l += 1
                r -= 1
        
        return ans