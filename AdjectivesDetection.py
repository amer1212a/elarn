import spacy

nlp = spacy.load("en_core_web_sm")


##############some of adj end with -ed , the tag was VBN instaed of JJ , this error
##### (good) error


def Adjectives(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["JJ"]
            and tagged[i][2] in ["ADJ"]
            and not (
                str(tagged[i][0]).lower().endswith("ed")
                and str(tagged[i][0]).lower().endswith("ing")
            )
        ):
            res.append(str(tagged[i][0]))

    return res


def AdjectivesendwithEDandING(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["JJ"]
            and tagged[i][2] in ["ADJ"]
            and (
                str(tagged[i][0]).lower().endswith("ed")
                or str(tagged[i][0]).lower().endswith("ing")
            )
        ):
            res.append(str(tagged[i][0]))

    return res


def ComparativeAdjectives(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["JJR"]:
            res.append(str(tagged[i][0]))
        if (
            i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in ["more"]
            and tagged[i + 1][1] in ["JJ"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

    return res


def SuperlativeAdjectives(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["JJS"]:
            if i - 1 >= 0 and str(tagged[i - 1][0]).lower() in ["the"]:
                res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))
            else:
                res.append(str(tagged[i][0]))
        if (
            i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in ["most"]
            and tagged[i + 1][1] in ["JJ"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

    return res


def IntensifiersWithAdjectives(tagged):
    res = []
    listofintensifiers = [
        "very",
        "really",
        "extremely",
        "amazingly",
        "particularly",
        "remarkably",
        "unusually",
        "exceptionally",
        "incredibly",
        "absolutely",
        "completely",
        "totally",
        "utterly",
        "quite",
    ]
    for i in range(len(tagged)):
        if (
            str(tagged[i][0]).lower() in listofintensifiers
            and i + 1 < len(tagged)
            and tagged[i + 1][1] in ["JJ"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
        if (
            i + 1 < len(tagged)
            and tagged[i][1] in ["JJ"]
            and str(tagged[i + 1][0]).lower() in ["enough"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

    return res


def IntensifiersWithComparativeAdjectives(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["JJR"]
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() in ["much", "far"]
        ):
            res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))

        if (
            tagged[i][1] in ["JJR"]
            and i - 2 >= 0
            and str(tagged[i - 1][0]).lower() in ["lot"]
            and str(tagged[i - 2][0]).lower() in ["a"]
        ):
            res.append(
                str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

        if (
            tagged[i][1] in ["JJR"]
            and i - 3 >= 0
            and str(tagged[i - 1][0]).lower() in ["lot"]
            and str(tagged[i - 2][0]).lower() in ["a"]
            and str(tagged[i - 3][0]).lower() in ["quite"]
        ):
            res.append(
                str(tagged[i - 3][0])
                + " "
                + str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

        if (
            tagged[i][1] in ["JJR"]
            and i - 3 >= 0
            and str(tagged[i - 1][0]).lower() in ["deal"]
            and str(tagged[i - 2][0]).lower() in ["great"]
            and str(tagged[i - 3][0]).lower() in ["a"]
        ):
            res.append(
                str(tagged[i - 3][0])
                + " "
                + str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

        if (
            tagged[i][1] in ["JJR"]
            and i - 3 >= 0
            and str(tagged[i - 1][0]).lower() in ["deal", "bit"]
            and str(tagged[i - 2][0]).lower() in ["good"]
            and str(tagged[i - 3][0]).lower() in ["a"]
        ):
            res.append(
                str(tagged[i - 3][0])
                + " "
                + str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

        if (
            tagged[i][1] in ["JJR"]
            and i - 3 >= 0
            and str(tagged[i - 1][0]).lower() in ["bit"]
            and str(tagged[i - 2][0]).lower() in ["fair"]
            and str(tagged[i - 3][0]).lower() in ["a"]
        ):
            res.append(
                str(tagged[i - 3][0])
                + " "
                + str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

    return res


def IntensifiersWithSuperlativeAdjectives(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["JJS"]
            and i - 2 >= 0
            and str(tagged[i - 1][0]).lower() in ["the"]
            and str(tagged[i - 2][0]).lower() in ["easily", "much"]
        ):
            res.append(
                str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

        if (
            tagged[i][1] in ["JJS"]
            and i - 3 >= 0
            and str(tagged[i - 1][0]).lower() in ["the"]
            and str(tagged[i - 2][0]).lower() in ["far"]
            and str(tagged[i - 3][0]).lower() in ["by"]
        ):
            res.append(
                str(tagged[i - 3][0])
                + " "
                + str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
            )

        if (
            i - 3 >= 0
            and str(tagged[i - 1][0]).lower() in ["the"]
            and str(tagged[i - 2][0]).lower() in ["far"]
            and str(tagged[i - 3][0]).lower() in ["by"]
            and i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in ["most"]
            and tagged[i + 1][1] in ["JJ"]
        ):
            res.append(
                str(tagged[i - 3][0])
                + " "
                + str(tagged[i - 2][0])
                + " "
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
            )

    return res


def Mitigators(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["JJ"]
            and tagged[i][2] in ["ADJ"]
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() in ["pretty", "fairly", "rather", "quite"]
        ):
            res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))

    return res


def MitigatorsWithComparatives(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["JJR"]:
            if i - 1 >= 0 and str(tagged[i - 1][0]).lower() in ["rather", "slightly"]:
                res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))

            if (
                i - 2 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit", "little"]
                and str(tagged[i - 2][0]).lower() in ["a"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                )

            if (
                i - 3 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit"]
                and str(tagged[i - 2][0]).lower() in ["a"]
                and str(tagged[i - 3][0]).lower() in ["just"]
            ):
                res.append(
                    str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                )

            if (
                i - 3 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit"]
                and str(tagged[i - 2][0]).lower() in ["little"]
                and str(tagged[i - 3][0]).lower() in ["a"]
            ):
                res.append(
                    str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                )

            if (
                i - 4 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit"]
                and str(tagged[i - 2][0]).lower() in ["little"]
                and str(tagged[i - 3][0]).lower() in ["a"]
                and str(tagged[i - 4][0]).lower() in ["just"]
            ):
                res.append(
                    str(tagged[i - 4][0])
                    + " "
                    + str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                )

        if (
            i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in ["more"]
            and tagged[i + 1][1] in ["JJ"]
        ):
            if i - 1 >= 0 and str(tagged[i - 1][0]).lower() in ["rather", "slightly"]:
                res.append(
                    str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )

            if (
                i - 2 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit", "little"]
                and str(tagged[i - 2][0]).lower() in ["a"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )

            if (
                i - 3 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit"]
                and str(tagged[i - 2][0]).lower() in ["a"]
                and str(tagged[i - 3][0]).lower() in ["just"]
            ):
                res.append(
                    str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )

            if (
                i - 3 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit"]
                and str(tagged[i - 2][0]).lower() in ["little"]
                and str(tagged[i - 3][0]).lower() in ["a"]
            ):
                res.append(
                    str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )

            if (
                i - 4 >= 0
                and str(tagged[i - 1][0]).lower() in ["bit"]
                and str(tagged[i - 2][0]).lower() in ["little"]
                and str(tagged[i - 3][0]).lower() in ["a"]
                and str(tagged[i - 4][0]).lower() in ["just"]
            ):
                res.append(
                    str(tagged[i - 4][0])
                    + " "
                    + str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )

    return res


def determiners_Adjectives(sentence):
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
    adjectives = {}

    adjectives["Adjectives"] = Adjectives(tagged)
    adjectives["Adjectives end with -ed or -ing"] = AdjectivesendwithEDandING(tagged)
    adjectives["Comparative Adjectives"] = ComparativeAdjectives(tagged)
    adjectives["Superlative Adjectives"] = SuperlativeAdjectives(tagged)
    adjectives["Intensifiers with Adjectives"] = IntensifiersWithAdjectives(tagged)
    adjectives[
        "Intensifiers With Comparative Adjectives"
    ] = IntensifiersWithComparativeAdjectives(tagged)
    adjectives[
        "Intensifiers With Superlative Adjectives"
    ] = IntensifiersWithSuperlativeAdjectives(tagged)
    adjectives["Mitigators Adjectives"] = Mitigators(tagged)
    adjectives["Mitigators With Comparatives Adjectives"] = MitigatorsWithComparatives(
        tagged
    )

    return adjectives


# sentence1 = "we were rather tired"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "we had a pretty good time at the party"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "she's a bit younger than i am"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "it is a little bit longer by road"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "this is a slightly more expensive model than that"
# res1 = determiners_Adjectives(sentence1)
# print(res1)

###########
# sentence1 = "the blue whale is easily the biggest animal"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "this car was by far the most expensive"
# res1 = determiners_Adjectives(sentence1)
# print(res1)


################
# sentence1 = "he is much older than me"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "he is a far better player than me"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "new york is a lot bigger than boston"
# res1 = determiners_Adjectives(sentence1)
# print(res1)

###########3
# sentence1 = "it's a really interesting story"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "you are old enough"
# res1 = determiners_Adjectives(sentence1)
# print(res1)

#############
# sentence1 = "it was the happiest day"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "that's the best film i have seen this year"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "most careful"
# res1 = determiners_Adjectives(sentence1)
# print(res1)


###########
# sentence1 = "this car is certainly better , but it's much more expensive"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "i am feeling happier now"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "she is tow years older than me"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "the balloon got bigger and bigger "
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "the faster you drive , the more dangerous it is"
# res1 = determiners_Adjectives(sentence1)
# print(res1)

#################
# sentence1 = "i read a very interesting article"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "that dracula film was absolutely terrifying"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "we were really bored"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
#
# sentence1 = "Most of the time i was terrified"
# res1 = determiners_Adjectives(sentence1)
# print(res1)
