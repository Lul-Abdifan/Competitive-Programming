class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        unpre = [i for i in range(1,n + 1)]
        def com(pre,unpre,result):
            

            if len(pre) == k:
                result.append(pre)
                return

            if not unpre:
                return   

            next_no = unpre[0]

            com(pre + [next_no],unpre[1:],result) 
            com(pre,unpre[1:],result) 

            return result

               
        return com([],unpre,[])    

        