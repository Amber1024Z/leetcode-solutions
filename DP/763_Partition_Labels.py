class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]

        time: O(n), we traverse the string twice, once to record last idx for each char, once to find patition
        spcae: O(1), we use dict to record last idx for each char, worst case, we have 26 chars, so space complexity is O(1)

        """

        last_idx = {}
        res = []

        # record last idx for each char
        for i in range(len(s)):
            last_idx[s[i]] = i

        start, end = 0, 0

        for i in range(len(s)):
            # find curr patition end idx
            end = max(end, last_idx[s[i]])
            # if i reach curr patition end range, we should start next partition
            if i == end:
                # update curr patition size
                res.append(end - start + 1)
                # update new start idx for next partition
                start = i + 1

        return res