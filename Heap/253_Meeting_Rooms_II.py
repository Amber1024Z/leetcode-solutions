import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Time: O(n log n)
        - sorting: O(n log n)
        - n meetings * O(log n) heap operation

        Space: O(n)
        - heap can contain all n meetings in the worst case
        """
        
        intervals.sort(key=lambda x:x[0])

        # heap stores each room's ending time
        heap = []

        for start, end in intervals:
            
            # if curr start >= prev interval's end, means we can use same room
            if heap and start >= heap[0]:
                heapq.heappop(heap)

            # if satified if condition, room number remains same, otherwise +1
            heapq.heappush(heap, end)

        return len(heap)