class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        at most ans will have 2 candidates

        time: O(n)
        space: O(1)
        """

        n = len(nums)
        
        if not nums:
            return []

        cand1, count1 = None, 0
        cand2, count2 = None, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1

            else:
                count1 -= 1
                count2 -= 1

        ans = []

        # check count, if all num only appears once, no valid answer
        for c in [cand1, cand2]:
            if nums.count(c) > n // 3:
                ans.append(c)
        
        return ans

