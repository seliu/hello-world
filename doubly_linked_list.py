class DoublyListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or self.head is None: return -1

        cur = self.head
        for _ in range( index ): # go to the index-th node
            if cur.next:
                cur = cur.next
            else: # index out of bound
                return -1
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        cur = DoublyListNode( val )
        if self.head is None:
            self.head = cur
        else:
            cur.next = self.head
            self.head.prev = cur
            self.head = cur

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur = DoublyListNode( val )
        if self.head is None:
            self.head = cur
        else:
            prv = self.head
            while prv.next: # go to the last node
                prv = prv.next
            cur.prev = prv
            prv.next = cur

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0: return
        cur = DoublyListNode( val )
        if self.head:
            prv, nxt = None, self.head
            for _ in range( index ): # go to the index-th node
                if nxt:
                    prv, nxt = nxt, nxt.next
                else: # index out of bound
                    return
            cur.prev, cur.next = prv, nxt
            if nxt: # means it's not the tail
                nxt.prev = cur
            if prv: # means it's not the head
                prv.next = cur
            else:
                self.head = cur
        else:
            if index == 0:
                self.head = cur

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or self.head is None:
            return

        cur = self.head
        for _ in range( index ): # go to the index-th node
            if cur.next:
                cur = cur.next
            else: # index out of bound
                return
        # remove the node
        if cur.next: # means it's not the tail
            cur.next.prev =  cur.prev
        if cur.prev: # means it's not the head
            cur.prev.next = cur.next
        else:
            self.head = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
