def solve(k):
    maximum = 0
    sum = 0
    while k > 0:
        try:
           a,b = map(int,input().split())
           tmp = b - a + sum
           sum +=b
           sum -=a
           maximum = max(tmp,maximum)
        except EOFError:
            break
    return maximum    
        
    


if __name__ == '__main__':
    k = int(input())
    print(solve(k))
