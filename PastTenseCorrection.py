import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown

word_list = brown.words()

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")
Pronouns = ["i", "you", "we", "they", "he", "she", "it"]


def PastSimple(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))

        if (
            (tagged[i][1] in ["NNS", "NN"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][5] in ["VERB"]
            and tagged[i][4] not in ["VBD"]
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]).lower(), "v")
            if lemma != "be":
                if "not" in mymap or "n't" in mymap:
                    res.append(str(tagged[i][0]) + " did not (didn’t) " + str(lemma))
                elif "not" not in mymap and "n't" not in mymap:
                    if (
                        getInflection(lemma, tag="VBD") != None
                        and str(getInflection(lemma, tag="VBD")[0]).lower()
                        != str(tagged[i][3]).lower()
                        and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(getInflection(lemma, tag="VBD")[0]).lower()
                        )

        elif (
            (tagged[i][1] in ["NNS", "NN"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] not in ["VBG", "VBN"]
            and i + 2 < len(tagged)
            and tagged[i + 2][1] not in ["VBG", "VBN"]
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")

            # verb -be with neg
            if lemma == "be" and ("not" in mymap or "n't" in mymap):
                if (
                    tagged[i][1] in ["NN"]
                    or str(tagged[i][0]).lower() in ["i", "he", "she", "it"]
                ) and "was" != str(tagged[i][3]).lower():
                    res.append(str(tagged[i][0]) + " was not (wasn't)")
                if (
                    tagged[i][1] in ["NNS"]
                    or str(tagged[i][0]).lower() in ["you", "we", "they"]
                ) and "were" != str(tagged[i][3]).lower():
                    res.append(str(tagged[i][0]) + " were not (weren't)")

            # verb -be without neg
            if lemma == "be" and "not" not in mymap and "n't" not in mymap:
                if (
                    tagged[i][1] in ["NN"]
                    or str(tagged[i][0]).lower() in ["i", "he", "she", "it"]
                ) and "was" != str(tagged[i][3]).lower():
                    res.append(str(tagged[i][0]) + " was")
                if (
                    tagged[i][1] in ["NNS"]
                    or str(tagged[i][0]).lower() in ["you", "we", "they"]
                ) and "were" != str(tagged[i][3]).lower():
                    res.append(str(tagged[i][0]) + " were")

            # verb nooot -be with neg
            if lemma != "be" and ("not" in mymap or "n't" in mymap):
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][0]) != "did"
                    or lemma != str(tagged[i][3]).lower()
                ):
                    res.append(str(tagged[i][0]) + " did not (didn’t) " + str(lemma))

            # verb nooot -be without neg
            if (
                lemma != "be"
                and "not" not in mymap
                and "n't" not in mymap
                and getInflection(lemma, tag="VBD") != None
                and str(getInflection(lemma, tag="VBD")[0]).lower()
                != str(tagged[i][3]).lower()
                and str(getInflection(lemma, tag="VBD")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(getInflection(lemma, tag="VBD")[0]).lower()
                )

    return res


def PastContinuous(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in ing
        if (
            (
                tagged[i][1] in ["NN"]
                or str(tagged[i][0]).lower() in ["i", "he", "she", "it"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "was"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 2][0]), "v")
            if (
                getInflection(lemma, tag="VBG") != None
                and str(getInflection(lemma, tag="VBG")[0]).lower()
                != str(tagged[i + 2][0]).lower()
                and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(getInflection(lemma, tag="VBG")[0]).lower()
                )

        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "were"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 2][0]), "v")
            if (
                getInflection(lemma, tag="VBG") != None
                and str(getInflection(lemma, tag="VBG")[0]).lower()
                != str(tagged[i + 2][0]).lower()
                and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(getInflection(lemma, tag="VBG")[0]).lower()
                )

        # error in (am is are)
        if (
            (
                tagged[i][1] in ["NN"]
                or str(tagged[i][0]).lower() in ["i", "he", "she", "it"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            # this if for negative
            if "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["was"]:
                    res.append(
                        str(tagged[i][0]) + " was not (wasn't) " + str(tagged[i][3])
                    )
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["was"]:
                res.append(str(tagged[i][0]) + " was " + str(tagged[i][3]))
        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            if "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["were"]:
                    res.append(
                        str(tagged[i][0]) + " were not (weren't) " + str(tagged[i][3])
                    )
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["were"]:
                res.append(str(tagged[i][0]) + " were " + str(tagged[i][3]))
    return res


def PastPerfect(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v2
        if (
            (tagged[i][1] in ["NN", "NNS"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "had"
            and str(tagged[i][4]) != "VBG"
        ):
            if "not" not in mymap and "n't" not in mymap:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 2][0]), "v")
                if (
                    getInflection(lemma, tag="VBN") != None
                    and str(getInflection(lemma, tag="VBN")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " "
                        + str(getInflection(lemma, tag="VBN")[0]).lower()
                    )
            if "not" in mymap or "n't" in mymap and i + 3 < len(tagged):
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 3][0]), "v")
                if (
                    getInflection(lemma, tag="VBN") != None
                    and str(getInflection(lemma, tag="VBN")[0]).lower()
                    != str(tagged[i][3]).lower()
                    and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " "
                        + str(tagged[i + 2][0])
                        + " "
                        + str(getInflection(lemma, tag="VBN")[0]).lower()
                    )

        # error in (had)
        if (
            (tagged[i][1] in ["NN", "NNS"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBN", "VBD"]
            and "will" not in mymap
            and "wo" not in mymap
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]) not in ["had"]
        ):
            # this if for negative
            if "not" in mymap or "n't" in mymap:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")
                if (
                    str(getInflection(lemma, tag="VBN")[0]).lower()
                    != str(tagged[i][3]).lower()
                    or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                    == str(getInflection(lemma, tag="VBN")[0]).lower()
                ) and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list:
                    if "been" not in mymap:
                        res.append(
                            str(tagged[i][0])
                            + " had not (hadn't) "
                            + str(getInflection(lemma, tag="VBN")[0])
                        )
            elif "not" not in mymap and "n't" not in mymap:
                if "been" not in mymap:
                    res.append(str(tagged[i][0]) + " had " + str(tagged[i][3]))
                elif i + 3 >= len(tagged):
                    res.append(str(tagged[i][0]) + " had " + str(tagged[i][3]))

    return res


def PastPerfectContinuous(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v-ing
        if (
            (tagged[i][1] in ["NN", "NNS"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 3 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "had"
        ):
            if "not" in mymap or "n't" in mymap:
                if str(tagged[i + 3][0]).lower() == "been":
                    lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 4][0]), "v")
                    if (
                        getInflection(lemma, tag="VBG") != None
                        and str(getInflection(lemma, tag="VBG")[0]).lower()
                        != str(tagged[i][3]).lower()
                        and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
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
                            + str(getInflection(lemma, tag="VBG")[0]).lower()
                        )
            if "not" not in mymap and "n't" not in mymap:
                if str(tagged[i + 2][0]).lower() == "been":
                    lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 3][0]), "v")
                    if (
                        getInflection(lemma, tag="VBG") != None
                        and str(getInflection(lemma, tag="VBG")[0]).lower()
                        != str(tagged[i][3]).lower()
                        and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                    ):
                        res.append(
                            str(tagged[i][0])
                            + " "
                            + str(tagged[i + 1][0])
                            + " "
                            + str(tagged[i + 2][0])
                            + " "
                            + str(getInflection(lemma, tag="VBG")[0]).lower()
                        )

        # error in (been)
        if (
            (tagged[i][1] in ["NN", "NNS"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            # this if for negative
            if i + 3 < len(tagged) and str(tagged[i + 1][0]).lower() == "had":
                if "not" in mymap or "n't" in mymap:
                    if str(tagged[i + 3][0]) not in ["been"]:
                        res.append(
                            str(tagged[i][0])
                            + " had not (hadn't) been "
                            + str(tagged[i][3])
                        )
                elif str(tagged[i + 2][0]) not in ["been"]:
                    res.append(str(tagged[i][0]) + " had been " + str(tagged[i][3]))

        # error in (have has)
        if (
            (tagged[i][1] in ["NN", "NNS"] or str(tagged[i][0]).lower() in Pronouns)
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            # this if for negative
            if "been" in mymap:
                if "not" in mymap or "n't" in mymap:
                    if str(tagged[i + 1][0]) not in ["had"]:
                        res.append(
                            str(tagged[i][0])
                            + " had not (hadn't) been "
                            + str(tagged[i][3])
                        )
                elif str(tagged[i + 1][0]) not in ["had"]:
                    res.append(str(tagged[i][0]) + " had been " + str(tagged[i][3]))

    return res


def PastTense_Checker(sentence):
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
    Past = {}

    Past["Past Simple"] = PastSimple(tagged)
    Past["Past Continuous"] = PastContinuous(tagged)
    Past["Past Perfect"] = PastPerfect(tagged)
    Past["Past Perfect Continuous"] = PastPerfectContinuous(tagged)

    return Past
