# Python code to find Lexicographically largest permutation 
# by sequentially inserting Array elements at ends

from collections import deque

def largestPermutation(arr):
    n = len(arr)
    
    dq = deque()
    dq.append(arr[0])
    
    for i in range(1, n):
        if arr[i] >= dq[0]:
            dq.appendleft(arr[i])
        else:
            dq.append(arr[i])
    
    return list(dq)

if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    res = largestPermutation(arr)
    for num in res:
        print(num, end=" ")
    print()
