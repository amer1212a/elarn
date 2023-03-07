import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown

word_list = brown.words()

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")

modalsverb = [
    "can",
    "could",
    "may",
    "might",
    "shall",
    "should",
    "will",
    "would",
    "must",
]


def Can_Might_Shall_Will_Would_Verb(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            (
                str(tagged[i][0]).lower() == "can"
                or str(tagged[i][0]).lower() == "ca"
                or str(tagged[i][0]).lower() == "might"
                or str(tagged[i][0]).lower() == "shall"
                or str(tagged[i][0]).lower() == "sha"
                or str(tagged[i][0]).lower() == "would"
                or str(tagged[i][0]).lower() == "will"
                or str(tagged[i][0]).lower() == "'ll"
            )
            and str(tagged[i][5])
            not in [
                "VERB",
                "ADJ",
            ]
            and (
                i + 1 >= len(tagged)
                or (i + 1 < len(tagged) and str(tagged[i + 1][2]) != "VERB")
            )
        ):
            res.append(
                "ERROR: You need to use a verb after modals verbs ("
                + str(tagged[i][0])
                + ")"
            )
        if (
            str(tagged[i][0]).lower() == "can"
            or str(tagged[i][0]).lower() == "ca"
            or str(tagged[i][0]).lower() == "might"
            or str(tagged[i][0]).lower() == "shall"
            or str(tagged[i][0]).lower() == "sha"
            or str(tagged[i][0]).lower() == "would"
            or str(tagged[i][0]).lower() == "will"
            or str(tagged[i][0]).lower() == "'ll"
        ):
            if "n't" not in mymap and "not" not in mymap:
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][2]) == "VERB"
                    and str(tagged[i + 1][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 1][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADV"
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " be " + str(tagged[i][3]))

            elif i + 1 < len(tagged) and str(tagged[i + 1][6]) == "neg":
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][2]) == "ADV"
                    and str(tagged[i + 3][2]) == "VERB"
                    and str(tagged[i + 3][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " not be " + str(tagged[i][3]))
    return res


def Could_May_Must_Verb(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            (
                str(tagged[i][0]).lower() == "could"
                or str(tagged[i][0]).lower() == "may"
                or str(tagged[i][0]).lower() == "must"
            )
            and str(tagged[i][5])
            not in [
                "VERB",
                "ADJ",
            ]
            and (
                i + 1 >= len(tagged)
                or (i + 1 < len(tagged) and str(tagged[i + 1][2]) != "VERB")
            )
        ):
            res.append(
                "ERROR: You need to use a verb after modals verbs ("
                + str(tagged[i][0])
                + ")"
            )
        if (
            str(tagged[i][0]).lower() == "could"
            or str(tagged[i][0]).lower() == "may"
            or str(tagged[i][0]).lower() == "must"
        ):
            if "n't" not in mymap and "not" not in mymap:
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][2]) == "VERB"
                    and str(tagged[i + 1][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 1][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADV"
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " be " + str(tagged[i][3]))
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][0]).lower() in ["have"]
                    and str(tagged[i + 1][2]) == "AUX"
                    and str(tagged[i + 2][1]) != "VBN"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBN") != None
                        and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][0]).lower() != "have"
                    and str(tagged[i][4]) == "VBN"
                ):
                    res.append(str(tagged[i][0]) + " have " + str(tagged[i][3]))

            elif i + 1 < len(tagged) and str(tagged[i + 1][6]) == "neg":
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][2]) == "ADV"
                    and str(tagged[i + 3][2]) == "VERB"
                    and str(tagged[i + 3][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " not be " + str(tagged[i][3]))
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][0]).lower() in ["have"]
                    and str(tagged[i + 2][2]) == "AUX"
                    and str(tagged[i + 3][1]) != "VBN"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBN") != None
                        and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][0]).lower() != "have"
                    and str(tagged[i][4]) == "VBN"
                ):
                    res.append(str(tagged[i][0]) + " not have " + str(tagged[i][3]))
    return res


