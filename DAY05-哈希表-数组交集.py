"""
题意：给定两个数组，编写一个函数来计算它们的交集。
"""

"""
思路 交集的意思就是一个数组中出现过 另一个数组也出现
我们构建一个dict 存储数组1中每个元素出现的次数
在数组2中 遍历 如果字典中有值 就说明相交 
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]

        return list(res)