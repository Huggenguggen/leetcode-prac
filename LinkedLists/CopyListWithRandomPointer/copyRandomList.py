from typing import List, Optional
from Node import Node

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
  Nodemap = {}

  tmp = head
  while tmp:
    newNode = Node(tmp.val)
    Nodemap[tmp] = newNode
    tmp = tmp.next
  
  #now we have the hashmap set up and copies

  dummy = Node()
  newList = dummy
  tmp = head
  while tmp:
    newList.next = Nodemap[tmp]
    newList.next.random = Nodemap[tmp.random]
    newList = newList.next

  return dummy.next

 

