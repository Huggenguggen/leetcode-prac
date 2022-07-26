from typing import List, Optional
from ListNode import ListNode

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  slow, fast = head, head.next
  dummy = ListNode()
  tmp = dummy
  i = n
  while i > 1:
    fast = fast.next
    i -= 1
  
  while fast:
    tmp.next = slow
    slow = slow.next
    fast = fast.next
    tmp = tmp.next
  
  while slow:
    tmp.next = slow.next
    slow = slow.next
    tmp = tmp.next
  
  return dummy.next

if __name__ == "__main__":
  test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
  print(removeNthFromEnd(ListNode(1, ListNode(2)), 1))
  print(removeNthFromEnd(test_list, 2))


  

