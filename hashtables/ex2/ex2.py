#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flight = {}
    route = []

    # Your code here

    # create key for each ticket
    for i in range(length):
        key = tickets[i].source
        val = tickets[i].destination

        # make source as key
        flight[key] = val

    # if key is NONE, it's the beginning of route
    key = flight["NONE"]

    # if key has a value of NONE, that the last destination
    # until then, keep adding to route list

    while key != "NONE":
        route.append(key)

        # determine the next destination
        key = flight[key]

    # key has a value of NONE so while loop won't execute
    route.append(key)

    return route
