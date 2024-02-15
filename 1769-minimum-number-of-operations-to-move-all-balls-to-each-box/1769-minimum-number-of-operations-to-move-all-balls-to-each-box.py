class Solution:
    def minOperations(self, boxes: str) -> List[int]:
      
        boxes = list(boxes)
        result = []
        
        for i in range(len(boxes)):
            cnt = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    cnt +=abs(j - i)
            result.append(cnt)
            
        return result    
            
                
            
            
            
        
        