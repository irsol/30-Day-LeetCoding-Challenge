# Linked Lists
#
# - linked list consists of nodes
# - each node consists of a value and a pointer to another node
# - the starting node of a linked list is referred to as the header
# - linked list is a chain of values connected with pointers



class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None # the pointer initially points to nothing

class LinkedList:
    def __init__(self):
        self.headval = None

    def ListPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.val)
            printval = printval.next
#if __name__=='__main__':
list1 = LinkedList()
list1.headval = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")
# Link first Node to second node
list1.headval.next = node2

# Link second Node to third node
node2.next = node3
list1.ListPrint()

