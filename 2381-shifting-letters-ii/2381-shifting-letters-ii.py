class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        string = list(s)
        shifts_pref = [0]*(len(s) + 1)
        answer = ""
        
        for i in range(len(shifts)):
         
            if shifts[i][2] == 0:
                shifts_pref[shifts[i][0]] -=1
                shifts_pref[shifts[i][1] + 1] +=1
            else:
                shifts_pref[shifts[i][0]] +=1
                shifts_pref[shifts[i][1] + 1] -=1
                
        for i in range(1,len(shifts_pref)):
            shifts_pref[i] = shifts_pref[i - 1] + shifts_pref[i]
            
            
            
        for i in range(len(string)):
            answer += chr((ord(s[i]) - ord("a") + shifts_pref[i]) % 26 + ord("a"))

        return answer