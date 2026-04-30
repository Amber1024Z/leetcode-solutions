class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        time complexity: O(n), where n is the length of nums
        space complexity: O(n), The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.
        """

        num_dict = {}

        # create dict, key is num, value is index
        for i, num in enumerate(nums):
            num_dict[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            # check if complement exists in dict and is not the same index
            if complement in num_dict and num_dict[complement] != i:
                return [i, num_dict[complement]]


