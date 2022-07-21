from typing import Optional
from ListNode import ListNode

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    
    while curr: 
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev