class Solution:
    def smallestNumber(self, num: int) -> int:

        if num == 0:
            return 0
        

            
        nos = ""
        if num > 0:
            numbers =sorted([int(n) for n in str(num)])
            if 0 in numbers:
                i = 0
                while i < len(numbers):
                    if numbers[i] != 0:
                        numbers[0],numbers[i]= numbers[i],numbers[0]
                        break
                    i +=1    
                    
 
            return int("".join(map(str,numbers)))
                
        else:
            num = -(num)
            numbers =sorted([int(n) for n in str(num)],reverse = True)
            
            return -(int("".join(map(str,numbers))))
            
