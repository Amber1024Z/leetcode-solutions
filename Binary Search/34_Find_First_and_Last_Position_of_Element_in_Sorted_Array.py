class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        time = O(logn)
        space = O(1)
        """

        if not nums:
            return [-1, -1]


        def findFirst(nums, target):
            l, r = 0, len(nums) - 1
            result = -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    result = m 
                    # still nedd search on left
                    r = m - 1 

                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return result

        def findLast(nums, target):
            l, r = 0, len(nums) - 1
            result = -1

            while l <= r:
                m = (l + r)// 2
                if nums[m] == target:
                    result = m
                    # still need search on right
                    l = m + 1

                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return result

        start = findFirst(nums, target)
        last = findLast(nums, target)
        return [start, last]
