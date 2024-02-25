class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        cols = len(img[0])
        rows = len(img)
        result_image = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                image_sum = 0
                cnt = 0
                for imr in range(-1,2):
                    for imc in range(-1,2):
                        if 0<= imr + i < rows and 0 <= imc + j < cols:
                            image_sum +=img[imr + i][imc + j]
                            cnt +=1
                result_image[i][j] = image_sum//cnt            
                            
                    

               

        return result_image