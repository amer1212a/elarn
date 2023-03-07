import spacy

nlp = spacy.load("en_core_web_sm")


def Subject_Pronouns(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["PRP"]
            and i + 1 < len(tagged)
            and tagged[i + 1][2] in ["VERB"]
        ):
            res.append(str(tagged[i][0]))
    return res


def Object_Pronouns(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["PRP"]
            and i - 1 >= 0
            and (tagged[i - 1][2] in ["VERB"] or tagged[i - 1][1] in ["IN"])
        ):
            res.append(str(tagged[i][0]))
    return res


def DemonstrativesPlural(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["these", "those"] and tagged[i][5] in ["NOUN"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))
    return res


def DemonstrativesSingular(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["this", "that"] and tagged[i][5] in ["NOUN"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))
    return res


def OneandOnesafterAdj(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in ["one", "ones"]
            and i - 1 >= 0
            and tagged[i - 1][2] in ["ADJ"]
        ):
            res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))
    return res


def OneandOnesafterThe(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in ["one", "ones"]
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() in ["the"]
        ):
            res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))
    return res


def OneandOnesafterWhich(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][6])
        if (
            str(tagged[i][0]).lower() in ["one", "ones"]
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() in ["which"]
            and "?" in map(str, mymap)
        ):
            res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))
    return res


def ReflexivePronounsSingular(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in [
            "myself",
            "yourself",
            "himself",
            "herself",
            "itself",
        ]:
            res.append(str(tagged[i][0]))
    return res


def ReflexivePronounsPlural(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["ourselves", "yourselves", "themselves"]:
            res.append(str(tagged[i][0]))
    return res


def ReciprocalPronouns(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in ["each"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["other"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
        if (
            str(tagged[i][0]).lower() in ["one"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["another"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
    return res


def IndefinitePronounsPeople(tagged):
    res = []
    listofpronounsforpeople = [
        "anybody",
        "everybody",
        "nobody",
        "somebody",
        "anyone",
        "everyone",
        "someone",
    ]
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in listofpronounsforpeople:
            res.append(str(tagged[i][0]))
        if (
            str(tagged[i][0]).lower() in ["no"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["one"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
    return res


def IndefinitePronounsThings(tagged):
    res = []
    listofpronounsforthings = ["anything", "everything", "nothing", "something"]
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in listofpronounsforthings:
            res.append(str(tagged[i][0]))
    return res


def PronounsInQuestion(tagged):
    res = []
    listofpronouns = ["what", "which", "whose", "who"]
    temp = None
    temp2 = None
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in listofpronouns and tagged[i][5] not in ["NOUN"]:
            if str("?") in map(str, tagged[i][6]):
                res.append(str(tagged[i][0]) + " ?")
        if str(tagged[i][0]).lower() in listofpronouns and tagged[i][5] in ["NOUN"]:
            temp = tagged[i][3]
            temp2 = tagged[i][0]
        elif temp is not None and str(tagged[i][0]) == temp:
            if "?" in map(str, tagged[i][6]):
                temp = None
                res.append(str(temp2) + " ?")
                temp2 = None
    return res


def determine_pronouns(sentence):
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
    modals = {}
    modals["Subject Pronouns"] = Subject_Pronouns(tagged)
    modals["Object Pronouns"] = Object_Pronouns(tagged)
    modals["Demonstratives for singular nouns"] = DemonstrativesSingular(tagged)
    modals["Demonstratives for plural nouns"] = DemonstrativesPlural(tagged)
    modals["One and Ones after Adjective"] = OneandOnesafterAdj(tagged)
    modals["One and Ones after (the)"] = OneandOnesafterThe(tagged)
    modals["One and Ones after (Which)"] = OneandOnesafterWhich(tagged)
    modals["Reflexive Pronouns Singular"] = ReflexivePronounsSingular(tagged)
    modals["Reflexive Pronouns Plural"] = ReflexivePronounsPlural(tagged)
    modals["Reciprocal Pronouns"] = ReciprocalPronouns(tagged)
    modals["Indefinite Pronouns use for People"] = IndefinitePronounsPeople(tagged)
    modals["Indefinite Pronouns use for Things"] = IndefinitePronounsThings(tagged)
    modals["Pronouns In Question"] = PronounsInQuestion(tagged)

    return modals


# sentence1 = "What subjects did you study at school?"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "Which one is yours?"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "What do you want?"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "Whose bags are those?"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "Who did you see?"
# res1 = determine_pronouns(sentence1)
# print(res1)

###############
# sentence1 = "Everybody enjoyed the concert"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "we could see everything"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "Everybody loves sally"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "peter and mary helped each other"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "we sent one another christmas card"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "i fell over and hurt myself"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "you might cut yourselves"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "which one do you want ?"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "helen is the tall one and jane is the short one"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "the red one or the blue one"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "i need some new ones"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "the ones you took in paris"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "this great house"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "these great books"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "that amazing house"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "those bad great people"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "can you help me ?"
# res1 = determine_pronouns(sentence1)
# print(res1)

# sentence1 = "don't take it from us"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "why are you looking at her ?"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
# sentence1 = "give it to him"
# res1 = determine_pronouns(sentence1)
# print(res1)
#
#
# sentence1 = "she is waiting for me"
# res1 = determine_pronouns(sentence1)
# print(res1)
