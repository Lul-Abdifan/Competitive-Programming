class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        elt1,elt2,cnt1,cnt2 = None,None,0,0
       
        for num in nums:
            if cnt1 == 0 and num != elt2:
                elt1 = num
                cnt1 = 1
            
            elif num == elt1:
                cnt1 +=1
            elif cnt2 == 0 and num != elt1:
                elt2 = num
                cnt2 = 1
            elif  num == elt2:
                cnt2 +=1
            else:
                cnt1 -=1
                cnt2 -=1
                 
        
        
        cnt1 = 0
        cnt2 = 0
        output = []
        for num in nums:
            if num == elt1 and elt1 not in output:
                cnt1 +=1
                if cnt1 > math.floor(len(nums)/3):
                   output.append(elt1)
            if num == elt2 and elt2 not in output:
                cnt2 +=1
                if cnt2 > math.floor(len(nums)/3):
                   output.append(elt2)    
        return list(set(output))       
        
        
