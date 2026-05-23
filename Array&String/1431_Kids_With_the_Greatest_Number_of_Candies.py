class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        
        time: O(n)
        space: O(1) 
        """
        
        ans = [False] * len(candies)
        max_candy = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                ans[i] = True
        
        return ans