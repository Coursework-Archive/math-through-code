###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = sorted(cows.items(), key= lambda x: x[1], reverse=True)
    result = []

    while sorted_cows:
        sublist = []
        totalWeight = 0
        for cow in sorted_cows[:]:
            name, weight = cow
            if totalWeight + weight <= limit:
                sublist.append(name)
                sorted_cows.remove(cow)
                totalWeight += weight
        result.append(sublist)
    return result



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    items = cows.items() if isinstance(cows, dict) else cows
    feasible = (
        p for p in get_partitions(items)
        if all(sum(w for n, w in subset) <= limit for subset in p)
    )
    try:
        best = min(feasible, key=len, default=None)
    except ValueError:
        return []

    return [[name for name, _ in subset] for subset in best]






        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    start = time.time()
    c = greedy_cow_transport(cows, limit)
    end = time.time()
    print("Number of trips returned by greedy_cow_transport:", len(c))
    print("Greedy cow transport took {} seconds.".format(end - start))

    start1 = time.time()
    c1 = brute_force_cow_transport(cows, limit)
    end1 = time.time()
    print("Number of trips returned by greedy_cow_transport:", len(c1))
    print("brute force cow transport took {} seconds.".format(end1 - start1))




compare_cow_transport_algorithms()



