from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """
    
        n = len(fruits)

        if n <= 2:
            return n

        l = 0

        basket = defaultdict(int)
        ans = 0

        for r in range(n):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]

                l += 1

            ans = max(ans, r - l + 1)

        return ans



        
            