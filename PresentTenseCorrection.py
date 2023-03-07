import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown
word_list = brown.words()

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")



def PresentSimple(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] not in ["VBG", "VBN", "VBD", "VB"]
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")
            # if verb -be
            if lemma == "be":
                # if verb -be with neg
                if "not" in mymap or "n't" in mymap:
                    if i + 2 < len(tagged) and (
                        str(tagged[i + 1][0]).lower() != "is"
                        or str(tagged[i + 2][6]) == "neg"
                    ):
                        res.append(str(tagged[i][0]) + " is not (isn't) ")
                # if verb -be without neg
                else:
                    if i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() != "is":
                        res.append(str(tagged[i][0]) + " is")

            # if verb not -be with neg
            elif "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) != "does":
                    res.append(str(tagged[i][0]) + " does not (doesn’t) " + str(lemma))

            # if verb not -be and no neg
            elif (
                getInflection(lemma, tag="VBZ") != None
                and str(getInflection(lemma, tag="VBZ")[0]).lower()
                != str(tagged[i][3]).lower()
                and str(getInflection(lemma, tag="VBZ")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(getInflection(lemma, tag="VBZ")[0]).lower()
                )

        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] not in ["VBG", "VBN", "VBD"]
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")
            # if verb -be with (I)
            if lemma == "be" and str(tagged[i][0]).lower() == "i":
                # if verb -be with neg
                if "not" in mymap or "n't" in mymap:
                    if "am" != str(tagged[i][3]).lower():
                        res.append(str(tagged[i][0]) + " am not")
                # if verb -be without neg
                else:
                    if "am" != str(tagged[i][3]).lower():
                        res.append(str(tagged[i][0]) + " am")
            # if verb -be nooooooot (I)
            if lemma == "be" and str(tagged[i][0]).lower() != "i":
                # if verb -be with neg
                if "not" in mymap or "n't" in mymap:
                    if "are" != str(tagged[i][3]).lower():
                        res.append(str(tagged[i][0]) + " are not (aren't)")
                # if verb -be without neg
                else:
                    if "are" != str(tagged[i][3]).lower():
                        res.append(str(tagged[i][0]) + " are")

            # if verb not -be with neg
            if lemma != "be" and ("not" in mymap or "n't" in mymap):
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][0]) != "do"
                    or lemma != str(tagged[i][3]).lower()
                ):
                    res.append(str(tagged[i][0]) + " do not (don’t) " + str(lemma))

            # if verb not -be and no neg
            if (
                lemma != "be"
                and "not" not in mymap
                and "n't" not in mymap
                and getInflection(lemma, tag="VBP") != None
                and str(getInflection(lemma, tag="VBP")[0]).lower()
                != str(tagged[i][3]).lower()
                and str(getInflection(lemma, tag="VBP")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(getInflection(lemma, tag="VBP")[0]).lower()
                )

    return res


def PresentContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in ing
        if (
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "is"
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
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 2][2]) != "NOUN"
            and str(tagged[i + 1][0]).lower() in ["am", "are"]
        ):
            if "not" in mymap or "n't" in mymap:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 3][0]), "v")
                if (
                    getInflection(lemma, tag="VBG") != None
                    and str(getInflection(lemma, tag="VBG")[0]).lower()
                    != str(tagged[i + 3][0]).lower()
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " not "
                        + str(getInflection(lemma, tag="VBG")[0]).lower()
                    )
            elif "not" not in mymap and "n't" not in mymap:
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
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            # this if for negative
            if "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["is"]:
                    res.append(
                        str(tagged[i][0]) + " is not (isn't) " + str(tagged[i][3])
                    )
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["is"]:
                res.append(str(tagged[i][0]) + " is " + str(tagged[i][3]))
        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            if "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["are"]:
                    res.append(
                        str(tagged[i][0]) + " are not (aren't) " + str(tagged[i][3])
                    )
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["are"]:
                res.append(str(tagged[i][0]) + " are " + str(tagged[i][3]))
        if (
            str(tagged[i][0]).lower() in ["i"]
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
            and "been" not in mymap
        ):
            if "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["am"]:
                    res.append(str(tagged[i][0]) + " am not " + str(tagged[i][3]))
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["am"]:
                res.append(str(tagged[i][0]) + " am " + str(tagged[i][3]))
    return res


