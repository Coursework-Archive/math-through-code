def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
             or NaN if L is empty.
    """
    if not L:
        return float('nan')

    lengths = [len(s) for s in L]
    mean = sum(lengths) / len(lengths)

    variance = sum((x - mean) ** 2 for x in lengths) / len(lengths)
    return variance ** 0.5



L = ['a', 'z', 'p']
#Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
print('Test case 1:', stdDevOfLengths(L))


#Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print('Test case 2:', stdDevOfLengths(L))