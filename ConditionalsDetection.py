import spacy
from PresentTenseDetection import *
from FutureTenseDetection import *
from PastTenseDetection import *


def TheZeroConditional(tagged):
    index = None
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() == "if":
            for j in range(len(tagged) - i):
                x = i + j
                if str(tagged[x][0]) == ",":
                    index = x
                    break
            # reverse if conditional
            if index == None:
                sublist = tagged[i + 1 : len(tagged)]
                simplepresent1 = PresentSimple(sublist)
                if len(simplepresent1) == 1:
                    sublist = tagged[0:i]
                    simplepresent2 = PresentSimple(sublist)
                    if len(simplepresent2) == 1:
                        res.append(
                            simplepresent2[0]
                            + " , "
                            + str(tagged[i][0])
                            + " "
                            + simplepresent1[0]
                        )
                        return res
            else:
                sublist = tagged[i + 1 : index + 1]
                simplepresent1 = PresentSimple(sublist)
                if len(simplepresent1) == 1:
                    sublist = tagged[index + 1 : len(tagged)]
                    simplepresent2 = PresentSimple(sublist)
                    if len(simplepresent2) == 1:
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + simplepresent1[0]
                            + " , "
                            + simplepresent2[0]
                        )
    return res


def TheFirstConditional(tagged):
    index = None
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() == "if":
            for j in range(len(tagged) - i):
                x = i + j
                if str(tagged[x][0]) == ",":
                    index = x
                    break
            # reverse if conditional
            if index == None:
                sublist = tagged[i + 1 : len(tagged)]
                simplepresent = PresentSimple(sublist)
                if len(simplepresent) == 1:
                    sublist = tagged[0:i]
                    simplefuture = SimpleFuture(sublist)
                    if len(simplefuture) == 1:
                        res.append(
                            simplefuture[0]
                            + " , "
                            + str(tagged[i][0])
                            + " "
                            + simplepresent[0]
                        )
                        return res
            else:
                sublist = tagged[i + 1 : index + 1]
                simplepresent1 = PresentSimple(sublist)
                if len(simplepresent1) == 1:
                    sublist = tagged[index + 1 : len(tagged)]
                    simplefuture = SimpleFuture(sublist)
                    if len(simplefuture) == 1:
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + simplepresent1[0]
                            + " , "
                            + simplefuture[0]
                        )
    return res


def wouldSecondFormGrammar(subtagged):
    res = []
    for i in range(len(subtagged)):
        if subtagged[i][1] in ["MD"]:
            if i + 1 < len(subtagged) and subtagged[i + 1][1] in ["VB"]:
                res.append(str(subtagged[i][0]) + " " + str(subtagged[i + 1][0]))

        if (
            subtagged[i][1] in ["MD"]
            and i + 2 < len(subtagged)
            and subtagged[i + 1][1] in ["RB"]
            and subtagged[i + 2][1] in ["VB"]
        ):
            res.append(
                str(subtagged[i][0])
                + " "
                + str(subtagged[i + 1][0])
                + " "
                + str(subtagged[i + 2][0])
            )
    return res


def TheSecondConditional(tagged):
    index = None
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() == "if":
            for j in range(len(tagged) - i):
                x = i + j
                if str(tagged[x][0]) == ",":
                    index = x
                    break
            # reverse if conditional
            if index == None:
                sublist = tagged[i + 1 : len(tagged)]
                pastsimple = PastSimple(sublist)
                if len(pastsimple) >= 1:
                    sublist = tagged[0:i]
                    wouldgrammar = wouldSecondFormGrammar(sublist)
                    if len(wouldgrammar) >= 1:
                        res.append(
                            str(wouldgrammar[0])
                            + " , "
                            + str(tagged[i][0])
                            + " "
                            + str(pastsimple[0])
                        )
                        return res
            else:
                sublist = tagged[i + 1 : index + 1]
                pastsimple = PastSimple(sublist)
                if len(pastsimple) >= 1:
                    sublist = tagged[index + 1 : len(tagged)]
                    wouldgrammar = wouldSecondFormGrammar(sublist)
                    if len(wouldgrammar) >= 1:
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(pastsimple[0])
                            + " , "
                            + str(wouldgrammar[0])
                        )
    return res