def PresentPerfect(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v3
        if (
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "has"
            and "been" not in mymap
        ):
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

        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 2 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "have"
            and "been" not in mymap
        ):
            # without neg
            if "not" not in mymap and "n't" not in mymap:
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 2][0]), "v")
                if (
                    getInflection(lemma, tag="VBN") != None
                    and str(getInflection(lemma, tag="VBN")[0]).lower()
                    != str(tagged[i + 2][0]).lower()
                    and str(getInflection(lemma, tag="VBN")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " "
                        + str(getInflection(lemma, tag="VBN")[0]).lower()
                    )
            # with neg
            if i + 3 < len(tagged) and ("not" in mymap or "n't" in mymap):
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i + 3][0]), "v")
                if (
                    getInflection(lemma, tag="VBN") != None
                    and str(getInflection(lemma, tag="VBN")[0]).lower()
                    != str(tagged[i + 3][0]).lower()
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

        # error in (has have)
        if (
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBN", "VBD"]
            and "will" not in mymap
            and "wo" not in mymap
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][3]), "v")
            # this if for negative
            if "not" in mymap or "n't" in mymap:
                if (
                    i + 1 < len(tagged)
                    and str(tagged[i + 1][0]) not in ["has"]
                    and (
                        str(getInflection(lemma, tag="VBN")[0]).lower()
                        != str(tagged[i][3]).lower()
                        or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                        == str(getInflection(lemma, tag="VBN")[0]).lower()
                    )
                    and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
                ):
                    res.append(
                        str(tagged[i][0])
                        + " has not (hasn't) "
                        + str(getInflection(lemma, tag="VBN")[0])
                    )
            elif (
                i + 1 < len(tagged)
                and str(tagged[i + 1][0]) not in ["has"]
                and (
                    str(getInflection(lemma, tag="VBN")[0]).lower()
                    != str(tagged[i][3]).lower()
                    or str(getInflection(lemma, tag=str(tagged[i][4]))[0]).lower()
                    == str(getInflection(lemma, tag="VBN")[0]).lower()
                )
                and str(getInflection(lemma, tag="VBG")[0]).lower() in word_list
            ):
                res.append(
                    str(tagged[i][0])
                    + " has "
                    + str(getInflection(lemma, tag="VBN")[0])
                )

        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBN", "VBD"]
            and tagged[i][5] != "AUX"
            and (
                i + 3 >= len(tagged)
                or (i + 3 < len(tagged) and tagged[i + 3][2] not in ["VERB"])
            )
            and "will" not in mymap
            and "wo" not in mymap
        ):
            if "not" in mymap or "n't" in mymap:
                if i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["have"]:
                    res.append(
                        str(tagged[i][0]) + " have not (haven't) " + str(tagged[i][3])
                    )
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]) not in ["have"]:
                res.append(str(tagged[i][0]) + " have " + str(tagged[i][3]))
    return res


