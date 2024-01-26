"""
你可以选择使用单链表或者双链表，设计并实现自己的链表。
单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。
实现 MyLinkedList 类：
MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self, headNode):
        self.virtual_head = Node(next=headNode)
        self.size = 0

    # 获取第index个元素的值
    def get(self, index):
        """
        思路 先判断给的index是否超出限制
        如果没超出限制 找第index个元素的值
        :param index:
        :return:
        """
        if index < 0 or index > self.size:
            return -1
        current_node = self.virtual_head.next
        for i in range(index):
            current_node = current_node.next
        return current_node

    # 添加一个元素在头部
    def addAtHead(self, val):
        """
        思路:创建一个元素 并把这个元素的后一个元素为之前的第一个元素
        这个元素变为虚拟头部的后一个元素
        :param val:
        :return:
        """
        new_head = Node(val=val, next=self.virtual_head.next)
        self.virtual_head.next = new_head

    # 添加一个元素在尾部
    def addAtTail(self, val):
        """
        思路:先找到尾部 把原来尾部的最后一个元素变成新创建的元素
        :param val:
        :return:
        """
        tail_node = Node(next=None, val=val)
        current_node = self.virtual_head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = tail_node

    # 添加一个元素在index这个元素位置
    def addAtIndex(self, index, val):
        """
        思路:找到这个位置的元素 把这个元素后元素变为新创建的元素
        把新创建元素的元素后一个元素变为这个元素的下一个元素
        :param index:
        :param val:
        :return:
        """
        index_node = self.get(index)
        new_node = Node(val=val, next=index_node.next)
        index_node.next = new_node.next

    # 删除指定位置元素
    def deleteAtIndex(self, index):
        """
        思路 找到这个元素 把该元素的后一个元素变为原本的后两个元素
        :param index:
        :return:
        """
        index_node = self.get(index)
        index_node.next = index_node.next.next


MyLinkedList = MyLinkedList()
