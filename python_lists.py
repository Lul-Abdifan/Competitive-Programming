if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range(N):
        commands = list(input().split())
        if commands[0] == "insert":
            lists.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            print(lists)
        
        elif commands[0] == "remove":
            lists.remove(int(commands[1]))    
        elif commands[0] == "append":
            lists.append(int(commands[1]))
        elif commands[0] == "sort":
            lists.sort()
        elif commands[0] == "pop":
            lists.pop()
        else:
            lists.reverse()      
                          
            
    