def PresentPerfectContinuous(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        # error in v-ing
        if (
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 3 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "has"
            and str(tagged[i + 2][0]).lower() == "been"
        ):
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

        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and i + 3 < len(tagged)
            and str(tagged[i + 1][0]).lower() == "have"
            and str(tagged[i + 2][0]).lower() == "been"
        ):
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
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            # this if for negative
            if i + 3 < len(tagged) and str(tagged[i + 1][0]).lower() == "has":
                if "not" in mymap or "n't" in mymap:
                    if str(tagged[i + 3][0]) not in ["been"]:
                        res.append(
                            str(tagged[i][0])
                            + " has not (hasn't) been "
                            + str(tagged[i][3])
                        )
                elif str(tagged[i + 2][0]) not in ["been"]:
                    res.append(str(tagged[i][0]) + " has been " + str(tagged[i][3]))
        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            if i + 3 < len(tagged) and str(tagged[i + 1][0]).lower() == "have":
                if "not" in mymap or "n't" in mymap:
                    if str(tagged[i + 3][0]) not in ["been"]:
                        res.append(
                            str(tagged[i][0])
                            + " have not (haven't) been "
                            + str(tagged[i][3])
                        )
                elif str(tagged[i + 2][0]) not in ["been"]:
                    res.append(str(tagged[i][0]) + " have been " + str(tagged[i][3]))

        # error in (have has)
        if (
            (tagged[i][1] in ["NN"] or str(tagged[i][0]).lower() in ["he", "she", "it"])
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            # this if for negative
            if "been" in mymap:
                if "not" in mymap or "n't" in mymap:
                    if str(tagged[i + 1][0]) not in ["has"]:
                        res.append(
                            "ERROR: "
                            + str(tagged[i][0])
                            + " has not (hasn't) been "
                            + str(tagged[i][3])
                        )
                elif str(tagged[i + 1][0]) not in ["has"]:
                    res.append(
                        "ERROR: " + str(tagged[i][0]) + " has been " + str(tagged[i][3])
                    )
        if (
            (
                tagged[i][1] in ["NNS"]
                or str(tagged[i][0]).lower() in ["i", "you", "we", "they"]
            )
            and tagged[i][6] in ["nsubj", "nsubjpass"]
            and tagged[i][4] in ["VBG"]
        ):
            if "been" in mymap:
                if "not" in mymap or "n't" in mymap:
                    if str(tagged[i + 1][0]) not in ["have"]:
                        res.append(
                            "ERROR: "
                            + str(tagged[i][0])
                            + " have not (haven't) been "
                            + str(tagged[i][3])
                        )
                elif str(tagged[i + 1][0]) not in ["have"]:
                    res.append(
                        "ERROR: "
                        + str(tagged[i][0])
                        + " have been "
                        + str(tagged[i][3])
                    )

    return res


def PresentTense_Checker(sentence):
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
    Present = {}

    Present["Present Simple"] = PresentSimple(tagged)
    Present["Present Continuous"] = PresentContinuous(tagged)
    Present["Present Perfect"] = PresentPerfect(tagged)
    Present["Present Perfect Continuous"] = PresentPerfectContinuous(tagged)

    return Present

# lemma = wordnet_lemmatizer.lemmatize('new', "v")
# dd = str(getInflection(lemma, tag="VBG")[0]).lower()
# print(dd in word_list)





# sentence3 = "I have been walk."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "I have walking."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "he has not walking."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "I have not walking."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "I has not been walking."
# res3 = Present_Checker(sentence3)
# print(res3)


# sentence3 = "I has not eaten breakfast today."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "i written."
# res3 = PresentTense_Checker(sentence3)
# print(res3)

# sentence3 = "i have writing."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "he written."
# res3 = Present_Checker(sentence3)
# print(res3)


# sentence3 = "he has writing."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "we not cooking."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "He sleeping."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "I sleeping."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "We sleeping."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "he is play."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "he is teacher."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "he is angry."
# res3 = Present_Checker(sentence3)
# print(res3)


# sentence3 = "I am sleep."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "he is sleep."
# res3 = Present_Checker(sentence3)
# print(res3)


# present simple
# sentence3 = "Good haelth depend on having a good diet."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "Good haelth depends on having a good diet."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "The building have three rooms."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "The students have three rooms."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "He live in India."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "I lives in India."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "He often go to bed late."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "i don't live in London."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "i not live in London."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "We is always on time."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "We are always on time."
# res3 = Present_Checker(sentence3)
# print(res3)

# sentence3 = "I usually plays football with my friends."
# res3 = Present_Checker(sentence3)
# print(res3)


# sentence4 = "I fell graet!"
# res4 = Present_Checker(sentence4)
# print(res4)

# sentence2 = "she gos to schol"
# res1 = Present_Checker(sentence2)
# print(res1)