import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown

word_list = brown.words()


wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")

intensifiers = ["very", "really", "extremely"]
mitigators = ["fairly", "rather", "quite", "pretty"]
mitigatorswithcomparative = ["slightly", "little", "bit"]


def AdjectiveOrder(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][2]) == "ADJ"
            and str(tagged[i][1]) not in ["JJR", "JJS"]
            and (
                i - 1 <= 0
                or (
                    i - 1 > 0
                    and str(tagged[i - 1][0]).lower()
                    not in intensifiers + mitigators + mitigatorswithcomparative
                )
            )
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")
            if i - 1 >= 0 and str(tagged[i - 1][2]) == "NOUN":
                if (
                    i + 4 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADJ"
                    and str(tagged[i + 2][2]) == "ADJ"
                    and str(tagged[i + 3][2]) == "ADJ"
                    and str(tagged[i + 4][2]) == "ADJ"
                    and (
                        (
                            i + 5 < len(tagged)
                            and str(tagged[i + 5][2]) not in ["ADJ", "NOUN"]
                        )
                        or i + 5 >= len(tagged)
                    )
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
                        + str(tagged[i + 4][0])
                        + " "
                        + str(tagged[i - 1][0])
                    )
                elif (
                    i + 3 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADJ"
                    and str(tagged[i + 2][2]) == "ADJ"
                    and str(tagged[i + 3][2]) == "ADJ"
                    and (
                        (
                            i + 4 < len(tagged)
                            and str(tagged[i + 4][2]) not in ["ADJ", "NOUN"]
                        )
                        or i + 4 >= len(tagged)
                    )
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
                        + str(tagged[i - 1][0])
                    )
                elif (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADJ"
                    and str(tagged[i + 2][2]) == "ADJ"
                    and (
                        (
                            i + 3 < len(tagged)
                            and str(tagged[i + 3][2]) not in ["ADJ", "NOUN"]
                        )
                        or i + 3 >= len(tagged)
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " "
                        + str(tagged[i + 2][0])
                        + " "
                        + str(tagged[i - 1][0])
                    )
                elif (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADJ"
                    and (
                        (
                            i + 2 < len(tagged)
                            and str(tagged[i + 2][2]) not in ["ADJ", "NOUN"]
                        )
                        or i + 2 >= len(tagged)
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " "
                        + str(tagged[i - 1][0])
                    )
                elif (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][2])
                    not in [
                        "ADJ",
                        "NOUN",
                    ]
                ) or i + 1 >= len(tagged):
                    res.append(str(tagged[i][0]) + " " + str(tagged[i - 1][0]))

            elif (
                str(tagged[i][5]) != "NOUN"
                and lemma != "be"
                and (
                    str(tagged[i - 1][2]) != "ADJ"
                    or (i + 1 < len(tagged) and str(tagged[i + 1][2]) != "ADJ")
                )
            ):
                res.append(
                    "ERROR: You need to use a noun after adjective ("
                    + str(tagged[i][0])
                    + ")"
                )
    return res


def SuperlativeAdjectives(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if str(tagged[i][1]) == "JJS":
            if i - 1 < 0 or (i - 1 >= 0 and str(tagged[i - 1][0]).lower() != "the"):
                res.append("the " + str(tagged[i][0]))

        if (
            str(tagged[i][2]) == "ADJ"
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() == "the"
            and str(tagged[i][5]) != "NOUN"
            and str(tagged[i][1]) != "JJS"
            and (
                i + 1 >= len(tagged)
                or (
                    i + 1 < len(tagged) and str(tagged[i + 1][2]) not in ["ADJ", "NOUN"]
                )
            )
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][0]).lower(), "a")
            if (
                getInflection(lemma, tag="JJS") != None
                and str(getInflection(lemma, tag="JJS")[0]).lower() in word_list
            ):
                res.append("the " + str(getInflection(lemma, tag="JJS")[0]))

    return res


def Intensifiers(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if str(tagged[i][0]).lower() in intensifiers and (
            i + 1 >= len(tagged)
            or (i + 1 < len(tagged) and str(tagged[i + 1][2]) != "ADJ")
        ):
            res.append(
                "ERROR: You need to use an adjective after intensifiers ("
                + str(tagged[i][0])
                + ")"
            )
        if (
            str(tagged[i][0]).lower() in intensifiers
            and i + 1 < len(tagged)
            and str(tagged[i + 1][2]) == "ADJ"
            and str(tagged[i + 1][1]) != "JJ"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 1][0]), "a")
            if (
                getInflection(lemma, tag="JJ") != None
                and str(getInflection(lemma, tag="JJ")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0]) + " " + str(getInflection(lemma, tag="JJ")[0])
                )

    return res


