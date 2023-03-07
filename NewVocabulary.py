# count of new words
# output [0,1]
# if count ++ --> result ++
from helper_function import ScallingDomain
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


def getValue(number_of_words, len_text, translate):
    A = (number_of_words / len_text) * 100
    #  A in [0,100]
    if translate == "true":
        A_new = ScallingDomain(A, 0, 100, 0, 0.7)
    else:
        A_new = ScallingDomain(A, 0, 100, 0, 1)
    return A_new


def NewVocabulary(nlp, text, translate):
    # number_of_words_defualt = data[str(level)][0]
    doc = nlp(text)
    tokens = [
        (
            str(word).lower(),
            word.pos_,
        )
        for word in doc
    ]
    words = []
    for i in range(len(tokens)):
        if str(tokens[i][1]) != "PUNCT" and str(tokens[i][0]).lower() not in stop_words:
            words.append(tokens[i][0])

    number_of_words = len(set(words))
    # print(len(words))
    # print(number_of_words)
    res = getValue(number_of_words, len(words), translate)

    return res