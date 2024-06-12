class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def comToTarget(index,value,comb):
            nonlocal result
            if value == target:
                result.append(comb)
                return 
            if value > target or index >= len(candidates):
                return
            
            comToTarget(index,value + candidates[index],comb + [candidates[index]])   
            comToTarget(index + 1,value,comb)   

            return result
        return comToTarget(0,0,[])    









        