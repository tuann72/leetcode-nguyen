from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # NOTE: the input a list of nodes, think of it as a multiple node that is chained together with pointers
        # so this means if you do list1.val it is only the value of that node you are currently on, not the entire list value

        # TODO: create dummy node and a current pointer to it
        # dummy node will point to the head of the actual answer
        # current pointer will point to where we are at, if we try using dummy.next instead of current.next
        # we will lose the head of the list
        dummy = ListNode()
        current = dummy

        # TODO: while list1 and list2 have elements loop through each list and compare
        while list1 and list2:
            # TODO: if list1 value > list2 value
            if list1.val < list2.val:
                # append node to answer (current pointer)
                current.next = list1
                # move to next node in list1
                list1 = list1.next
            else:
                # append node to answer (current pointer)
                current.next = list2
                # move to next node in list2
                list2 = list2.next
            # moves the pointer to the new location that was created from condition
            current = current.next

        # TODO: if one of the list is empty, append the entire other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # return dummy because we have dummy pointing to head of list
        return dummy.next
