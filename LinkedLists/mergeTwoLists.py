from typing import List, Optional
from ListNode import ListNode

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  dummy = ListNode()
  newList = dummy
  while list1 and list2:
    if list1.val > list2.val:
      newList.next = list2
      list2 = list2.next
    else:
      newList.next = list1
      list1 = list1.next
    newList = newList.next
  if list1:
    newList.next = list1
  elif list2:
    newList.next = list2
  return dummy.next


if __name__ == "__main__":

  print(mergeTwoLists(ListNode(), ListNode()))
  print(mergeTwoLists(ListNode(), ListNode(0)))
  print(mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), 
            ListNode(1, ListNode(3, ListNode(4)))))
  if ((mergeTwoLists(ListNode(), ListNode()).equal(ListNode())) and 
     (mergeTwoLists(ListNode(), ListNode(0)).equal(ListNode(0))) and
     (mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), 
            ListNode(1, ListNode(3, ListNode(4)))).equal(
              ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))))):
            print("Everything passed!")
  else:
    print("Something went wrong")