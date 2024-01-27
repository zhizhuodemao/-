"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
输入：head = [1,2,3,4]
输出：[2,1,4,3]
"""
"""
思路 链表节点两两交换 首先从交换前两个节点开始 1->2->3->4->5->null
那么要做到的就是2->1->3->4->5->null
需要更改的是 1原本指向2 现在指向3 
2原本指向3 现在指向1
怎么让1指向3 2指向1 
我们找到头节点 找到下一个节点

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        new_head = None
        if current is not None:
            if current.next is not None:
                new_head = head.next
            else:
                while current.next is not None and current.next.next is not None:
                    next_current = current.next
                    # 这一步让1指向3 先在current还是1
                    current.next = current.next.next
                    # 下一步应该让2指向1 问题是2没有了现在 所以应该先保存2
                    next_current.next = current
                    # 现在应该让current移动到3 执行下一轮改变
                    # 但是current可能存在next 也不存在next 甚至current都可能不存在
                    # 所以应该做检验
                    # 问题就是current 原本指向1 现在还是1 所以应该指向下一个
                    # 但是下一个也会变 所以说这样不好 应该构造虚拟头节点
                    current = current.next
        return new_head

    def swapPairs2(self, head):
        virtual_head = ListNode(next=head)
        current_head = virtual_head
        # 现在有了虚拟头节点 只需要交换之后在移动current就好了
        # 到最后直接返回virtual_head.next就好了 不管谁是头部
        # 要交换 起码得有两个元素 不然假设只有0或1个元素 直接返回就可以了
        while current_head.next is not None and current_head.next.next is not None:
            temp_second = current_head.next.next
            # 第一步 第一个元素得下一个节点是第三个元素
            current_head.next.next = current_head.next.next.next
            # 第二步 第二个元素得下一个节点是第一个元素 第一个元素现在还没变
            # 还是current_head.next
            # temp是第二个元素 current_head还是虚拟头节点 没改变
            temp_second.next = current_head.next
            # 第三步 当前节点得下一个元素是第二个元素
            current_head.next =temp_second
            # 第四步 移动current_head为后两个节点
            current_head=current_head.next.next
        return virtual_head.next
if __name__ == '__main__':
    list1 = ListNode(1, next=ListNode(2, next=ListNode(3)))
    solution = Solution()
    print(solution.swapPairs(list1))
