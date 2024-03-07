import math
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return math.prod(skill)
        
        skill.sort()
        left = 0
        right = len(skill) - 1
        skill_chemistry = 0
        fixed_amount = skill[0] + skill[len(skill) - 1]
        
        if len(skill) == 2:
            return math.prod(skill)
        while left < right:
           skill_amount = skill[left] + skill[right]
        
           if skill_amount != fixed_amount:
                return -1
           else:
                skill_chemistry += skill[left] * skill[right]
                left +=1
                right -=1
        return skill_chemistry       
                
            
        
        