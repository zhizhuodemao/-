"""给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。"""

"""
思路 如果是正数第n个节点 我们都知道怎么做 但是倒数怎么实现呢
首先要找到倒数第n个节点 怎么找是关键
我们假设先找到最后一个节点 然后找到前边n个节点 这样显然不可能
所以我们用两个指针 指针2指向最后一个节点 指针1只要和指针2差距n个节点 那么指针2就是倒数第n+1节点
应该差距n-1节点?
首先其实我们没办法定位最后一个节点 只能先定位到最后一个节点的后一个节点
那么差距n个节点得指针1 指向得就是倒数第n个节点 但是我们要删除这个节点
应该让指针1指向倒数n+1节点 也就是说两个指针差距n+1节点
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 首先还是构建虚拟头节点
        virtual_head = ListNode(next=head)
        # 定义快指针和慢指针
        fast = virtual_head
        slow = virtual_head
        # 把快指针向右移动n+1节点 这道题不用判断是否有第n个节点
        for i in range(n+1):
            fast = fast.next
        # 把快慢指针同时移动 直到快指针指向None
        while fast:
            fast = fast.next
            slow = slow.next
        # 满指针得位置就是倒数第n+1节点
        # 满指针得下一个节点是下下一个节点
        slow.next = slow.next.next
        return virtual_head.next