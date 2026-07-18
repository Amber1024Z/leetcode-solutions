class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int

        time: for cost will takes O(n^3), for dp is O(n * k * n), overall is O(n^k)
        space: for dp is O(n^2), cost is O(n * k), overall O(n^2)
        """
        
        houses.sort()

        n = len(houses)

        # cost represents from house[i] to house[j], min distance of place 1 mailbox 
        cost = []
        for _ in range(n):
            cost.append([0] * n)

        for i in range(n):
            for j in range(i, n):
                # to find min distance, we should place mailbox in median
                median_pos = houses[(i + j) // 2]
                # calculate from house[i] to house[j], place mailbox on median_pos, the accumulate distance.
                for house in range(i, j + 1):
                    cost[i][j] += abs(houses[house] - median_pos)

        """
        dp[i][j], i represents number of houses, not idx. min distance to place j mailbox
        dp[2][j] represents min distance of place j mailbox with 2 hosues
        also need case of 0 houses with 0 mailbox, thus size need to be n + 1
                     j=0邮筒  j=1邮筒      j=2邮筒   j=3邮筒
        i=0栋房子   [  0         0           0           0 ]
        i=1栋房子   [  inf   cost[0][0]      inf      inf  ]
        i=2栋房子   [  inf   cost[0][1]      inf      inf  ]
        i=3栋房子   [  inf   cost[0][2]      inf      inf  ]
        i=4栋房子   [  inf   cost[0][3]      inf      inf  ]
        """
        dp = []
        for i in range(n + 1):
            row = [float('inf')] * (k + 1)
            dp.append(row)

        # initialize first row, 0 houses place k mailbox, all need to be 0
        for j in range(k + 1):
            dp[0][j] = 0

        # initialize second col, i houses place 1 mailbox
        for i in range(1, n + 1):
            dp[i][1] = cost[0][i - 1]

        # calculate i houses with j mailbox
        for i in range(1, n + 1):
            for j in range(2, k + 1):
                # if number houses <= k mailbox, we can assign mailbox to each hosue
                if i <= j:
                    dp[i][j] = 0
                    continue
                
                """
                p represents the number of houses allocated to the left
                
                first p houses are managed by the first j-1 postboxes(left), from the p+1st to the i-th are managed by the jth postbox(right).

                # we've already calculate use only 1 mailbox on cost, thus for left at least has j - 1 houses to make sure no waste. upper bound for p is i - 1, at least we need to left 1 house for right part
                """
                for p in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]

                
