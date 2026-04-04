class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        time: 4^n is all possible combination, we have 2n position to fill out, each position has 2 options,
        ethier left or right, thus will be 2^(2n) = 4^n, but we have constraints r <= l <= n, through pruning,
        denominator will be catlan number which is n(root n),  thus overall is 4^n/n(root n)
        space: O(n)
        """
        result = []

        # key rule: right <= left <= n
        def backtrack(cur_string, left_count, right_count):
            # stop case
            if len(cur_string) == 2 * n:
                result.append(''.join(cur_string))
                return

            # add left parentheses
            # as long as left parentheses < n, we can add
            if left_count < n:
                cur_string.append('(')
                backtrack(cur_string, left_count + 1, right_count)
                # backtrack
                cur_string.pop()

            # for right must < left
            if right_count < left_count:
                cur_string.append(')')
                backtrack(cur_string, left_count, right_count + 1)
                cur_string.pop()

        backtrack([], 0, 0)

        return result