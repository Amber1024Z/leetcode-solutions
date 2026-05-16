class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        i = 0

        while i < len(nums):
            # j is corrct pos for nums[i], ex: 1 should put on pos 0
            j = nums[i] - 1
            # swap num to corr pos
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # if num already in right pos, i += 1
                # i is curr idx, j is correct idx
                if i == j:
                    i += 1
                # if i != j, and nums[i] = nums[j], nums[i] must be the duplicate num
                else:
                    return nums[i]

            