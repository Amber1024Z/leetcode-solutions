class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        time: O(n^2)
        space: O(n) for timesort
        """
        
        n = len(nums)

        if n == 3:
            return sum(nums)

        nums.sort()

        ans = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if curr == target:
                    return curr

                if abs(curr - target) < abs(ans - target):
                    ans = curr

                if curr > target:
                    r -= 1
                else:
                    l += 1

        return ans
                
