class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int

        we can transfer question into convex, x present number from min(nums) to max(nums), 
        y represents total cost, our goal is to find the target with min cost, which is the lowest
        point on graph, use binary search.

        time: n be the length of the input array nums, k is the difference between the maximum
        and minimum, each time we pick a mid, we will call 'get_cost' which take O(n) to iterate
        all num. Thus overall is O(nlogk)

        space: O(1)

        space
        """
        
        n = len(nums)

        if len(set(nums)) == 1:
            return 0

        def get_cost(base):
            total_cost = 0

            for i in range(n):
                num = nums[i]
                c = cost[i]

                # calculate how many steps away curr num to base
                steps = abs(base - num)
                curr_cost = steps * c

                total_cost += curr_cost

            return total_cost

        l, r = min(nums), max(nums)

        # initialize ans, take first num as base
        ans = get_cost(nums[0])

        while l < r:
            m = (l + r) // 2

            # we need 2 cost to determine is 'upward' or 'downward'
            cost_1 = get_cost(m)
            cost_2 = get_cost(m + 1)

            ans = min(cost_1, cost_2)

            # f(x) > f( x+ 1), it's downward, min ans is on right
            if cost_1 > cost_2:
                l = m + 1
            # if it's upward, f(x) could be target we want
            else:
                r = m

        return ans