if __name__ == '__main__':
    # Take input length
    n = int(input())
    # Splitting the input based on whitespace and converting to int then changing to list finally sorting the gotten list
    arr = sorted(list(map(int, input().split())))
    # check if we have the 2nd largest and break the loop
    for i in range(n, -1, -1):
        if i - 2 >= 0 and arr[i - 2] < arr[i - 1]:
            print(arr[i - 2])
            break
        
    
