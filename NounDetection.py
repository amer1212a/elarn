import spacy

nlp = spacy.load("en_core_web_sm")


def SingularNoun(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["NN"]:
            # if i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() not in ["of"]:
            res.append(str(tagged[i][0]))

    return res


def PluralNoun(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["NNS"] and str(tagged[i][0]).endswith("s"):
            # if i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() not in ["of"]:
            res.append(str(tagged[i][0]))
    return res


def irregularPluralsNoun(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["NNS"] and not str(tagged[i][0]).endswith("s"):
            res.append(str(tagged[i][0]))
    return res


def determine_nouns(sentence):
    doc = nlp(sentence)
    tagged = [
        (
            word,
            word.tag_,
            word.pos_,
            word.head.text,
            word.head.tag_,
            word.head.pos_,
            [child for child in word.head.children],
        )
        for word in doc
    ]
    # print(tagged)
    Nouns = {}
    Nouns["Singular Noun"] = SingularNoun(tagged)
    Nouns["Plural Noun"] = PluralNoun(tagged)
    Nouns["irregular Plurals Noun"] = irregularPluralsNoun(tagged)

    return Nouns


# sentence1 = "Smith received three large sums of money."
# res1 = determine_nouns(sentence1)
# print(res1)
#
# sentence1 = "Computers are very expensive."
# res1 = determine_nouns(sentence1)
# print(res1)
#
# sentence1 = "That's a useful piece of equipment."
# res1 = determine_nouns(sentence1)
# print(res1)
#
# sentence1 = "We ate a lot of food. "
# res1 = determine_nouns(sentence1)
# print(res1)
#
# sentence1 = "the men"
# res1 = determine_nouns(sentence1)
# print(res1)