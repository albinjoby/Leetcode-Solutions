class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        stack = []
        for start, end in intervals:
            if stack and stack[-1][0] <= start and stack[-1][-1] >= end:
                continue
            elif stack and stack[-1][-1] >= start:
                stack[-1][-1] = end
            else:
                stack.append([start,end])
        
        return stack