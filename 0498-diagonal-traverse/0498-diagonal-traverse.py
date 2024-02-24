class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        dictionary = {}
        rows = len(mat)
        cols = len(mat[0])
        
        result = []
        
        for i in range(rows):
            for j in range(cols):
                if i + j not in dictionary:
                    
                    dictionary[i + j] = [mat[i][j]]
                else:
                    dictionary[i + j].append(mat[i][j])
                    
                    
        for num in dictionary:
            if num%2 == 0:
                dictionary[num].reverse()
                result += dictionary[num]
            else:
                result += dictionary[num]
        print(result)
        
        return result
                    
                    
                    
                    
                
              
                
       
        