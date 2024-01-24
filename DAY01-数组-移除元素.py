"""
question2:给你一个数组nums和一个值val
你需要原地移除所有数值等于val的元素并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""

"""
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 
或 nums = [2,2,0,0]，也会被视作正确答案。
看到元素移动加上返回指针类似东西,优先考虑双指针法
"""
"""
思路 不许使用额外空间 还要移除元素 意思是遍历所有元素 找到指定位置元素 
把指定位置元素之后所有元素都往前移动一位 之后把该位置元素放到倒数第i位 
i是集合中找到该元素的次数
用while循环实现 如果等于集合中某个元素 就定位置元素之后所有元素都往前移动一位 之后把该位置元素放到倒数第i位 
如果不等于 就看看下一个元素 
"""
"""
优化思路 上述思路的时间复杂度是O(n^2) 我们可以使用双指针法 
左右指针初始化在最左边
左指针指向要输出数组的位置 右指针始终向右移动
如果右指针指向的元素不等于target 代表这个应该是要输出的元素 应该放在左指针
因此把这个元素的值赋值到左指针的位置 左指针右移 同时右指针右移
如果右指针指向的元素等于target 左指针不变 右指针右移 相当于跳过这个元素
最后这个数组一定是等于target的元素在最后边
"""


def delete_item(nums, target):
    flag = 0
    i = 0
    while i < len(nums) - flag:
        if nums[i] == target:
            now_item = nums[i]
            flag += 1
            for j in range(i + 1, len(nums)):
                nums[j - 1] = nums[j]
            nums[-flag] = now_item
        else:
            i += 1
    return len(nums) - flag


def delete_item2(nums, target):
    left, right = 0, 0
    for i in range(len(nums)):
        if nums[i] != target:
            nums[left] = nums[right]
            left += 1
            right += 1
        else:
            right += 1
    return left


print(delete_item([1, 2, 3, 3, 4, 5], 3))
print(delete_item2([1, 2, 3, 3, 4, 5], 3))
