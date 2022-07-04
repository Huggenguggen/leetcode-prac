from itertools import accumulate


def calculateMinimumHP(dungeon):
  print(dungeon)
  if len(dungeon) == 1:
    return sum(dungeon[0]) * -1
  if len(dungeon[0]) == 1:
    res = 0
    for i in dungeon:
      res += i[0]
    return res * -1
  initial_hp = dungeon[0][0] * -1
  right_step =  calculateMinimumHP(list(map(lambda x: list(x[1:]), dungeon)))
  down_step = calculateMinimumHP(list(dungeon[1:]))
  return min(initial_hp + right_step, initial_hp + down_step)


print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))