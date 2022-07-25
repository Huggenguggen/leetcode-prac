from typing import List, Optional
from ListNode import ListNode

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    
    while curr: 
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverseListRec(head: Optional[ListNode]) -> Optional[ListNode]:
    return reverseHelper(None, head)

def reverseHelper(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
    if (curr == None): return prev

    newNext = curr.next

    curr.next= prev

    return reverseHelper(curr, newNext)

if __name__ == "__main__":
    test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res_list = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
    if reverseList(test_list).equal(res_list):
        print("Everything passed!")
    else:
        print("Something went wrong")