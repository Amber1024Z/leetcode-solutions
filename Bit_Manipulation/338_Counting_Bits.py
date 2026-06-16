class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]

        any even number's binary version last digit must be 0, any odd number last digit is 
        must 1.
        for even number:
        6 :1 1 0 6 // 2 = 3
        3 :1 1
        we can find out the diff between them is remove last 0 from 6
        4: 1 0 0 
        2: 1 0
        same logic, no matter the res is even or odd, for even number always remove last 0,
        no change for count.

        for odd number:
        7: 1 1 1
        3: 1 1
        7 // 2 = 3, remove last digit from odd number, did change count.
        
        time: O(n)
        space: O(n)
        """
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            # even number has no contribute to count
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            # odd number will contribute to count, need + 1
            else:
                ans[i] = ans[i // 2] + 1

        return ans
