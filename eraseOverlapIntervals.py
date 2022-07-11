def eraseOverlapIntervals(intervals):
  if len(intervals) == 1:
    return 0
  
  intervals = list(sorted(intervals))
  print(intervals)
  end = intervals[0][1]
  num_to_remove = 0
  for interval in range(1, len(intervals)):
    curr_start, curr_end = intervals[interval]
    if curr_start < end:
      num_to_remove += 1
      if curr_end < end:
        end = curr_end
    else:
      end = curr_end 
  return num_to_remove

print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))