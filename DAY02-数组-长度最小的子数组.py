"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
"""
思路:从连续两个开始找 找到就返回 找不到就找连续三个 直到连续N个
"""
"""
思路进阶 先移动右边的指针直到和大于目标值 再移动左边指针直到和小与目标值 之后同时移动左右指针 直到右指针移动到最右边就停止
"""

def find_sub_array(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:

        if left == right:
            array_sum = nums[left]
        else:
            array_sum = sum(nums[left:right + 1])
        if array_sum >= target:
            if left == right:
                return 1
            old_left = left
            left = 0
            right = right - old_left - 1
            continue
        else:
            if right - left == len(nums) - 1:
                return 0
            if left == right == len(nums) - 1:
                return 2
            else:
                if right + 1 < len(nums):
                    left += 1
                    right += 1
                else:
                    return right - left + 2


def minSubArrayLen(nums, s):
    l = len(nums)
    left = 0
    right = 0
    min_len = float('inf')
    cur_sum = 0  # 当前的累加值

    while right < l:
        cur_sum += nums[right]

        while cur_sum >= s:  # 当前累加值大于目标值
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1

        right += 1

    return min_len if min_len != float('inf') else 0


nums = [1, 2, 3, 4, 5]
target = 11
# s = find_sub_array(nums, target)
s = minSubArrayLen(nums, target)
print(s)
