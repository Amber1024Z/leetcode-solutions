from collections import defaultdict
from fractions import math
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        math.atan2 是计算 反正切Arctangent的函数

        (0, 0), (2, 2), k = 2 / 2 = 1, math.atan2(1) = 0.785  = 4 = 45度

        time: O(n^2), each point will compare to another n - 1 points
        space: O(n) for map
        """
        n = len(points)
        if n == 1:
            return 1
        
        max_total = 0

        for i in range(n):
            # 每一轮基准点都要重置哈希表，确保只统计经过当前点的直线
            # 这样就自动排除了不经过该点的“平行线”
            angle_dict = defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                
                angle = math.atan2(dy, dx)

                angle_dict[angle] += 1
            
            if angle_dict:
                max_curr_count = max(angle_dict.values())
            else:
                # if len(points) == 1, visit empty dict will caused error
                max_curr_count = 0

            max_total = max(max_total, max_curr_count + 1)

        return max_total


        
