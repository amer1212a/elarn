import spacy

nlp = spacy.load("en_core_web_sm")


def SpecificDeterminers(tagged):
    res = []
    listofdet = [
        "the",
        "my",
        "your",
        "his",
        "her",
        "its",
        "our",
        "their",
        "whose",
        "this",
        "that",
        "these",
        "those",
    ]
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in listofdet and tagged[i][5] in ["NOUN"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))
    return res


def GeneralDeterminersSingular(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in ["a", "an", "any", "another"]
            and tagged[i][5] in ["NOUN"]
            and str(tagged[i + 1][0]).lower() not in ["lot", "bit", "couple"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))

    return res


def GeneralDeterminersPlural(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["other"] and tagged[i][4] in ["NNS"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))
    return res


def InterrogativeDeterminersSpecific(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["which"] and tagged[i][5] in ["NOUN"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))

    return res


def InterrogativeDeterminersGeneral(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["what"] and tagged[i][5] in ["NOUN"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))
    return res


def QuantifiersCountAndUncountNouns(tagged):
    res = []
    listofQ = ["all", "some", "more", "enough", "no", "any", "most", "less"]
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in listofQ
            and i + 1 < len(tagged)
            and tagged[i + 1][2] in ["NOUN"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

        if (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() in ["a"]
            and str(tagged[i + 1][0]).lower() in ["lot"]
            and str(tagged[i + 2][0]).lower() in ["of"]
            and tagged[i + 3][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["lots"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["plenty"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["heaps"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["loads"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["tons"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() in ["a"]
            and str(tagged[i + 1][0]).lower() in ["load"]
            and str(tagged[i + 2][0]).lower() in ["of"]
            and tagged[i + 3][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
            )

    return res


def QuantifiersCountNouns(tagged):
    res = []
    listofQ = [
        "many",
        "each",
        "either",
        "few",
        "several",
        "both",
        "neither",
        "fewer",
        "every",
    ]
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in listofQ
            and i + 1 < len(tagged)
            and tagged[i + 1][2] in ["NOUN"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["hundreds"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["thousands"]
            and str(tagged[i + 1][0]).lower() in ["of"]
            and tagged[i + 2][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() in ["a"]
            and str(tagged[i + 1][0]).lower() in ["couple", "number"]
            and str(tagged[i + 2][0]).lower() in ["of"]
            and tagged[i + 3][2] in ["NOUN"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
            )

    return res


def QuantifiersUncountNouns(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in ["much"]
            and i + 1 < len(tagged)
            and tagged[i + 1][2] in ["NOUN", "ADJ"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

        if (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() in ["a"]
            and str(tagged[i + 1][0]).lower() in ["bit"]
            and str(tagged[i + 2][0]).lower() in ["of"]
            and tagged[i + 3][2] in ["NOUN", "ADJ"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
            )

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() in ["a"]
            and str(tagged[i + 1][0]).lower() in ["little", "bit"]
            and tagged[i + 2][2] in ["NOUN", "ADJ"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        if (
            i + 4 < len(tagged)
            and str(tagged[i][0]).lower() in ["a"]
            and str(tagged[i + 1][0]).lower() in ["great", "good"]
            and str(tagged[i + 2][0]).lower() in ["deal"]
            and str(tagged[i + 3][0]).lower() in ["of"]
            and tagged[i + 4][2] in ["NOUN", "ADJ"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
                + " "
                + str(tagged[i + 3][0])
            )
    return res


def determine_Determiners(sentence):
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
    Determiners = {}
    Determiners["Specific Determiners"] = SpecificDeterminers(tagged)
    Determiners["General Determiners Singular"] = GeneralDeterminersSingular(tagged)
    Determiners["General Determiners Plural"] = GeneralDeterminersPlural(tagged)
    Determiners[
        "Interrogative Determiners Specific"
    ] = InterrogativeDeterminersSpecific(tagged)
    Determiners["Interrogative Determiners General"] = InterrogativeDeterminersGeneral(
        tagged
    )
    Determiners[
        "Quantifiers with Count And Uncount Nouns"
    ] = QuantifiersCountAndUncountNouns(tagged)
    Determiners["Quantifiers only with Count Nouns"] = QuantifiersCountNouns(tagged)
    Determiners["Quantifiers only with Uncount Nouns"] = QuantifiersUncountNouns(tagged)

    return Determiners


###############
# sentence1 = "would you like a little wine ?"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "could i have a bit of butter ?"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "i will back in a couple of minutes"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "there were hundreds of people at the meeting"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "we have loads of time"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "there was heaps of food"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "we have lots of time"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "there was a lot of food but no drinks"
# res1 = determine_Determiners(sentence1)
# print(res1)

###########
# sentence1 = "What food do you like ?"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "i can not remember which house janet lives in"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "Which restaurant did you go to?"
# res1 = determine_Determiners(sentence1)
# print(res1)

#########
# sentence1 = "A man came this morning and left a parcel"
# res1 = determine_Determiners(sentence1)
# print(res1)

# sentence1 = "Any child can do it"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "i like any fruit"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "would you like another glass of wine"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "helen and a few other friends"
# res1 = determine_Determiners(sentence1)
# print(res1)


##############
# sentence1 = "can you pass me the salt ?"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "whose coat is this ?"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "look at those lovely flowers"
# res1 = determine_Determiners(sentence1)
# print(res1)
#
# sentence1 = "the tallest boy"
# res1 = determine_Determiners(sentence1)
# print(res1)
