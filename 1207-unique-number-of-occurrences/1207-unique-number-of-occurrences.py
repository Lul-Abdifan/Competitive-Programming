class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = {}
        set_ = set()
        for num in arr:
            if num in dict_:
                dict_[num] +=1
            else:
                dict_[num] =1
        for num in dict_.values():
            if num in set_:
                return False
            else:
                set_.add(num)
        return True        
                
                
        