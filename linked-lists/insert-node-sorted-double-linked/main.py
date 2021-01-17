#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    curr = head
    prev = head
    node = DoublyLinkedListNode(data)

    while curr.data < node.data:
        prev = curr
        curr = curr.next
        if curr is None:
            break


    if curr is None:
        prev.next = node
        node.prev = prev
        curr = prev
    else:
        node.prev = curr.prev
        if curr.prev is not None:
            curr.prev.next = node
        curr.prev = node
        node.next = curr
    
    while curr.prev is not None:
        curr = curr.prev

    return curr