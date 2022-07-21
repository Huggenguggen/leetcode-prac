boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10


def maximumUnits(boxTypes, truckSize):
  boxTypes.sort(key=lambda x:x[1], reverse=True)
  idx = 0
  res = 0
  while truckSize > 0 and idx < len(boxTypes):
    boxType = boxTypes[idx]
    print(truckSize)
    if truckSize - boxType[0] >= 0:
      res += boxType[0] * boxType[1]
      truckSize -= boxType[0]
    else:
      res += truckSize * boxType[1]
      truckSize = 0
    idx += 1
  return res


print(maximumUnits(boxTypes, truckSize))