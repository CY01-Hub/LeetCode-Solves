class Solution:
    def search(self, n: List[int], t: int) -> int:
        low = 0
        high = len(n) - 1

        while low <= high:
            mid = low + (high - low) // 2
        
            if n[mid] == t:
                return mid
        
            if n[low] <= n[mid]:
                if n[low] <= t < n[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        
            else:
                if n[mid] < t <= n[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1