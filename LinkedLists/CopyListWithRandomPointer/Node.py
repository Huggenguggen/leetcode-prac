class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random  

  def __str__(self) -> str:
    res = ""
    res += "( " + str(self.val) + ", " + str(self.random) + " ) -> " + str(self.next) 
    return res
  
  def equal(self, other):
    while self and other and self.val == other.val:
      self = self.next
      other = other.next
    if not self and not other:
      return True
    return False 