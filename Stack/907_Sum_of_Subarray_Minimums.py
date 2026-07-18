class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        time: O(n)
        sapce: O(n)
        """
        
        MOD = 10**9 + 7

        n = len(arr)

        """
        left[i] represents start from arr[i], look left, how many consecutive elements are greater than it (including itself)

        ex: arr = [3,1,2,4]

        for number 2, look to left, 1 < 2, thus left[2] is 1, right[2] is 2
        """
        left = [0] * n
        right = [0] * n

        # push number and count into stack(arr[i], count)
        stack = []

        # find first element on left < arr[i]
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                # if prev number in stack > curr number, curr number can still can be smallest number to generate longer subarry, pop out larger number.
                count += stack.pop()[1]
            # if prev < curr, left[i] = count = 1
            left[i] = count
            stack.append((arr[i], count))

        stack = []
        # find first number on right < arr[i]
        for i in range(n - 1, -1, -1):
            count = 1
            # remember =, to avoid duplicate calculation.
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            
            right[i] = count
            stack.append((arr[i], count))

        total = 0
        for i in range(n):
            total = (total + arr[i] * left[i] * right[i]) % MOD
        
        return total

