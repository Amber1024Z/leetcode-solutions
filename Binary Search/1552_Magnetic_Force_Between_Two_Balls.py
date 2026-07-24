class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int

        time: O(nlog((n * k) / m), sort takes nlogn, for binary search, assume max position is k
        max d can reach is k / m, that also is our search range, will take log(k/m). For each
        binary search round, we called canPlace(mid), this will cost n times(line 22). Thus for binary seach total is nlogn(k/m).

        space: O(n) for timsort
        """
        
        position.sort()

        # assume d is the ans we want, all force(distance) between 2 balls must >= d.
        def canPlace(d):
            # test with min distance of d, whether it's able to place all m balls
            # first ball with always place on head
            count = 1
            last_pos = position[0]

            for i in range(1, len(position)):
                if position[i] - last_pos >= d:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            
            return False

        # binary serach find best d
        # smallest distance is 1, because all integers in position are distinct. largest distance will be position[r] - positions[l], place 2 balls on head and tail
        low = 1
        # max desire d = total length // gap number, if we have 4 balls to place, gap will be 3
        high = (position[-1] - position[0]) // (m - 1)

        ans = 1

        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                # if able to place with mid, we need find if exsits larger answer
                ans = mid
                low = mid + 1
            else:
                # mid is too large
                high = mid - 1

        return ans

