class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '{}->{}'.format(self.val,self.next)


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__head = None

    def getHead(self):
        return self.__head

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1

        if self.__head == None:
            return -1

        p = self.__head
        for _ in range(index):
            if p.next:
                p = p.next
            else:
                return -1
        return p.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        n = Node(val,self.__head)
        self.__head = n

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.__head is None:
            self.__head = Node(val)
            return

        p = self.__head
        while p.next is not None:
            p = p.next

        p.next = Node(val)
        return

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
            return

        if self.__head is None:
            return

        p = self.__head
        for _ in range(index-1):
            if p.next:
                p = p.next
            else:
                return

        n = Node(val)
        if p.next:
            p.next,n.next = n,p.next
        else:
            p.next = n

        return


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0:
            return

        if self.__head is None:
            return
        if index == 0:
            self.__head = self.__head.next
            return

        p = self.__head
        for _ in range(index-1):
            if p.next:
                p = p.next
            else:
                return
        if p.next:
            p.next = p.next.next
        return
