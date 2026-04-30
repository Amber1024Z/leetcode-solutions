class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n), we traverse the array once
        space: O(1)
        """
        # logic is greedy algorithms, keep scanning farthest distance can reach
        answer, n = 0, len(nums)

        # cur_end: current step's range
        # cur_far: furthest position of the next hop that can be detected during traversal within the current scope
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])

            # if we finish search the range, move to starting range of next jump
            # when i = cur_end, means we must jump
            if i == cur_end:
                answer += 1
                cur_end = cur_far

            
            # if cur_end >= n - 1, means we already reach the end, n - 1 is the end position
            if cur_end >= n - 1:
                break

        return answer