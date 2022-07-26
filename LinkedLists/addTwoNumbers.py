from typing import Optional
from ListNode import ListNode

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  dummy = ListNode(0)
  res = dummy
  carry = 0
  while l1 and l2:
    total = l1.val + l2.val + carry
    number = total % 10
    res.next = ListNode(number)
    carry = total // 10
    res = res.next
    l1 = l1.next
    l2 = l2.next  

  while l1:
    total = l1.val + carry
    number = total % 10
    res.next = ListNode(number)
    carry = total // 10
    res = res.next
    l1 = l1.next
  while l2:
    total = l2.val + carry
    number = total % 10
    res.next = ListNode(number)
    carry = total // 10
    res = res.next
    l2 = l2.next

  if carry != 0:
    res.next = ListNode(carry)

  return dummy.next
  



if __name__ == "__main__":
  firstNum = ListNode(2, ListNode(4, ListNode(3)))
  secondNum = ListNode(5, ListNode(6, ListNode(4)))

  thirdNum = ListNode(0)
  fourthNum = ListNode(0)

  fifthNum = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))) 
  sixthNum = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

  print(addTwoNumbers(firstNum, secondNum))
  print(addTwoNumbers(thirdNum, fourthNum))
  print(addTwoNumbers(fifthNum, sixthNum))