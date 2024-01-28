"""
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。
"""
"""
1.如何判断链表中有环
2.如果直到在哪里相遇
思路:如果链表有环 意味着当节点进入环之后只能无限循环 无法出来
所以如果有一个快指针 有一个慢指针同时出发 那么一定可以在环内相遇
那么相遇在什么地方呢?怎么知道呢? 我们可以想像 快指针一定先进环 慢指针后进环
假设快指针速度是慢指针2倍 那么当慢指针进环之后 还没走完一圈的时候 快指针一定能追上 
因为慢指针走一圈 快指针已经走两圈了 所以慢指针不可能走完一圈
那么假设从头节点到环的入口距离是x
环入口到相交位置为y
那么慢指针走的路程一定是x+y
快指针走的路程比慢指针多n个环的路程
假设环剩下的距离为z
那么快指针走的距离为x+y+n(y+z)
因为快指针速度是慢指针2倍  所以慢指针路程的2倍是快指针路程
2(x+y)=x+y+n(y+z)
x+y=n(y+z)
x=n(y+z)-y=(n-1)(y+z)+z
假设n=1 就是x=z 
这就意味着 如果能相遇 从头节点到入口的距离 等于(n-1)个环的距离加上从相遇点到入口的距离
那是不是说 假设现在有两个指针 从相遇点到入口的距离加上(n-1)个环的距离 等于从头节点到入口的距离
也就是说 一个指针从头节点开始走 一个从相遇点开始走 速度相同 一定会在入口相遇
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def huan_lianbiao(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            index1 = head
            index2 = fast
            while index1 != index2:
                index1 = index1.next
                index2 = index2.next
            return index1
    return None
