"""
给你一个链表的头节点 head 和一个整数 val ，
请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
"""
"""
思路:先建立一个虚拟的头节点 把虚拟头节点的下一个节点设置为传入的头节点 
虚拟头节点的值设为None  虚拟头结点的下一个元素的值开始跟传入值对比 
如果相同 就把这个节点的下一个元素变为原本的下下个元素 就可以做到删除这个元素
如果不同 就把直接到下一个节点
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = None
        self.next = None


def removeNode(headNode, val):
    virtual_head_node = Node(next=headNode, val=None)
    current_node = virtual_head_node
    while current_node.next:
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return virtual_head_node.next
