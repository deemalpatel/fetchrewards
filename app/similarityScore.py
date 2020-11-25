def jaccardScore(text1, text2):
    textIntersect = set(text1).intersection(set(text2))
    textUnion = set(text1).union(set(text2))
    return round(len(textIntersect)/len(textUnion),4)


def getSimilarity(text1, text2):
    text1Words = text1.split()
    text2Words = text2.split()
    noOfCommonTerms = 0
    for word in text1Words:
        if word in text2Words:
            noOfCommonTerms+=1

    return round(noOfCommonTerms / len(text2Words),4)


