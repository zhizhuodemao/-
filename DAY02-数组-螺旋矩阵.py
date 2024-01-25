"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]

"""
"""
分两步 第一步获取平方 第二步排列组合
1 2 3 -> 1,2,3,4,5,6,7,8,9
顺时针排列 4=N+1 所以4不得不在第二行 5=N+2 所以5在第三行 6=2N 但是最多只有三行 因此
6不得不在最后一行 7=2N+1 7在最后一行 8=2n+2 8在倒数第二行 9=3N 9
1 2 3
8 9 4
7 6 5

"""


class Solution:
    def generateMatrix(self, n: int):
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        loop, mid = n // 2, n // 2  # 迭代次数、n为奇数时，矩阵的中心点
        count = 1  # 计数

        for offset in range(1, loop + 1):  # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums
