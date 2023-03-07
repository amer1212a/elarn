# output count_of_linking_words / text.length
# output[0,2]
# if count ++ --> result ++

from helper_function import ScallingDomain


linkingwords = [
    "first of all",
    "first",
    "firstly",
    "second",
    "secondly",
    "third",
    "thirdly",
    "next",
    "then",
    "finally",
    "in addition",
    "additionally",
    "an additional" "moreover",
    "furthermore",
    "similarly",
    "likewise",
    "but",
    "however",
    "nevertheless",
    "nonetheless",
    "in spite of",
    "despite",
    "in contrast",
    "on the contrary",
    "on the other hand",
    "conversely",
    "due to",
    "owing to",
    "as a result",
    "as a consequence",
    "therefore",
    "for that reason",
    "consequently",
    "in the beginning",
    "at the beginning",
    "at last",
    "lastly",
    "eventually",
    "before",
    "until",
    "as soon as",
    "while",
    "during",
    "all in all",
    "briefly",
    "to sum up",
    "to summarise",
    "to conclude",
    "concluding",
    "in conclusion",
    "for",
    "because",
    "since",
    "as",
]


def getValue(count_of_linking_words, len_text):
    A = (count_of_linking_words / len_text) * 100
    #  A in [0,100]
    A_new = ScallingDomain(A, 0, 100, 0, 2)
    return A_new


def LinkingWords(nlp, text):
    doc = nlp(text)
    tokens = [
        (
            str(word).lower(),
            word.pos_,
        )
        for word in doc
    ]

    count_of_linking_words = 0
    for word in linkingwords:
        if word in str(text).lower():
            count_of_linking_words = count_of_linking_words + str(text).lower().count(
                str(" " + word)
            )

    words = []
    for i in range(len(tokens)):
        if str(tokens[i][1]) != "PUNCT":
            words.append(tokens[i][0])

    # print(count_of_linking_words)
    # print(len(words))

    res = getValue(count_of_linking_words, len(words))
    return res