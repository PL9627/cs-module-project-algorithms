'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    newlist = []
    zerolist = []

    for i in arr:
        if not isinstance(i, bool):
            if i == 0:
                zerolist.append(i)
                continue
        newlist.append(i)
    return newlist + zerolist


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")