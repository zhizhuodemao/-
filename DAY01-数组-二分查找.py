"""
question1:从非重复的升序数组中查找特定元素,查到返回元素索引,查不到返回-1
解题关键 非重复有序 二分法可以把每次查询的复杂度降低至logN
因为返回的是索引值 所以应该用指针来做 指针用左右指针
因为用指针 指针不停移动 所以用while循环 最终两个指针重合 重合的位置就是结果
"""
"""
解题思路:定义两个指针 一个左指针 一个右指针 由于我们只需要找到元素的下标 所以指针移动就够了
当左指针小于右指针时 继续循环 直到左指针等于右指针
什么时候左指针等于右指针 目标元素等于最小最大元素 目标元素小于最小元素或者目标元素大于最大元素
此时判断目标元素是否等于最小最大元素 如果不等于 返回-1 如果等于 返回此时的指针位置
看到要返回索引 优先考虑指针
"""


def search(array, target):
    array_len = len(array)
    left = 0
    right = array_len - 1
    while left < right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == right and array[left] == target:
        return left
    else:
        return -1


index = search([3, 4, 5, 6, 7, 8, 9], 10)
print(index)
