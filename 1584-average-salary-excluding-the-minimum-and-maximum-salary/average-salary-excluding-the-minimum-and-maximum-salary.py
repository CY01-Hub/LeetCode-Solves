class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        store = salary[1 : len(salary)-1]
        print(store)
        ans = sum(store)/len(store)
        return ans