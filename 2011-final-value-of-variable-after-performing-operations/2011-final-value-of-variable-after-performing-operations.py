class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        initial = 0
        for opn in operations:
            if opn == "++X" or opn == "X++":
                initial +=1
            else:
                initial -=1
        return initial        
        