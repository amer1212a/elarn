import spacy
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")
Subject = ["i", "you", "we", "they", "he", "she", "it"]
Object = ["me", "you", "him", "her", "it", "us", "them"]


def SubjectPronouns(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if str(tagged[i][0]).lower() in Subject and tagged[i][5] not in ["VERB", "ADP"]:
            res.append(
                "ERROR: You need to use a verb after subject Pronouns ("
                + str(tagged[i][0])
                + ")"
            )

    return res


def ObjectPronouns(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in Object
            and str(tagged[i][6]) == "dobj"
            and i - 1 >= 0
            and tagged[i - 1][2] not in ["VERB", "ADP"]
        ):
            res.append(
                "ERROR: You need to use verb or prepositions before the pronoun object ("
                + str(tagged[i][0])
                + ")"
            )

    return res


def Demonstratives(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["this", "that"]
            and str(tagged[i][6]) not in ["nsubj","dobj"]
            and str(tagged[i][4]) != "NN"
        ):
            res.append(
                "ERROR: You need to use singular nouns after " + str(tagged[i][0])
            )
        elif str(tagged[i][0]).lower() in ["this", "that"] and str(
            tagged[i][3]
        ).lower() not in ["is", "'s"] and str(
            tagged[i][5]
        ) not in ["VERB"]:
            res.append(str(tagged[i][0]) + " is")

        if (
            str(tagged[i][0]).lower() in ["these", "those"]
            and str(tagged[i][6]) not in ["nsubj" , "dobj"]
            and str(tagged[i][4]) != "NNS"
        ):
            res.append("ERROR: You need to use plural nouns after " + str(tagged[i][0]))
        elif str(tagged[i][0]).lower() in ["these", "those"] and str(
            tagged[i][3]
        ).lower() not in ["are"] and str(
            tagged[i][5]
        ) not in ["VERB"]:
            res.append(str(tagged[i][0]) + " are")

    return res


def OneandOnes(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if str(tagged[i][0]).lower() in ["one", "ones"] and (
            (
                i - 1 >= 0
                and str(tagged[i - 1][2]) != "ADJ"
                and str(tagged[i - 1][0]).lower() not in ["the", "which"]
            )
            or i - 1 < 0
        ):
            res.append(
                "ERROR: You need to add adjective OR (the) before " + str(tagged[i][0])
            )

    return res


def Pronouns_Checker(sentence):
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
    # print(tagged)
    Pronouns = {}

    Pronouns["Subject Pronouns"] = SubjectPronouns(tagged)
    Pronouns["Object Pronouns"] = ObjectPronouns(tagged)
    Pronouns["Demonstratives"] = Demonstratives(tagged)
    Pronouns["One and Ones"] = OneandOnes(tagged)

    return Pronouns


# sentence3 = "I need some ones."
# res3 = Pronouns_Checker(sentence3)
# print(res3)


# sentence3 = "Jane is the one."
# res3 = Pronouns_Checker(sentence3)
# print(res3)


# sentence3 = "ones you took in Paris."
# res3 = Pronouns_Checker(sentence3)
# print(res3)


# sentence3 = "We have lived in this for twenty years."
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "Have you read all of these ?"
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "Who lives in that ?"
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "Who are those ?"
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "This a nice cup of tea."
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "These my friends."
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "Those very expensive shoes."
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# sentence3 = "that Rebecca's house over there."
# res3 = Pronouns_Checker(sentence3)
# print(res3)


# I'll get it for you.
# sentence3 = "I'll get it you."
# res3 = Pronouns_Checker(sentence3)
# print(res3)

# I like your dress.
# sentence3 = "I your dress."
# res3 = Pronouns_Checker(sentence3)
# print(res3)
