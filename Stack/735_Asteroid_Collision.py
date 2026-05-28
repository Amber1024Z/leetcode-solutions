class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]

        time: O(n)
        space: O(n)
        """
        
        stack = []

        for num in asteroids:
            # explode: curr < 0 (left) and top element in stack > 0(right)
            alive = True
            
            while alive and num < 0 and stack and stack[-1] > 0:
                if stack[-1] < abs(num):
                    stack.pop()
                elif stack[-1] == abs(num):
                    stack.pop()
                    alive = False
                # stack[-1] > num
                else:
                    alive = False
            
            if alive:
                stack.append(num)

        return stack
        