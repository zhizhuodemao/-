"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
"""
思路:遍历列表中每一个数 找到这个数跟target的差值 如果差值在剩下的数中存在 就找到了
但是要记录两个数的index
因为有两个任务 1是看看剩下数中是否存在差值的数
2是看看数的下标 所以应该用map实现
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            result = []
            result.append(i)
            if target - nums[i] in dict:
                result.append(dict[target - nums[i]])
                return result
            else:
                dict[nums[i]] = i
        return []
