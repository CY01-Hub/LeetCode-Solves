class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        
        st = 0
        end = len(people) - 1
        count = 0

        while st <= end:
            if people[st] + people[end] <= limit:
                st += 1
                end -= 1
            else:
                end -= 1
            count += 1
        
        return count