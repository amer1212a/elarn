import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown


word_list = brown.words()

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")
determiners = [
    "my",
    "your",
    "his",
    "her",
    "its",
    "our",
    "their",
    "whose",
    "the",
    "this",
    "that",
    "these",
    "those",
    "a",
    "an",
    "any",
    "another",
    "other",
    "which",
    "what",
]


def Determiners(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in determiners
            and str(tagged[i][5]) not in ["NOUN","VERB"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][2]) != "NOUN"
        ):
            res.append(
                "ERROR: You need to use a noun after determiners ("
                + str(tagged[i][0])
                + ")"
            )
            # a-e-i-o-u
        if (
            str(tagged[i][0]).lower() == "a"
            and (
                str(tagged[i][5]) in ["NOUN"]
                or (i + 1 < len(tagged) and str(tagged[i + 1][2]) == "NOUN")
            )
            and i + 1 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower().startswith("a")
                or str(tagged[i + 1][0]).lower().startswith("e")
                or str(tagged[i + 1][0]).lower().startswith("i")
                or str(tagged[i + 1][0]).lower().startswith("o")
                or str(tagged[i + 1][0]).lower().startswith("u")
            )
        ):
            if str(tagged[i][5]) in ["NOUN"]:
                res.append("an " + str(tagged[i][3]))
            else:
                res.append("an " + str(tagged[i + 1][0]))

        if (
            str(tagged[i][0]).lower() == "an"
            and (
                str(tagged[i][5]) in ["NOUN"]
                or (i + 1 < len(tagged) and str(tagged[i + 1][2]) == "NOUN")
            )
            and i + 1 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower().startswith("a")
                and not str(tagged[i + 1][0]).lower().startswith("e")
                and not str(tagged[i + 1][0]).lower().startswith("i")
                and not str(tagged[i + 1][0]).lower().startswith("o")
                and not str(tagged[i + 1][0]).lower().startswith("u")
            )
        ):
            if str(tagged[i][5]) in ["NOUN"]:
                res.append("a " + str(tagged[i][3]))
            else:
                res.append("a " + str(tagged[i + 1][0]))

    return res


def Quantifiers(tagged):
    # print(tagged)
    quantifiers = [
        "all",
        "some",
        "more",
        "enough",
        "no",
        "any",
        "most",
        "less",
    ]
    quantifiers_of = [
        "lots",
        "plenty",
        "heaps",
        "loads",
        "tons",
    ]
    quantifiers_a_of = ["lot", "load", "bit"]
    quantifiers_count = [
        "many",
        "each",
        "either",
        "few",
        "several",
        "both",
        "neither",
        "fewer",
    ]
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # no noun with quantifiers don't use (of)
        if str(tagged[i][0]).lower() in quantifiers + quantifiers_count and tagged[i][
            5
        ] not in ["NOUN"]:
            res.append(
                "ERROR: You need to use a noun after quantifiers ("
                + str(tagged[i][0])
                + ")"
            )
        if (
            (
                str(tagged[i][0]).lower() in quantifiers_count
                or (
                    str(tagged[i][0]).lower() in ["hundreds", "couple", "thousands"]
                    and i + 1 < len(tagged)
                    and str(tagged[i + 1][0]).lower() == "of"
                )
            )
            and str(tagged[i][5]) not in ["NOUN"]
            and str(tagged[i][4]) not in ["NNS"]
            and str(tagged[i][0]) == str(tagged[i][3])
        ):
            if i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() == "of":
                res.append(
                    "ERROR: You need to use a noun after quantifiers ("
                    + str(tagged[i][0])
                    + "of)"
                )
            else:
                res.append(
                    "ERROR: You need to use a noun after quantifiers ("
                    + str(tagged[i][0])
                    + ")"
                )
        if (
            (
                str(tagged[i][0]).lower() in quantifiers_count
                or (
                    str(tagged[i][0]).lower() in ["hundreds", "couple", "thousands"]
                    and i + 1 < len(tagged)
                    and str(tagged[i + 1][0]).lower() == "of"
                )
            )
            and str(tagged[i][5]) in ["NOUN"]
            and (
                str(tagged[i][4]) not in ["NNS"]
                or str(tagged[i][0]) == str(tagged[i][3])
            )
        ):
            if str(tagged[i][0]) == str(tagged[i][3]):
                if str(tagged[i + 1][0]).lower() == "of":
                    if str(tagged[i + 2][2]) == "ADJ":
                        lemma = wordnet_lemmatizer.lemmatize(
                            str(tagged[i + 2][3]).lower(), "n"
                        )
                    else:
                        lemma = wordnet_lemmatizer.lemmatize(
                            str(tagged[i + 2][0]).lower(), "n"
                        )
                    if (
                        str(tagged[i][0]).lower() in ["couple"]
                        and str(getInflection(lemma, tag="NNS")[0]).lower() in word_list
                    ):
                        res.append(
                            "a "
                            + str(tagged[i][0])
                            + " of "
                            + str(getInflection(lemma, tag="NNS")[0])
                        )
                    elif str(getInflection(lemma, tag="NNS")[0]).lower() in word_list:
                        res.append(
                            str(tagged[i][0])
                            + " of "
                            + str(getInflection(lemma, tag="NNS")[0])
                        )
                else:
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 1][0]).lower(), "n"
                    )
                    if str(getInflection(lemma, tag="NNS")[0]).lower() in word_list:
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(getInflection(lemma, tag="NNS")[0])
                        )
            else:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]).lower(), "n")
                if str(getInflection(lemma, tag="NNS")[0]).lower() in word_list:
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(getInflection(lemma, tag="NNS")[0])
                    )
        # no (of) with quantifiers use (of)
        if (
            str(tagged[i][0]).lower() in quantifiers_of
            and tagged[i][5] in ["NOUN"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() != "of"
        ):
            res.append(str(tagged[i][0]) + " of " + str(tagged[i + 1][0]))

        # no noun with quantifiers use (of)
        if (
            str(tagged[i][0]).lower() in quantifiers_of
            and tagged[i][5] not in ["NOUN"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "of"
        ):
            res.append(
                "ERROR: You need to use a noun after quantifiers ("
                + str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + ")"
            )

        # no (a) with quantifiers_a_of
        if (
            str(tagged[i][0]).lower() in quantifiers_a_of
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "of"
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() != "a"
        ):
            res.append("a " + str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

        # no (of) with quantifiers_a_of
        if (
            str(tagged[i][0]).lower() in quantifiers_a_of
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() != "of"
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() == "a"
        ):
            res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]) + " of")

        # no noun with quantifiers_a_of
        if (
            str(tagged[i][0]).lower() in quantifiers_a_of
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "of"
            and i - 1 >= 0
            and str(tagged[i - 1][0]).lower() == "a"
            and str(tagged[i + 2][2]) != "NOUN"
            and str(tagged[i + 2][5]) != "NOUN"
        ):
            res.append(
                "ERROR: You need to use a noun after quantifiers ("
                + str(tagged[i - 1][0])
                + " "
                + str(tagged[i][0])
                + " of)"
            )

    return res


def Determiners_Checker(sentence):
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
    Determiner = {}

    Determiner["Determiners"] = Determiners(tagged)
    Determiner["Quantifiers"] = Quantifiers(tagged)

    return Determiner


# sentence3 = "I have a bit butter."
# res3 = Determiners_Checker(sentence3)
# print(res3)

# sentence3 = "thousands of young man at the university."
# res3 = Determiners_Checker(sentence3)
# print(res3)

# sentence3 = "a university is big"
# res3 = Determiners_Checker(sentence3)
# print(res3)

# sentence3 = "the train leaves in a few minute."
# res3 = Determiners_Checker(sentence3)
# print(res3)

# sentence3 = "I've got lots money."
# res3 = Determiners_Checker(sentence3)
# print(res3)

# sentence3 = "I've got a lot of sweet."
# res3 = Determiners_Checker(sentence3)
# print(res3)

# sentence3 = "Thank you very much for your great."
# res3 = Determiners_Checker(sentence3)
# print(res3)
