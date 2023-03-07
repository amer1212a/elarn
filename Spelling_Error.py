# output number of error spell
# output[0,2]
# if count ++ --> result --
from helper_function import ScallingDomain
from nltk.corpus import brown
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


def getValue(count_error, len_text, autocomplete):
    A = (count_error / len_text) * 100
    #  A in [0,100]
    if autocomplete == "true":
        A_new = ScallingDomain(A, 0, 100, 0, 1.5)
    else:
        A_new = ScallingDomain(A, 0, 100, 0, 2)
    return A_new


def Spelling_Error(nlp, text, autocomplete):
    Listofwordspellerror = []
    word_list = brown.words()
    word_set = set(word_list)
    count_error = 0
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
        if str(tokens[i][1]) != "PUNCT":
            words.append(str(tokens[i][0]))

    ents = [(e.text, e.label_, e.kb_id_) for e in doc.ents]
    entities = []
    for i1, j1, k1 in ents:
        entities.append(str(i1).lower())

    for i in range(len(tokens)):
        if (
            str(tokens[i][1]) != "PUNCT"
            and str(tokens[i][0]).lower() not in word_set
            and str(tokens[i][0]).lower() not in stop_words
            and str(tokens[i][0]).lower() not in entities
        ):
            count_error = count_error + 1
            Listofwordspellerror.append(str(tokens[i][0]))

    # print(count_error)
    # print(len(words))
    res = getValue(count_error, len(words), autocomplete)

    return res , Listofwordspellerror