def wouldThirdFormGrammar(subtagged):
    res = []
    for i in range(len(subtagged)):
        if subtagged[i][1] in ["MD"]:
            if (
                i + 2 < len(subtagged)
                and str(subtagged[i + 1][0]).lower() == "have"
                and subtagged[i + 2][1] in ["VBN"]
            ):
                res.append(
                    str(subtagged[i][0])
                    + " "
                    + str(subtagged[i + 1][0])
                    + " "
                    + str(subtagged[i + 2][0])
                )

            if (
                i + 3 < len(subtagged)
                and subtagged[i + 1][1] in ["RB"]
                and str(subtagged[i + 2][0]).lower() == "have"
                and subtagged[i + 3][1] in ["VBN"]
            ):
                res.append(
                    str(subtagged[i][0])
                    + " "
                    + str(subtagged[i + 1][0])
                    + " "
                    + str(subtagged[i + 2][0])
                    + " "
                    + str(subtagged[i + 3][0])
                )
    return res


def TheThirdConditional(tagged):
    index = None
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() == "if":
            for j in range(len(tagged) - i):
                x = i + j
                if str(tagged[x][0]) == ",":
                    index = x
                    break
            # reverse if conditional
            if index == None:
                sublist = tagged[i + 1 : len(tagged)]
                pastsimple = PastPerfect(sublist)
                if len(pastsimple) >= 1:
                    sublist = tagged[0:i]
                    wouldgrammar = wouldThirdFormGrammar(sublist)
                    if len(wouldgrammar) >= 1:
                        res.append(
                            wouldgrammar[0]
                            + " , "
                            + str(tagged[i][0])
                            + " "
                            + pastsimple[0]
                        )
                        return res
            else:
                sublist = tagged[i + 1 : index + 1]
                pastsimple = PastPerfect(sublist)
                if len(pastsimple) >= 1:
                    sublist = tagged[index + 1 : len(tagged)]
                    wouldgrammar = wouldThirdFormGrammar(sublist)
                    if len(wouldgrammar) >= 1:
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + pastsimple[0]
                            + " , "
                            + wouldgrammar[0]
                        )
    return res


nlp = spacy.load("en_core_web_sm")


def ConditionalDet(sentence):
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
    # print("")
    Conditionals = {}
    Conditionals["TheZeroConditional"] = TheZeroConditional(tagged)
    Conditionals["TheFirstConditional"] = TheFirstConditional(tagged)
    Conditionals["TheSecondConditional"] = TheSecondConditional(tagged)
    Conditionals["TheThirdConditional"] = TheThirdConditional(tagged)
    return Conditionals


# sentence1 = "If I'm late for dinner, they start eating without me."
# res1 = ConditionalDet(sentence1)
# print(res1)


# print("TheSecondConditional")
# sentence = "She would travel all over the world if she were rich."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheSecondConditional(tagged)
# print(res)
# print("-------------------")
# sentence = "If I met the Queen of England, I would say hello."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheSecondConditional(tagged)
# print(res)
#
#
# print("--------------------------------------------------------------------------------")
# print("TheThirdConditional")
# sentence = "If she had studied, she would have passed the exam."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheThirdConditional(tagged)
# print(res)
#
# print("-----------------------------------------------------------")
# print("The First Conditional")
# sentence = "She'll be late if the train is late."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheFirstConditional(tagged)
# print(res)
# print("-------------------")
# sentence = "If it rains, I won't go to the park."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheFirstConditional(tagged)
# print(res)
# print("---------------------------------------------------------")
# print("TheZeroConditional")
# sentence = "If babies are hungry, they cry."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheZeroConditional(tagged)
# print(res)

# wraning
# sentence = "Snakes bite if they are scared."
# doc = nlp(sentence)
# tagged = [(word, word.tag_, word.pos_) for word in doc]
# print(tagged)
# res = TheZeroConditional(tagged)
# print(res)