def Should_Verb(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() == "should"
            and str(tagged[i][5])
            not in [
                "VERB",
                "ADJ",
            ]
            and (
                i + 1 >= len(tagged)
                or (i + 1 < len(tagged) and str(tagged[i + 1][2]) != "VERB")
            )
        ):
            res.append(
                "ERROR: You need to use a verb after modals verbs ("
                + str(tagged[i][0])
                + ")"
            )
        if str(tagged[i][0]).lower() == "should":
            if "n't" not in mymap and "not" not in mymap:
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][2]) == "VERB"
                    and str(tagged[i + 1][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 1][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][2]) == "ADV"
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " be " + str(tagged[i][3]))
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][0]).lower() in ["have"]
                    and str(tagged[i + 1][2]) == "AUX"
                    and str(tagged[i + 2][1]) != "VBN"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBN") != None
                        and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][0]).lower() != "have"
                    and str(tagged[i][4]) == "VBN"
                ):
                    res.append(str(tagged[i][0]) + " have " + str(tagged[i][3]))
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 1][0]).lower() == "be"
                    and str(tagged[i + 2][1]) != "VBG"
                    and str(tagged[i + 2][2]) == "VERB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBG") != None
                        and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VBG")[0])
                        )
                if str(tagged[i][4]) == "VBG" and (
                    (i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() != "be")
                    or i + 1 >= len(tagged)
                ):
                    res.append(str(tagged[i][0]) + " be " + str(tagged[i][3]))
                elif i + 1 < len(tagged) and str(tagged[i + 1][1]) == "VBG":
                    res.append(str(tagged[i][0]) + " be " + str(tagged[i + 1][0]))

            elif i + 1 < len(tagged) and str(tagged[i + 1][6]) == "neg":
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][2]) == "ADV"
                    and str(tagged[i + 3][2]) == "VERB"
                    and str(tagged[i + 3][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " not be " + str(tagged[i][3]))
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][0]).lower() in ["have"]
                    and str(tagged[i + 2][2]) == "AUX"
                    and str(tagged[i + 3][1]) != "VBN"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBN") != None
                        and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][0]).lower() != "have"
                    and str(tagged[i][4]) == "VBN"
                ):
                    res.append(str(tagged[i][0]) + " not have " + str(tagged[i][3]))
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][0]).lower() == "be"
                    and str(tagged[i + 3][1]) != "VBG"
                    and str(tagged[i + 3][2]) == "VERB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBG") != None
                        and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VBG")[0])
                        )
                if str(tagged[i][4]) == "VBG" and (
                    (i + 2 < len(tagged) and str(tagged[i + 2][0]).lower() != "be")
                    or i + 2 >= len(tagged)
                ):
                    res.append(str(tagged[i][0]) + " not be " + str(tagged[i][3]))
                elif i + 1 < len(tagged) and str(tagged[i + 1][1]) == "VBG":
                    res.append(str(tagged[i][0]) + " not be " + str(tagged[i + 1][0]))
    return res


def OughtTo_Verb(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() == "ought"
            and "to" in mymap
            and str(tagged[i][5])
            not in [
                "VERB",
                "ADJ",
            ]
            and (
                i + 2 >= len(tagged)
                or (i + 2 < len(tagged) and str(tagged[i + 2][2]) != "VERB")
            )
            and (
                i + 3 >= len(tagged)
                or (i + 3 < len(tagged) and str(tagged[i + 3][2]) != "VERB")
            )
        ):
            res.append(
                "ERROR: You need to use a verb after semi-modals verbs ("
                + str(tagged[i][0] + " to")
                + ")"
            )
        if str(tagged[i][0]).lower() == "ought":
            if "n't" not in mymap and "not" not in mymap:
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][2]) == "VERB"
                    and str(tagged[i + 2][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 2][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str("ought to " + str(getInflection(lemma, tag="VB")[0]))
                        )
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][2]) == "ADV"
                    and str(tagged[i + 3][2]) == "VERB"
                    and str(tagged[i + 3][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " to be " + str(tagged[i][3]))
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 2][0]).lower() in ["have"]
                    and str(tagged[i + 2][2]) == "AUX"
                    and str(tagged[i + 3][1]) != "VBN"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBN") != None
                        and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
                if (
                    i + 2 < len(tagged)
                    and str(tagged[i + 2][0]).lower() != "have"
                    and str(tagged[i][4]) == "VBN"
                ):
                    res.append(str(tagged[i][0]) + " to have " + str(tagged[i][3]))

            elif i + 1 < len(tagged) and str(tagged[i + 1][6]) == "neg":
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 3][2]) == "VERB"
                    and str(tagged[i + 3][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not to "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if (
                    i + 4 < len(tagged)
                    and str(tagged[i + 3][2]) == "ADV"
                    and str(tagged[i + 4][2]) == "VERB"
                    and str(tagged[i + 4][1]) != "VB"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VB") != None
                        and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not to "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(getInflection(lemma, tag="VB")[0])
                        )
                if str(tagged[i][5]) == "ADJ":
                    res.append(str(tagged[i][0]) + " not to be " + str(tagged[i][3]))
                if (
                    i + 4 < len(tagged)
                    and str(tagged[i + 3][0]).lower() in ["have"]
                    and str(tagged[i + 3][2]) == "AUX"
                    and str(tagged[i + 4][1]) != "VBN"
                ):
                    lemma = wordnet_lemmatizer.lemmatize(
                        str(tagged[i + 3][0]).lower(), "v"
                    )
                    if (
                        getInflection(lemma, tag="VBN") != None
                        and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " not to "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
                if (
                    i + 3 < len(tagged)
                    and str(tagged[i + 3][0]).lower() != "have"
                    and str(tagged[i][4]) == "VBN"
                ):
                    res.append(str(tagged[i][0]) + " not to have " + str(tagged[i][3]))
    return res


def ModalsVerb_Checker(sentence):
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
    modalsverb = {}

    # modalsverb["Modals Verb"] = ModalsVerb(tagged)
    modalsverb["Modals Verb"] = (
        Can_Might_Shall_Will_Would_Verb(tagged)
        + Could_May_Must_Verb(tagged)
        + Should_Verb(tagged)
        + OughtTo_Verb(tagged)
    )

    return modalsverb


# # She must have been at home
# sentence3 = "She must have be at home"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # I would get up before everyone
# #I would spend hours
# sentence3 = "I would spent hours"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # My son wouldn't eat his food.
# sentence3 = "My son wouldn't eating his food."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # We ought to have locked the gate.
# sentence3 = "We ought to have lock the gate."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)


# # It can be very cold here.
# sentence3 = "It can very cold here."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# You can easily get lost in this town.
# sentence3 = "You can easily lost in this town."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # We cannot park the car next to this
# sentence3 = "We cannot the car next to this"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # I can speak two languages.
# sentence3 = "I can speaking two languages."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # They can't have landed on the moon,
# sentence3 = "They can't have land on the moon,"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# error
# # It can get cold there at night
# sentence3 = "It can get cold there at night"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # They could have got lost.
# sentence3 = "They could have get lost."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # I could ride a horse
# sentence3 = "I could a horse."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # we couldn't leave the classroom
# sentence3 = "we couldn't have leave the classroom."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # He couldn't have painted that.
# sentence3 = "He couldn't painted that."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # It may have already been broken before you bought it.
# sentence3 = "It may have be broken before you bought it."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# # He should have the letter by now.
# sentence3 = "He should had the letter by now."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)


# # You should never lie to your doctor.
# sentence3 = "You should never lieing to your doctor."
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)


# # You should be wearing your seatbelt.
# sentence3 = "You should wearing your seatbelt"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)

# sentence3 = "You should be weared your seatbelt"
# res3 = ModalsVerb_Checker(sentence3)
# print(res3)