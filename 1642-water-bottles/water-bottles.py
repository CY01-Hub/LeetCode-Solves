class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        while numBottles >= numExchange :
            newBottles = numBottles // numExchange
            remBottles = numBottles % numExchange
            answer = answer + newBottles
            numBottles = newBottles + remBottles
        return answer
