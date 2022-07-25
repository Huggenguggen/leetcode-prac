class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  

  def __str__(self) -> str:
    res = ""
    res += "( " + str(self.val) + " ) -> " + str(self.next) 
    return res
  
  def equal(self, other):
    while self and other and self.val == other.val:
      self = self.next
      other = other.next
    if not self and not other:
      return True
    return False 