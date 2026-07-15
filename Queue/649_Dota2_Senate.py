from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str

        time: O(n)
        space: O(n)
        """

        n = len(senate)
        
        # use 2 queues to store each idx

        radiant = deque()
        dire = deque()

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # first come first make decision
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            # if r_idx is smallter, will vote out d_idx, also will join next round
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
        
        if radiant:
            return 'Radiant'
        else:
            return 'Dire'
