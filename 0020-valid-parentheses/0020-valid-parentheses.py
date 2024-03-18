class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for val in s:
            if  val =='(' or  val == '{' or  val == '[' or  val == '[':
                stack.append(val)
            else:
                if not stack:
                    return False
                elif stack[-1] =='(' and  val == ')' or  stack[-1] =='[' and val == ']' or stack[-1] =='{' and  val == '}':
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False        
                
                