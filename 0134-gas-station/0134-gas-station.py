class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = sum(gas) - sum(cost)

        if total < 0:
            return -1

        index = 0
        cur_total = 0

        for i in range(len(gas)):
            cur_total +=gas[i] - cost[i]

            if cur_total < 0:
                cur_total = 0
                index = i + 1
        return index        

        






        