'''Single Linked List Creation and adding elements to it'''

class Single_Linked_List_Init_Node():
    '''creates initial empty node for linked list'''
    def __init__(self):
        self.headval = None

class AddNode():
    '''adds new node to the list'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def printList(head):
    '''prints all elements of given list'''
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("NULL")

#create first empty node
List1 = Single_Linked_List_Init_Node()

#start adding elements to it
List1.headval = AddNode(1)

sec_ele = AddNode(2)
third_ele = AddNode(3)

#Link them
sec_ele = List1.headval.next
sec_ele.next = third_ele

#considering third_ele as last node, assign None to its next.
third_ele.next = None

printList(List1.headval)