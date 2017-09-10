#Module1
def dict2list(dct, keylist): return [dct[key] for key in keylist]

def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist, L)}

def listrange2dict(L): return {k:L[k] for k in range(len(L))}

def stringSplitter(inputFile): return list([line.split() for line in list(inputFile)])

def reverseIndex(inputFile):
    lineList = stringSplitter(inputFile)
    dict = {}
    for line in range(len(lineList)):
        for word in lineList[line]:
            if word not in dict:
                s = {line}
                dict[word] = s
            else:
                s = dict[word]
                s.add(line)
                dict[word] = s
    return dict

def orSearch(dict, wordList):
    docNumbers = set()
    for word in wordList:
        if word in dict: docNumbers = docNumbers | dict[word]
    return docNumbers

def andSearch(dict, wordList):
        docNumbers = set()
        wordFound = FalseK
        for word in wordList:
            if word in dict:
                if not wordFound:
                    docNumbers = dict[word]
                    wordFound = True
                    continue
                docNumbers = docNumbers & dict[word]
        return docNumbers



