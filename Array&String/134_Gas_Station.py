class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        Total loss in the first half + total profit in the second half = sum ≥ 0
        -> Total profit in the second half ≥ total loss in the first half ≥ 0
        -> The second half must therefore result in a net profit

        time: O(n)
        space: O(1)
        """
        
        # sum(gas) >= cost(gas) means there must have a valid solution
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            # calculate diff from gas and cost, if accumulate total < 0, means we can't start from any point before i
            total += (gas[i] - cost[i])

            # when total > 0, means start from i, left tour's gas must >= prev tour cost
            if total < 0:
                total = 0
                res = i + 1

        return res