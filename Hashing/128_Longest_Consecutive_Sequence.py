class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time complexity: O(n), where n is the length of nums. While loop runs at most n times, becuase we prune the loop 
        by only starting from numbers that are the beginning of a sequence (i.e., num - 1 is not in the set). Each number 
        is processed at most once.

        space complexity: O(n), we need to store all numbers in a set for O(n) space.
        """

        ans = 0
        num_set = set(nums)

        for num in num_set:
            # we only care about num - 1 whether if it's exsit in our num_set
            # if not, current num may be the start point
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1

                ans = max(curr_len, ans)

        return ans
