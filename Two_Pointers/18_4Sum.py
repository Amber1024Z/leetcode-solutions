class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]

        Time: O(n^3)
        - sorting: O(n log n)
        - two nested loops: O(n^2)
        - two pointers for each (i, j): O(n)
        - overall: O(n^3)

        Space:
        - O(1) auxiliary space excluding sorting/output
        - O(n) if Python Timsort's temporary space is counted
        """
        
        n = len(nums)
        nums.sort()
        res = []

        for i in range(len(nums)):
            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                # same logic like i, skip duplicate j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1

                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return res


