class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        
        time: O(n) where n is the length of flowerbed, we iterate through the flowerbed once.
        space: O(1) we are modifying the flowerbed in place and using only a constant amount of extra space.
        """
        if n <= 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # check left, if i == 0 also flowerbed[i] == 0 means its safe to plot here
                left = (i == 0) or (flowerbed[i - 1] == 0)
                # check right, first check if it's last plot, then check prev pos
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

        return False