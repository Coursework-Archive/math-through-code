def loadFile():
    high = []
    low = []
    with open('julytemps.txt') as inFile:
        for i, line in enumerate(inFile):
            if i < 6:     # skip header rows
                continue

            fields = line.split()
            high.append(float(fields[1]))
            low.append(float(fields[2]))

    return high, low


h, l = loadFile()