'''Single Linked List Creation and adding elements to it'''

class Single_Linked_List_Init_Node():
    '''creates initial empty node for linked list'''
    def __init__(self):
        self.headval = None

class AddNode():
    '''adds new node to the list'''
    print('adding node to the linked list..')
    def __init__(self, data=None):
        self.data = data
        self.next = None

def printList(head):
    '''prints all elements of given list'''
    print('\nElements of linked list are: ', end = '')
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("NULL")

# create first empty node
List1 = Single_Linked_List_Init_Node()

# start adding elements to it
List1.headval = AddNode(1)

sec_ele = AddNode(2)
third_ele = AddNode(3)

# Link them
List1.headval.next = sec_ele
sec_ele.next = third_ele

# considering third_ele as last node, assign None to its next.
third_ele.next = None

# display so far built linked list
printList(List1.headval)

# Adding an element at the start of linked list
new_init = AddNode(0)
new_init.next = List1.headval

# display so far built linked list
printList(new_init)

# Adding an element in the middle of linked list
mid = AddNode(2.5)
mid.next=third_ele
sec_ele.next=mid

# display so far built linked list
printList(new_init)

# Adding an element at the end of linked list
last_ele = AddNode(4)
third_ele.next = last_ele
last_ele.next = None

# display so far built linked list
printList(new_init)