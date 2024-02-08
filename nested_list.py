if __name__ == '__main__':
    lists = []
    
    # append the element to the lists
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lists.append([name,score])
    
    # find the second-lowest score on the list
    second_lowest_no = sorted(set(lists[i][1] for i in range(len(lists))))[1]
    
    # append the array of the second-lowest score to the result array
    result = [name for name,score in lists if score == second_lowest_no]
    result.sort()
    
    # print out alphabetically
    for std in result:
        print(std)
            
            
        
    
    
    
    
