from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        # check if head of queue is smaller than t - 3000
        while self.queue[0]<t-3000:
            self.queue.popleft()

        return len(self.queue)    

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)