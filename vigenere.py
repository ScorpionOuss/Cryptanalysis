from frequency import message, message2, ALPHABET
from substitution import getOrd

def addChar(marginals, index, x):
    """
    Appends the character in the index's dictionary
    """
    if x in marginals[index]:
        marginals[index][x] += 1
    else:
        marginals[index][x] = 1

def marginalFreq(l, message):
    """
    Returns the marginal probability distributions
    """
    marginals = [{} for _ in range(l)]
    for index, x in enumerate(message):
        addChar(marginals, index%l, x)
    return marginals


def distance(marginal):
    """ Distance of a probability distribution"""
    size = 0
    dist = 0
    for val in marginal.values():
        size += val
        dist += val**2
    return dist/(size**2)

def totalDistance(marginals):
    """ Computes the global distance by summing
    the distances of marginal distributions """
    globDist = 0
    for marginal in marginals:
        globDist += distance(marginal)
    return globDist


MAX_LENGTH = 25

def indexMax(lista):
    'Rteurns the index of the maximum'
    indexMax = 0
    maximum = -float("inf")
    if not lista:
        return None
    for index, val in enumerate(lista):
        if val > maximum:
            indexMax = index
            maximum = val
    return indexMax

def guessLength(message):
    dist = []
    marginals = []
    for length in range(1, MAX_LENGTH + 1):
        marg = marginalFreq(length, message2)
        marginals.append(marg)
        dist.append(totalDistance(marg))
    period = indexMax(dist) 
    return indexMax(dist), marginals[period] 

def computeOffset(marginal):
    """ Computes the offset of a marginal distribution"""
    sortedM = sorted(marginal.items(), key= lambda x: -x[1])
    return getOrd(sortedM[0][0]) - len(ALPHABET) + 1

def computeOffsets(marginals):
    """ Computes the offsets for the different marginals"""
    offsets = []
    for marginal in marginals:
        offsets.append(computeOffset(marginal))
    return offsets

def vigenereDecrpt(message):
    """ Decrypts the message by:
    Identifying the period and applying
    ceasar decryptuion for each subset"""
    # We need the period and the corresponding marginals
    period, marginals = guessLength(message)
    print(period)
    offsets = computeOffsets(marginals)
    decrypted = ''
    for index, x in enumerate(message):
        decrypted += ALPHABET[(getOrd(x) - offsets[index%(period+1)])%len(ALPHABET)]
    return decrypted

# The found period is 17

fp = open("out\\plainText2.txt", "w")
fp.write(vigenereDecrpt(message2))
