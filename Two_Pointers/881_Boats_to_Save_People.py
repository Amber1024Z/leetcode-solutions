class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int

        time: O(nlogn) for sort
        space: O(n) for timsort
        """
        people.sort()
        ans = 0

        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                ans += 1
                l += 1
                r -= 1
            else:
                ans += 1
                r -= 1

        return ans
            