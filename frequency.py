ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
INDEX_E = ord("E") - ord("A") + 10

def initializeFreq():
    """ Returns an initialized list of frequencies"""
    return [[i, 0] for i in range(len(ALPHABET))]

def getOrd(x):
    """ Returns the order of the character in the new alphabet"""
    if ord(x) >= ord("A") and ord(x) <= ord("Z"):
        return ord(x) - ord("A") + 10
    elif ord(x) <= ord("9") and ord(x) >= ord("0"):
        return int(x)
    elif x == "_":
        return len(ALPHABET) - 1
    else:
        return -1

def clean(message):
    " Clean the message"
    cleaned = ""
    message = message.upper()
    for x in message:
        if getOrd(x) >= 0:
            cleaned += x
    return cleaned

def readCipherText(file):
    """ Read the cipher text from a file and returns
    a string message """
    fp = open(file, "r")
    message = fp.read()
    return clean(message)

message = readCipherText("cipherTexts\\cipherText1.txt")

message2 = readCipherText("cipherTexts\\cipherText2.txt")





def frequencies(message):
    """ Returns the frequencies of the different letters
    in the alphabet; The alphabet is:
    0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_
    """
    frequency = initializeFreq()
    total = 0
    for x in message:
        order = getOrd(x)
        if order >= 0:
            total += 1
            frequency[order][1] += 1
    frequency = [[x, y/total] for x, y in frequency]
    return sorted(frequency, key=lambda x: - x[1])


def ceasar(message):
    """ Based on the frequency of ** _ ** """
    freqList = frequencies(message)
    print(freqList)
    offset = freqList[0][0] - len(ALPHABET) + 1
    decrypted = ""
    for x in message:
        decrypted += ALPHABET[(getOrd(x) - offset)%len(ALPHABET)]
    print(offset)
    return decrypted