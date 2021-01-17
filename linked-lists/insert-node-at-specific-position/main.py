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

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    curr = head
    node = SinglyLinkedListNode(data)

    for i in range(position - 1):
        curr = curr.next
    
    node.next = curr.next
    curr.next = node

    return head
    