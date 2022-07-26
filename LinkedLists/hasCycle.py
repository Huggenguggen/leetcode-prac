from typing import Optional
from ListNode import ListNode

def hasCycle(head: Optional[ListNode]) -> bool:
  if not head:
    return False
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

if __name__ == "__main__":
  recNode = ListNode(4)
  testList = ListNode(3, ListNode(2, ListNode(0, recNode)))
  recNode.next = testList
  print(hasCycle(testList))
