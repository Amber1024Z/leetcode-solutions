class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]

        time: O(n)
        space: O(1)
        """
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while  i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            # i will stop at last continous num
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            # if is a single number, just return
            else:
                ans.append(str(start))
            
            i += 1

        return ans

            