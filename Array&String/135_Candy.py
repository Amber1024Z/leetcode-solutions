class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        
        time: O(n)
        space: O(n) -> ans
        """
        ans = [1] * len(ratings)

        # scan from left to right
        i = 0
        while i < len(ratings):
            if i > 0 and ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1
            i += 1


        # scan from right to left
        j = len(ratings) - 2
        while j >= 0:
            if ratings[j] > ratings[j + 1]:
                # use max because we need compare left and right, qualified both side
                ans[j] = max(ans[j], ans[j + 1] + 1)
            j -= 1
                
        return sum(ans)

        

            