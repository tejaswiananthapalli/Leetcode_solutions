class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def get_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day
        
        alice_arrive = get_day_of_year(arriveAlice)
        alice_leave = get_day_of_year(leaveAlice)
        bob_arrive = get_day_of_year(arriveBob)
        bob_leave = get_day_of_year(leaveBob)
        
        latest_arrival = max(alice_arrive, bob_arrive)
        earliest_leave = min(alice_leave, bob_leave)
        
        return max(0, earliest_leave - latest_arrival + 1)