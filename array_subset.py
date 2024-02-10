#User function Template for python3
from collections import Counter

def isSubset( a1, a2, n, m):
    
    a1_freq = Counter(a1)
    a2_freq = Counter(a2)
    
    
    
    for num in a2_freq:
        if num not in a1_freq or a2_freq[num] > a1_freq[num]:
            return "No"
    return "Yes"        
        
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
