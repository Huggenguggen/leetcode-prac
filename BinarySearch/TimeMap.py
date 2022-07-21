class TimeMap:

  def __init__(self) -> None:
    self.map = {}
  
  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.map:
      self.map[key] = []
    self.map[key].append([value, timestamp])

  def get(self, key:str, timestamp: int) -> str:
    pass


  
if __name__ == "__main__":
  obj = TimeMap()
  obj.set("foo", "bar", 1)
  obj.set("foo", "bar2", 4)
  print(obj.map)