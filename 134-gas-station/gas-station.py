class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot=0
        for i in range(len(gas)):
            tot+=gas[i]-cost[i]
        if tot<0:
            return -1
        curr_gas=0
        start_ind=0
        for i in range(len(gas)):
            curr_gas+=gas[i]-cost[i]
            if curr_gas<0:
                start_ind=i+1
                curr_gas=0
        return start_ind
