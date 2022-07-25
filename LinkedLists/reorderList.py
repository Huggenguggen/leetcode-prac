from typing import List, Optional
from ListNode import ListNode

def reorderList(head: Optional[ListNode]) -> None:
  #first find the middle
  mid, end = head, head.next
  while end and end.next:
    mid = mid.next
    end = end.next.next
  
  #reverse other half
  second = mid.next
  prev = mid.next = None
  while second:
    tmp = second.next
    second.next = prev
    prev = second
    second = tmp
  
  first, second = head, prev
  while second:
    tmp1, tmp2 = first.next, second.next
    first.next = second
    second.next = tmp1
    first, second = tmp1, tmp2