from matplotlib.pyplot import get
from frequency import frequencies, getOrd, message

def words(message):
    """ Establishes the frequency diagrams of words of length 2 and 3 """
    l = len(message)
    c = 0
    dic2w = {}
    dic3w = {}
    while c < l:
        if message[c] == " ":
            if c + 3 == l or (c + 2 < l and message[c + 3] == ' '):
                word = message[c+1: c+3]
                if  word in dic2w:
                    dic2w[word] += 1
                else:
                    dic2w[word] = 1
            elif c + 4 == l or (c + 4 < l and message[c + 4] == ' '):
                word = message[c+1: c+4]
                if  word in dic3w:
                    dic3w[word] += 1
                else:
                    dic3w[word] = 1              
        c += 1
    return sorted(dic2w.items(), key = lambda x: -x[1]), sorted(dic3w.items(), key = lambda x: -x[1])

def graphs(message):
    """ Establishes frequency Digraphs and trigraphs"""
    c = 0
    di = {}
    tri = {}
    while c <len(message):
        if message[c] == " ":
            c += 1
            continue
        if c + 1 < len(message):
            if message[c + 1] == " ":
                c += 1
                continue
            diM = message[c:c+2] 
            if diM in di:
                di[diM] += 1
            else:
                di[diM] = 1
            if c + 2 < len(message):
                if message[c + 2] == " ":
                    c += 1
                    continue
                triM = message[c:c+3]
                if triM in tri:
                    tri[triM] += 1
                else:
                    tri[triM] = 1
        c += 1
    return sorted(di.items(), key = lambda x: -x[1]), sorted(tri.items(), key = lambda x: -x[1])



def substitution(message):
    """ Cryptanalysises based on the substitution model"""
    freqList = frequencies(message)
    firstFreq = freqList[0][0]
    secondFreq = freqList[1][0]
    decrypted = ''
    for x in message:
        # Replace the most frequent with "_"
        if getOrd(x) == firstFreq:
            decrypted += " "
        # Replace the second most frequent with "E"
        elif getOrd(x) == secondFreq:
            decrypted += "E"
        # Replace the third most frequent with "T"
        elif getOrd(x) == getOrd("O"):
            decrypted += "T"
        # After this first pass
        #  Based on 2 words analysis we perform some 2 and 3 words
        #  length frequency analysis and some digraphs and trigraphs
        #  frequency analysis. Those are done manualy
        # TM -> TO | MB -> OF | RT -> AT
        elif getOrd(x) == getOrd("9"):
            decrypted += "A"
        elif getOrd(x) == getOrd("2"):
            decrypted += "B"
        elif getOrd(x) == getOrd("W"):
            decrypted += "C"
        elif getOrd(x) == getOrd("P"):
            decrypted += "D"
        # E done previously
        elif getOrd(x) == getOrd("B"):
            decrypted += "F"
        elif getOrd(x) == getOrd("4"):
            decrypted += "G"
        elif getOrd(x) == getOrd("Y"):
            decrypted += "H"
        elif getOrd(x) == getOrd("R"):
            decrypted += "I"
        elif getOrd(x) == getOrd("K"):
            decrypted += "J"
        elif getOrd(x) == getOrd("D"):
            decrypted += "K"
        elif getOrd(x) == getOrd("6"):
            decrypted += "L"
        elif getOrd(x) == getOrd("_"):
            decrypted += "M"
        elif getOrd(x) == getOrd("T"):
            decrypted += "N"
        
        elif getOrd(x) == getOrd("M"):
            decrypted += "O"
        
        elif getOrd(x) == getOrd("F"):
            decrypted += "P"
        
        elif getOrd(x) == getOrd("8"):
            decrypted += "Q"
        
        elif getOrd(x) == getOrd("1"):
            decrypted += "R"
        
        elif getOrd(x) == getOrd("V"):
            decrypted += "S"
        # T Done before
        elif getOrd(x) == getOrd("H"):
            decrypted += "U"
        elif getOrd(x) == getOrd("A"):
            decrypted += "V"
        elif getOrd(x) == getOrd("3"):
            decrypted += "W"
        # X is invariant
        elif getOrd(x) == getOrd("Q"):
            decrypted += "Y"
        elif getOrd(x) == getOrd("I"):
            decrypted += "i"
        # Z is missing
        # Numbers are difficult to guess and thus missing           
        else:
            decrypted += x
    # Then we can do 2 letters words
    return decrypted

"""
Ideas: How to optimize and do it in one pass
"""
plain = substitution(message)
out = open("out\\plainText1.txt", "w")
out.write(plain)

