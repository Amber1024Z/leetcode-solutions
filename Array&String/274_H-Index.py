class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        | 0 | 1 | 2 | 3 | 4 | 5 (>=5) |
        | 1 | 1 | 0 | 1 | 0 | 2 |
        
        time: O(n)
        space: O(n)
        """

        # I have H papers, and each of these H papers has been cited at least H times.
        # H_index <= H
        # apply bucket sort intialize  0-6 bucket
        n = len(citations) 
        # create buckets, everithing >= 5 will store in bucket 5
        buckets = [0] * (n + 1)

        for c in citations:
            # if citation > n, put in bucket[n], last bucket
            if c >= n:
                buckets[n] += 1
            # otherwise put in corresponding bucket
            else:
                buckets[c] += 1

        # backward checking hIndex
        count = 0
        for i in range(n, -1, -1):
            # count represents num of citation 
            # i is total num of papers
            count += buckets[i]

            # at least i papers have been cited at least i times
            if count >= i:
                return i

        return 0

        



