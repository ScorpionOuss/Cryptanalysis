def readCipherText(file):
    """ Read the cipher text from a file and returns
    a string message """
    fp = open(file, "r")
    message = fp.read()
    return message

message = readCipherText("cipherText1.txt")


def clean(message):
    " Clean the message"
    cleaned = ""
    message = message.upper()
    for x in message:
        if getOrd(x) >= 0:
            cleaned += x
    return cleaned

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
INDEX_E = ord("E") - ord("A") + 10

def initializeFreq():
    """ Returns an initialized list of frequencies"""
    return [[i, 0] for i in range(len(ALPHABET))]


def getOrd(x):
    if ord(x) >= ord("A") and ord(x) <= ord("Z"):
        return ord(x) - ord("A") + 10
    elif ord(x) <= ord("9") and ord(x) >= ord("0"):
        return int(x)
    elif x == "_":
        return len(ALPHABET) - 1
    else:
        return -1

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

print(message[:20])
print(ceasar(message))

# Dear Oussama Kaddami,

# At the end of this email you find two ciphertexts, that have been
# prepared exclusively for you. Your task is to find the corresponding
# plaintexts.

# A cryptanalysis is considered successful if you report a reasonably
# large prefix of the plaintext as part of your written solution and
# give a brief description of your analysis.

# Submit your solution at https://canvas.kth.se/courses/31957

# Do not receive or share anything concrete like: code, writeups,
# ciphertexts, plaintexts, etc, but feel free to discuss the generic
# problem with a friend and share ideas.

# In other words, you may work on ideas in pairs, but you must write
# your own implementation, execute solely your own implementation during
# analysis, write your own summary, and submit your own solution.

# Each student receives unique ciphertexts encrypted with unique
# keys. The ciphers can be be broken by systematically applying the
# techniques covered in class.

# Good luck!

# Doug & Sonja

# -------------------------------------------------------------------

# HINTS FOR CIPHERTEXTS 1 AND 2:

# They are encryptions of English plaintexts using the following
# alphabet:

# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_

# In other words, only digits, capital letters, and the
# underscore-character "_" are used. The last letter is used as a
# replacement for space.

# THE CIPHERTEXTS

# Each ciphertext is represented as a number of newline-separated
# rows. You should remove the newlines, i.e., concatenate all the
# individual rows to construct the challenge ciphertext.