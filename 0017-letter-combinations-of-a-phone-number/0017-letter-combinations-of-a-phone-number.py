class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicts = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z'],
        }

        def l_conb(pre,unpre,results):
            if not unpre:
                results.append(pre)
                return


            f_char = unpre[0]

            for char in dicts[f_char]:
                  l_conb(pre + char,unpre[1:],results)
            return results
        return l_conb("",digits,[])          
























        