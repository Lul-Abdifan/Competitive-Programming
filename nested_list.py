if __name__ == '__main__':
    lists = []
    
    # append the element in the lists
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lists.append([name,score])
    
    # find the second score of the list
    second_lowest_no = sorted(set(lists[i][1] for i in range(len(lists))))[1]
    
    # append the array of the second score to res array
    result = [name for name,score in lists if score == second_lowest_no]
    result.sort()
    
    # print out alphabetically
    for std in result:
        print(std)
            
            
        
    
    
    
    
