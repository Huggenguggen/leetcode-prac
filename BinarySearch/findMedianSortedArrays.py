from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
  A, B = nums1, nums2
  size1, size2 = len(nums1), len(nums2)

  total_size = size1 + size2

  #if total_size % 2 == 1, take the (len - 1) / 2
  #if total_size % 2 == 0, take the ((len) / 2) + (((len) / 2) - 1) over 2
  target = total_size // 2

  if len(B) < len(A):
    A, B = B, A
  
  l, r = 0, len(A) - 1
  while True:
    i = (l + r) // 2
    j = target - i - 2

    Aleft = A[i] if i >= 0 else float("-inf")
    Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
    Bleft = B[j] if j >= 0 else float("-inf")
    Bright = B[j + 1] if (j + 1) < len(B) else float("int")

    if Aleft <= Bright and Bleft <= Aright:
      if total_size % 2:
        return min(Aright, Bright)

      return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
    elif Aleft > Bright:
        r = i - 1
    else:
        l = i + 1


def findMedianSortedArrays2(nums1, nums2):
  final = sorted(nums1 + nums2)

  return final[len(final) // 2] if len(final) % 2 == 1 else (final[len(final) // 2] + final[(len(final) // 2) - 1]) / 2


def test_func():
  assert findMedianSortedArrays([1,3], [2]) == 2.00000
  assert findMedianSortedArrays([1,2], [3,4]) == 2.500000
  assert findMedianSortedArrays2([1,3], [2]) == 2.00000
  assert findMedianSortedArrays2([1,2], [3,4]) == 2.500000


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")