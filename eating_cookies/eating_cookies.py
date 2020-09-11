'''
Input: an integer
Returns: an integer
'''
# from functools import lru_cache

def eating_cookies(n):
    # Your code here
    """ if n < 0:
        return 0
    if n == 0:
        return 1

    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3) """
    
    a, b, c = 1, 2, 4
    while n - 1 > 0:
        a, b, c = b, c, a + b + c
        n -= 1
    return a

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
