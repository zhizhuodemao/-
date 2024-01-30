"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意： 答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
"""
import array

"""
思路 找到nums中所有两数之和 第三数只需要为和的负数就可以
"""


class Solution:
    def threeSum(self, nums):
        dict = {}
        # 找到所有的两数之和
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dict[(i, j)] = nums[i] + nums[j]
        result = []

        for i in range(len(nums)):
            for k, v in dict.items():
                if i not in k and -v == nums[i]:
                    k_list = list(k)
                    k_list.append(i)
                    result.append(k_list)
        final_result = []
        for item in result:
            result_new = []
            for i in range(len(item)):
                result_new.append(nums[item[i]])
            final_result.append(result_new)
        res = []
        for item in final_result:
            item = sorted(item)
            if item not in res:
                res.append(item)
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # 找出a + b + c = 0
        # a = nums[i], b = nums[j], c = -(a + b)
        for i in range(len(nums)):
            # 排序之后如果第一个元素已经大于零，那么不可能凑成三元组
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 三元组元素a去重
                continue
            d = {}
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j - 1] == nums[j - 2]:  # 三元组元素b去重
                    continue
                c = 0 - (nums[i] + nums[j])
                if c in d:
                    result.append([nums[i], nums[j], c])
                    d.pop(c)  # 三元组元素c去重
                else:
                    d[nums[j]] = j
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
