import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown

word_list = brown.words()

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")
Pronouns = ["i", "you", "we", "they", "he", "she", "it"]


def FutureSimple(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 1 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower() == "will"
                or str(tagged[i + 1][0]).lower() == "wo"
            )
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    lemma == "be"
                    and i + 5 < len(tagged)
                    and str(tagged[i + 5][2] == "VERB")
                ):
                    lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 5][0]), "v")
                if (
                    getInflection(lemma, tag="VB") != None
                    and str(getInflection(lemma, tag="VB")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and (
                        i + 5 >= len(tagged)
                        or (i + 5 < len(tagged) and tagged[i + 5][2] != "VERB")
                    )
                    and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) "
                        + str(getInflection(lemma, tag="VB")[0]).lower()
                    )
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    lemma == "be"
                    and i + 4 < len(tagged)
                    and str(tagged[i + 4][2] == "VERB")
                ):
                    lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 4][0]), "v")
                if (
                    getInflection(lemma, tag="VB") != None
                    and str(getInflection(lemma, tag="VB")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and (
                        i + 4 >= len(tagged)
                        or (i + 4 < len(tagged) and tagged[i + 4][2] != "VERB")
                    )
                    and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will "
                        + str(getInflection(lemma, tag="VB")[0]).lower()
                    )

        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBP", "VB"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() != "will"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    getInflection(lemma, tag="VB") != None
                    and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VB")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VB")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) "
                        + str(getInflection(lemma, tag="VB")[0]).lower()
                    )
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    getInflection(lemma, tag="VB") != None
                    and str(getInflection(lemma, tag="VB")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VB")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VB")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will "
                        + str(getInflection(lemma, tag="VB")[0]).lower()
                    )

    return res


def FutureContinuous(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v-ing
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 3 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower() == "will"
                or str(tagged[i + 1][0]).lower() == "wo"
            )
            and ("be" in mymap or str(tagged[i + 1][3]).lower() == "be")
        ):

            # with neg
            if "not" in mymap or "n't" in mymap and i + 4 < len(tagged):
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 4][0]), "v")
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower()
                    != str(tagged[i + 4][0]).lower()
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) be "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 3][0]), "v")
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower()
                    != str(tagged[i + 3][0]).lower()
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will be "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )

        # error in will
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() != "will"
            and "be" in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBG")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) be "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBG")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will be "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )

        # error in be
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "will"
            and "be" not in mymap
        ):
            # with neg
            if "not" in mymap or "n't" in mymap:
                res.append(
                    str(tagged[i][0]) + " will not (won't) be " + str(tagged[i][3])
                )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                res.append(str(tagged[i][0]) + " will be " + str(tagged[i][3]))
    return res


def FuturePerfect(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v-ing
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 1 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower() == "will"
                or str(tagged[i + 1][0]).lower() == "wo"
            )
            and "have" in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    lemma == "be"
                    and i + 5 < len(tagged)
                    and str(tagged[i + 5][2] == "VERB")
                ):
                    lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 5][0]), "v")
                if (
                    getInflection(lemma, tag="VBD") != None
                    and str(getInflection(lemma, tag="VBD")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) have "
                        + str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    lemma == "be"
                    and i + 4 < len(tagged)
                    and str(tagged[i + 4][2] == "VERB")
                ):
                    lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 4][0]), "v")
                if (
                    getInflection(lemma, tag="VBD") != None
                    and str(getInflection(lemma, tag="VBD")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will have "
                        + str(getInflection(lemma, tag="VBD")[0]).lower()
                    )

        # error in will
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBD", "VBN"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() != "will"
            and "have" in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    getInflection(lemma, tag="VBD") != None
                    and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBD")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) have "
                        + str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    getInflection(lemma, tag="VBD") != None
                    and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBD")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will have "
                        + str(getInflection(lemma, tag="VBD")[0]).lower()
                    )

        # error in have
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBD", "VBN"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "will"
            and "have" not in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    getInflection(lemma, tag="VBD") != None
                    and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBD")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) have "
                        + str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    getInflection(lemma, tag="VBD") != None
                    and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBD")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBD")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will have "
                        + str(getInflection(lemma, tag="VBD")[0]).lower()
                    )

    return res


def FuturePerfectContinuous(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v-ing
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 1 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower() == "will"
                or str(tagged[i + 1][0]).lower() == "wo"
            )
            and "been" in mymap
            and "have" in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) have been "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will have been "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )

        # error type 2 in v-ing
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 4 < len(tagged)
            and (
                str(tagged[i + 1][0]).lower() == "will"
                or str(tagged[i + 1][0]).lower() == "wo"
            )
        ):
            # neg
            if (
                i + 5 < len(tagged)
                and str(tagged[i + 2][6]) == "neg"
                and str(tagged[i + 3][0]).lower() == "have"
                and str(tagged[i + 4][0]).lower() == "been"
                and str(tagged[i + 5][1]) != "VBG"
            ):
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 5][0]), "v")
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) have been "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )

            # no neg
            elif (
                str(tagged[i + 2][0]).lower() == "have"
                and str(tagged[i + 3][0]).lower() == "been"
                and str(tagged[i + 4][1]) != "VBG"
            ):
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 4][0]), "v")
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will have been "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )

        # error in will
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() != "will"
            and "been" in mymap
            and "have" in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # with neg
            if "not" in mymap or "n't" in mymap:
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBG")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will not (won't) have been "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    and (
                        str(getInflection(lemma, tag="VBG")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
                ):
                    res.append(
                        str(tagged[i][0])
                        + " will have been "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )

        # error in be
        if (
            tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "will"
            and (
                ("been" not in mymap and "have" in mymap)
                or ("been" in mymap and "have" not in mymap)
            )
        ):
            # with neg
            if "not" in mymap or "n't" in mymap:
                res.append(
                    str(tagged[i][0])
                    + " will not (won't) have been "
                    + str(tagged[i][3])
                )
            # without neg
            elif "not" not in mymap and "n't" not in mymap:
                res.append(str(tagged[i][0]) + " will have been " + str(tagged[i][3]))

    return res


def FutureTense_Checker(sentence):
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
    Tenses = {}

    Tenses["Future Simple"] = FutureSimple(tagged)
    Tenses["Future Continuous"] = FutureContinuous(tagged)
    Tenses["Future Perfect"] = FuturePerfect(tagged)
    Tenses["Future Perfect Continuous"] = FuturePerfectContinuous(tagged)

    return Tenses
