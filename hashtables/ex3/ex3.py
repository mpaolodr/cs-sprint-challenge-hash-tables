def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    nums = {}
    result = []

    # loop through array
    for i in range(len(arrays)):

        # for each array, create keys for values
        for num in arrays[i]:

            # increment counter for each key if duplicate in other array is found
            if num in nums:
                nums[num] += 1

            else:
                nums[num] = 1

    for key in nums:
        # check what numbers are in all arrays
        if nums[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
