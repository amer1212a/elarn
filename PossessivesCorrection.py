import spacy
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")
possessives = ["my", "your", "his", "her", "its", "our", "their"]


def PossessivesNouns(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if i + 1 < len(tagged) and str(tagged[i + 1][2]) == "NOUN":
            if str(tagged[i][1]) == "NN":
                res.append(str(tagged[i][0]) + "'s " + str(tagged[i + 1][0]))
            elif str(tagged[i][1]) == "NNS" and str(tagged[i][0]).lower().endswith("s"):
                res.append(str(tagged[i][0]) + "' " + str(tagged[i + 1][0]))
            elif str(tagged[i][1]) == "NNS" and not str(tagged[i][0]).lower().endswith(
                "s"
            ):
                res.append(str(tagged[i][0]) + "'s " + str(tagged[i + 1][0]))
    return res


def PossessivesAdjective(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if str(tagged[i][0]).lower() in possessives and str(tagged[i][5]) != "NOUN":
            res.append(
                "ERROR: You need to use a noun after possessives ("
                + str(tagged[i][0])
                + ")"
            )
        if (
            str(tagged[i][0]).lower() in possessives
            and str(tagged[i][1]) != "PRP$"
            and i - 1 > 0
            and str(tagged[i - 1][2]) == "NOUN"
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i - 1][0]))
        if (
            str(tagged[i][0]).lower() in possessives
            and str(tagged[i][1]) != "PRP$"
            and str(tagged[i][5]) == "NOUN"
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))

    return res


def Possessives_Checker(sentence):
    # print(sentence)
    # b = TextBlob(sentence)
    # sentence = str(b.correct())
    # print(sentence)
    doc = nlp(sentence)
    tagged = [
        (
            word,
            word.tag_,
            word.pos_,
            word.head.text,
            word.head.tag_,
            word.head.pos_,
            word.dep_,
            [child for child in word.head.children],
        )
        for word in doc
    ]
    Possessives = {}

    Possessives["Possessives Nouns"] = PossessivesNouns(tagged)
    Possessives["Possessives Adjective"] = PossessivesAdjective(tagged)

    return Possessives


# sentence3 = "He's broken his great."
# res3 = Possessives_Checker(sentence3)
# print(res3)

# sentence3 = "He's broken arm his."
# res3 = Possessives_Checker(sentence3)
# print(res3)

# sentence3 = "his friends car."
# res3 = Possessives_Checker(sentence3)
# print(res3)

# sentence3 = "a shoe shop."
# res3 = Possessives_Checker(sentence3)
# print(res3)