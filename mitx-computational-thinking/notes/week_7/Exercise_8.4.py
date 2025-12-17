import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    success = 0
    for _ in range(numTrials):
        bucket = ['R', 'R', 'R', 'G', 'G', 'G']
        draw = random.sample(bucket, 3) #draw 3 without replacement
        if draw[0] == draw[1] == draw[2]:
            success += 1
    return success / numTrials

print(noReplacementSimulation(100))
print(noReplacementSimulation(1000))
print(noReplacementSimulation(10000))
print(noReplacementSimulation(50000))