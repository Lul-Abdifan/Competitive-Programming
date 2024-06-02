class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def per(pro,unpro):
            if not unpro:
                # values.append(pro)
                # return 
                return [pro]

            s_no = unpro[0]

            res = []

            for i in range(len(pro) + 1):
                res += per(pro[:i] + [s_no] + pro[i:], unpro[1:])
            return res   
        return per([],nums)    


        