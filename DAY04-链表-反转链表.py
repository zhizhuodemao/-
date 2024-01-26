# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        思路:从第一个节点开始 把第一个节点的前一个元素变为第二个节点
        把后一个元素变为None
        这样之后 把第二个节点变成当前节点
        每次循环 当前节点都会后移 直到原本的最后一个节点的next节点 为Null

        :param head:
        :return:
        """
        cur = head
        pre = None
        while cur:
            temp = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre  # 反转
            # 更新pre、cur指针
            pre = cur
            cur = temp

        return pre
