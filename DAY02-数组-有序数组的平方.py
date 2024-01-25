"""
给你一个按非递减顺序排序的整数数组nums，
返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
"""

"""
思路:非递减顺序 不就是递增顺序  但是可能存在负数 负数的平方可能大于正数
所以思路应该是先按数值排序 在取其平方 那怎么按数值排序 
要利用好原本的递增顺序

思路提升:两边的元素一定是最大的 那么初始化两边指针 找到最大的 拿出来 指针移动 继续找
"""


def sort_nums(nums):
    out_nums = [num * num for num in nums]
    out_nums.sort()
    return out_nums


def sort_nums2(nums):
    out_nums = []
    left = 0
    right = len(nums) - 1
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            out_nums.append(nums[right] ** 2)
            right -= 1
        else:
            out_nums.append(nums[left] ** 2)
            left += 1
    out_nums.reverse()
    return out_nums


nums = [-4, -1, 0, 3, 10]
# print(sort_nums(nums))
print(sort_nums2(nums))
