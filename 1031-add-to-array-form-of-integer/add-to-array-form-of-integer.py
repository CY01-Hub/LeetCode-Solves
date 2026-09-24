class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        ans = []
        point = len(num)-1
        carry = 0

        while point >= 0 or k > 0:
            add = 0
            if point >= 0:
                add = num[point]
            
            dig = k % 10
            res = add + dig + carry
            sto = res % 10
            carry = res // 10
            
            ans.append(sto)
            point -= 1
            k //= 10

        if carry > 0:
            ans.append(carry)

        return ans[::-1]