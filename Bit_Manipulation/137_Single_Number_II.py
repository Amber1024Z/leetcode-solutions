class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        2  ->  0 0 1 0
        2  ->  0 0 1 0
        3  ->  0 0 1 1  <- 那个落单的数
        2  ->  0 0 1 0
        ------------------
      纵向数1:  0 0 4 1  (每一列 1 的总和 bit_sum)

        4 % 3 = 1, 1 % 3 = 1, 拼起来就是 0011, 十进制的 3.

        time: O(N), We iterate over all integers in nums once, and for each integer, we iterate over all 32 bits. So, the time complexity is O(32N), which is O(N).

        space: O(1)
        """
        ans = 0

        for shift in range(32):
            bit_sum = 0

            # 统计所有数字在当前这个 shift 位上 1 的总个数
            for num in nums:
                # (num >> shift) & 1 的作用是提取出 num 从右往左数第 shift 位的数字
                # 一竖列一竖列的处理
                bit_sum += (num >> shift) & 1

            ans_bit = bit_sum % 3

            #还原：把这个 1 弹射回它原本的 shift 位置，并用“或”运算填进结果
            # 如果 loner_bit 是 0，| 0 不会有影响；如果是 1，则会把该位置为 1
            ans |= (ans_bit << shift)

            """
            在 32 位有符号整数中，最高位（第 31 位）是符号位
            1 << 31是负数, 所以ans如果大于这个数, 代表ans也是负数
            10000000 00000000 00000000 00000000 -> 1 << 31 =  2,147,483,648
            第一个数字如果是1代表负数, 0的话就是正数
            """

        if ans >= (1 << 31):
            """
            如果是负数，想让它变成负数对应的位置，最快的方法就是减去一整圈 1 ^ 32
            1 << 32 = 4,294,967,296

            ex: 10000000 00000000 00000000 00000000 -> 1 << 31
            2,147,483,648 - 4,294,967,296 = -2,147,483,648
            成功把1 << 31 转换成了对应负数形式
            
            """
            ans -= (1 << 32)

        return ans
        




