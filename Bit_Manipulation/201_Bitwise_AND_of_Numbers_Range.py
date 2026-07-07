class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int

        5: 1 0 1
        6: 1 1 0
        7: 1 1 1
        只要竖着有一个0 整竖列位0, 等价于我们要找公共前缀, 因为有0的都会变成0
        只有第一列的1会被保留下来, 并且在操作过程中,我们实际只是在对比left 和right, 中间的数字
        都被忽略了, 因为left = right 的时候找到的公共前缀必定也是中间数字的公共前缀

        time: O(1), the number of iterations is bounded by the number of bits that an integer has, which is fixed.

        space: O(1)
        """
        shift = 0

        while left < right:
            # 7: 11 5: 10
            left = left >> 1
            right = right >> 1
            shift += 1

        # 砍到 5 和 7 都为1的时候，找到公共前缀
        return left << shift

            
        


        