#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    
    x = head
    cnt = 0
    while x:
    #find length of LL
        x = x.next
        cnt+=1

    if 0<= position <=cnt:
        if not head:
            if position == 0:
                head = SinglyLinkedListNode(data)
                return head

            if position >0:
                print("Can't insert node at the location of this empty list")
                return None
        
        org_head = head

        var = 0
        while head:
            head = head.next
            var+=1
            if var == position-1:
                temp = head.next
                node = SinglyLinkedListNode(data)
                head.next = node
                node.next = temp
                return org_head
    else:
        print("Not possible")
        return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()

