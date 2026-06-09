from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool

        time: O(N+k), N is num for rooms, K is num for keys.
        space: O(N) for queue and seen, worst case all keys in first room
        """
        # room 0 is not locked
        seen = set()
        seen.add(0)

        queue = deque()
        queue.append(0)

        while queue:
            node = queue.popleft()
            
            for nei in rooms[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        
        return len(seen) == len(rooms)

        