class Solution:
    def store(self):
        n = int(input())
        phone_nos = {}
        
        for _ in range(n):
            contact = input().split()
            phone_nos[contact[0]] = int(contact[1])
        
        return phone_nos

if __name__ == "__main__":
    sol = Solution()
    phone_book = sol.store()

    
    
        
    while True:
        try:
           input_value = input()
           if input_value in phone_book:
              print(input_value + "=" + str(phone_book[input_value]))
           else:
              print("Not found")    
        except EOFError:
            break
            
        

    
