import spacy
from pyinflect import getInflection
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown

word_list = brown.words()

wordnet_lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")


def SingularNoun(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["is", "was"]
            and i - 1 >= 0
            and str(tagged[i - 1][2]) == "NOUN"
        ):
            if str(tagged[i - 1][1]) != "NN":
                lemma = wordnet_lemmatizer.lemmatize(str(tagged[i - 1][0]), "n")
                if (
                    getInflection(lemma, tag="NN") != None
                    and str(getInflection(lemma, tag="NN")[0]) != str(tagged[i - 1][0])
                    and str(getInflection(lemma, tag="NN")[0]).lower() in word_list
                ):
                    res.append(
                        str(getInflection(lemma, tag="NN")[0]) + " " + str(tagged[i][0])
                    )
                else:
                    res.append(
                        "ERROR: You need to use a singular noun with ("
                        + str(tagged[i][0])
                        + ")"
                    )
    return res


def PluralNoun(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][7])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["are", "were"]
            and i - 1 >= 0
            and str(tagged[i - 1][2]) == "NOUN"
        ):
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i - 1][0]), "n")
            if (
                getInflection(lemma, tag="NNS") != None
                and str(getInflection(lemma, tag="NNS")[0]) != str(tagged[i - 1][0])
                and str(getInflection(lemma, tag="NNS")[0]).lower() in word_list
            ):
                res.append(
                    str(getInflection(lemma, tag="NNS")[0]) + " " + str(tagged[i][0])
                )
            elif str(tagged[i - 1][1]) != "NNS":
                res.append(
                    "ERROR: You need to use a plural noun with ("
                    + str(tagged[i][0])
                    + ")"
                )
        if str(tagged[i][1]) == "NNS":
            lemma = wordnet_lemmatizer.lemmatize(str(tagged[i][0]), "n")
            if (
                getInflection(lemma, tag="NNS") != None
                and str(getInflection(lemma, tag="NNS")[0]).lower() != str(tagged[i][0]).lower()
                and str(getInflection(lemma, tag="NNS")[0]).lower() in word_list
            ):
                res.append(str(getInflection(lemma, tag="NNS")[0]))
    return res


def Noun_Checker(sentence):
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
    Noun = {}

    Noun["Singular Noun"] = SingularNoun(tagged)
    Noun["Plural Noun"] = PluralNoun(tagged)

    return Noun


# sentence3 = "The mans work."
# res3 = Noun_Checker(sentence3)
# print(res3)