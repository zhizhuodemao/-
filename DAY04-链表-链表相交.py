"""
给你两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
"""

"""
这道题最大得问题在于怎么定义相交
如果链表相交 意味着交点之后每个元素都相等 
关键问题就是我们怎么判断 假设链表长度相等 那就从头开始比较到结尾
但是如果不相等 怎么比较 长的移动到一半 短的就走完了 
但是短的还有可能在后边得元素和长的相交
如果都长的先走到跟短的差距长度一样的位置 是可以保证同时走到结尾
但是怎么保证短的不会跟长的前边一样呢 实际上不可能这样
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:  # 求链表A的长度
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:  # 求链表B的长度
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:  # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next
        while curA:  # 遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
