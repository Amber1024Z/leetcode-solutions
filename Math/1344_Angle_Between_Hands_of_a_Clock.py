class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float

        time: O(1)
        space: O(1)
        """

        # hour hand move 1 hour angle is 30
        one_hour = 30
        # mimute hand move 1 minute is 360/60 = 6
        one_min = 6

        minute_angle = one_min * minutes
        # hour move angle depends on minute, if minutes = 30, hour need to move 1/2 more
        # 12 hrs 30 mins == 12.5 hours
        # hours % 12 to deal when hour = 12, actually start from 0
        hour_angle = ((hour % 12) + (minutes/60.0)) * one_hour

        # return the smaller angle
        diff = abs(minute_angle - hour_angle)
        
        return min(diff, 360 - diff)