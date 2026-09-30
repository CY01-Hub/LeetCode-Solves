class Solution:
    def first(self, n, t):
        low = 0
        high = len(n) - 1
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if n[mid] == t:
                ans = mid
                high = mid - 1
            elif n[mid] < t:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

    def last(self, n, t):
        low = 0
        high = len(n) - 1
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if n[mid] == t:
                ans = mid
                low = mid + 1
            elif n[mid] < t:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

    def searchRange(self, n: List[int], t: int) -> List[int]:
        return [self.first(n,t), self.last(n,t)]