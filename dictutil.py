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

