def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_table = {}

    for i in range(length):
        w = weights[i]

        # this is to take care of duplicate items in weights list
        # if there are duplicate items in list, the index of the dupliate will be added to the value of key
        if w in weight_table:
            weight_table[w].append(i)

        else:
            weight_table[w] = [i]

    for key in weight_table:

        total = limit - key

        if total in weight_table:

            if len(weight_table[total]) != 1:
                # the weight or key has a duplicate in array
                # return the array containing the indices and convert to tuple
                return tuple(sorted(weight_table[total], reverse=True))

            else:
                # return value of total and key
                return tuple(sorted((weight_table[total][0], weight_table[key][0]), reverse=True))

    return None
