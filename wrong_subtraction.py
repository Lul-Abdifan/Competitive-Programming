def solve(number,k):
    while k > 0:
        if number%10 != 0:
            number = number - 1
        else:
            number //=10
        k -=1
    return number    
    


if __name__ == '__main__':
    number,k = map(int,input().split())
    print(solve(number,k))
        
