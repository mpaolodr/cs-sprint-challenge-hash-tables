def has_negatives(a):
    """
    YOUR CODE HERE
    """

    nums = {}
    result = []

    # Your code here

    # loop through "a" and store each value as absolute values
    for num in a:

        if abs(num) in nums:

            #  if abs(num) is already in result, this might be the negative value
            result.append(abs(num))

        else:
            nums[abs(num)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
