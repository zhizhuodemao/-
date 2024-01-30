"""
给定四个包含整数的数组列表 A , B , C , D ,
计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。
"""
"""
问题应该拆分成两数之和等于另外两数之和
用一个字典存储所有可能的两数之和的次数
再找另外两个数组所有可能的和 如果两者相反 就计数加上这个和的次数

"""


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1 + n2] = hashmap.get(n1 + n2, 0) + 1

        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count

