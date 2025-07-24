class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev = 0
        for start,end in meetings:
            days -= max(0,(end-max(start,prev+1))+1)
            prev = max(prev,end)
        
        return days