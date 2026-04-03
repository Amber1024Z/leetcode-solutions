class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        N: number of candidates
        T: target
        M: smallest value in candidates
        time: since we can choose duplicate number, max height will be T/M, ex: target is 8, M is 2,
        depth is 8/2 = 4, since we have n candidates, maximal number of nodes in N-ary tree of height(T/M)
        will be N^(T/M)
        space: O(T/M)
        """
        result = []

        def backtrack(remain, comb, start):
            """
            remain: The remaining value to be completed
            comb: The current combination (list)
            start: The index from which to begin selecting from candidates
            """
            # stop case 1: remain number is 0
            if remain == 0:
                result.append(list(comb))
                return

            # stop case 2: out of range
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                # add current candinate
                comb.append(candidates[i])

                # pass candidate[i], since we can use it duplicatly
                backtrack(remain-candidates[i], comb, i)

                comb.pop()

        backtrack(target, [], 0)

        return result