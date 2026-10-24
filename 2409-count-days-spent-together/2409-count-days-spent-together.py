class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        if end < start:
            return 0 
        if end == start:
            return 1

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        start_month, start_day = map(int, start.split('-'))
        end_month, end_day = map(int, end.split('-'))

        days = end_day
        if start_month == end_month:
            days -= start_day - 1
        else:
            days += month_days[start_month - 1] - start_day + 1

        for month in range(start_month + 1, end_month):
            days += month_days[month - 1]

        return days