#
# This is my first time implementing a singly linked list. It's always interesting to record the learning progress.
#
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.head = None
        self.data_length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.data_length:
            return -1
        current_node_idx = self.head
        for _ in range( index ):
            current_node_idx = self.data[ current_node_idx ][ 1 ]
        return self.data[ current_node_idx ][ 0 ]
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = [ val, self.head ]
        self.data.append( node )
        self.head = len( self.data ) - 1
        self.data_length += 1
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex( self.data_length, val )
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.data_length:
            return
        if index == 0:
            self.addAtHead( val )
            return
        # go to the previous node of insertion index
        prev_node_idx = None
        curr_node_idx = self.head
        for _ in range( index ):
            prev_node_idx = curr_node_idx
            curr_node_idx = self.data[ prev_node_idx ][ 1 ]
        new_node = [ val, self.data[ prev_node_idx ][ 1 ] ]
        self.data.append( new_node )
        self.data[ prev_node_idx ][ 1 ] = len( self.data ) - 1
        self.data_length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.data_length:
            return
        # go to the previous node of deletion index
        prev_node_idx = None
        curr_node_idx = self.head
        for _ in range( index ):
            prev_node_idx = curr_node_idx
            curr_node_idx = self.data[ prev_node_idx ][ 1 ]
        self.data[ prev_node_idx ][ 1 ] = self.data[ curr_node_idx ][ 1 ]
        self.data_length -= 1