def IntensifierswithSuperlative(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["easily", "far"]
            and i + 2 < len(tagged)
            and str(tagged[i + 2][1]) != "JJS"
            and (
                i + 3 >= len(tagged)
                or (i + 3 < len(tagged) and str(tagged[i + 3][2]) != "JJS")
            )
        ):
            if str(tagged[i][0]).lower() in ["far"]:
                if i - 1 >= 0 and str(tagged[i - 1][0]).lower() == "by":
                    res.append(
                        "ERROR: You need to use a superlative adjectives after intensifiers (by "
                        + str(tagged[i][0])
                        + ")"
                    )
            else:
                res.append(
                    "ERROR: You need to use a superlative adjectives after intensifiers ("
                    + str(tagged[i][0])
                    + ")"
                )

    return res


def IntensifierswithComparative(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["much", "far"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][1]) != "JJR"
            and str(tagged[i + 1][2]) == "ADJ"
        ):
            if (i - 1 >= 0 and str(tagged[i - 1][0]).lower() != "by") or i - 1 < 0:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 1][0]), "a")
                if (
                    getInflection(lemma, tag="JJR") != None
                    and str(getInflection(lemma, tag="JJR")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(getInflection(lemma, tag="JJR")[0])
                    )
                else:
                    res.append(
                        "ERROR: You need to use a comparative adjectives after intensifiers ("
                        + str(tagged[i][0])
                        + ")"
                    )

    return res


def Mitigators(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in mitigators
            and i + 1 < len(tagged)
            and str(tagged[i + 1][1]) != "JJ"
            and str(tagged[i + 1][2]) == "ADJ"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 1][0]), "a")
            if (
                getInflection(lemma, tag="JJ") != None
                and str(getInflection(lemma, tag="JJ")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0]) + " " + str(getInflection(lemma, tag="JJ")[0])
                )
            else:
                res.append(
                    "ERROR: You need to use an adjectives after mitigators ("
                    + str(tagged[i][0])
                    + ")"
                )
        # mitigators with comparative
        if (
            str(tagged[i][0]).lower() in mitigatorswithcomparative
            and i + 1 < len(tagged)
            and str(tagged[i + 1][1]) != "JJR"
            and str(tagged[i + 1][2]) == "ADJ"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 1][0]), "a")
            if (
                getInflection(lemma, tag="JJR") != None
                and str(getInflection(lemma, tag="JJR")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0]) + " " + str(getInflection(lemma, tag="JJR")[0])
                )
            else:
                res.append(
                    "ERROR: You need to use a comparative adjectives after mitigators ("
                    + str(tagged[i][0])
                    + ")"
                )

    return res


def Adjective_Checker(sentence):
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
    Adjective = {}

    Adjective["Adjective Order"] = AdjectiveOrder(tagged)
    Adjective["Superlative Adjectives"] = SuperlativeAdjectives(tagged)
    Adjective["Intensifiers"] = Intensifiers(tagged)
    Adjective["Intensifiers with Superlative Adjective"] = IntensifierswithSuperlative(
        tagged
    )
    Adjective["Intensifiers with Comparative Adjective"] = IntensifierswithComparative(
        tagged
    )
    Adjective["Mitigators"] = Mitigators(tagged)

    return Adjective


# sentence3 = "She's a bit young than I am."
# res3 = Adjective_Checker(sentence3)
# print(res3)

# sentence3 = "we were rather biggest."
# res3 = Adjective_Checker(sentence3)
# print(res3)

# sentence3 = "he is a far good player than Ronaldo."
# res3 = Adjective_Checker(sentence3)
# print(res3)

# sentence3 = "This car was by far the bigger."
# res3 = Adjective_Checker(sentence3)
# print(res3)

# sentence3 = "very youngest"
# res3 = Adjective_Checker(sentence3)
# print(res3)

# sentence3 = "Everyone was very youngest."
# res3 = Adjective_Checker(sentence3)
# print(res3)

# sentence3 = "Angela is the young."
# res3 = Adjective_Checker(sentence3)
# print(res3)


# sentence3 = "a man handsome young great."
# res3 = Adjective_Checker(sentence3)
# print(res3)