class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        time: choose k from n numbers, binomial coefficient
        space: O(k),  depth of the call stack is equal to the length of curr, which is limited to k.
        """
        res = []
        def backtrack(curr, first_num):
            if len(curr) == k:
                # since it's list, we need shallow copy
                res.append(curr[:])
                return

            need = k - len(curr)
            # calculate the interval to avoid dupliate
            # ex: n = 10, first num = 8, we can choose 8,9,10, 10 - 8 + 1 = 3
            remain = n - first_num + 1
            # n = 10, k = 5, if I alreay have 2, still need 3, remain = 10-4+1=7,avalible = 7-3 = 4, which menas at most I can skip 4 num. 
            # # pruning, if avaliable < 0 we can skip
            avaliable = remain - need

            for num in range(first_num, first_num + avaliable + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

        backtrack([], 1)
        return res

            
        