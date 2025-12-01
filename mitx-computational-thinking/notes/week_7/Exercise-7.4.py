def variance(X):
    """Assumes that X is a list of numbers. Returns the variance of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)

def std_dev(X):
    """Assumes that X is a list of numbers. Returns the standard deviation of X"""
    return variance(X)**0.5

def CV(X):
    mean = sum(X)/len(X)
    try:
        return std_dev(X)/mean
    except ZeroDivisionError:
        return float('nan')

a = [1, 2, 3]
b = [11, 12, 13]
c = [0.1, 0.1, 0.1]
d =  [10, 4, 12, 15, 20, 5]

print(CV(a))
print(CV(b))
print(CV(c))
print(CV(d))