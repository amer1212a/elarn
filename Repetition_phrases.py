# output[0,2] for repetition phrases
# each phrases consists of four words
# if count ++ --> result --
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


def getValue(sum_of_repetition):
    a = sum_of_repetition * (0.5)
    if a > 2:
        return 2
    elif a < 0:
        return 0
    return sum_of_repetition * (0.5)


def Repetition(words):
    phrase = []
    for word in words:
        phrase.append(word)
        if len(phrase) > 4:
            phrase.remove(phrase[0])
        if len(phrase) == 4:
            yield tuple(phrase)


def Repetition_phrases(nlp, text):
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
        if (
            str(tokens[i][1]) != "PUNCT"
        ):  # and str(tokens[i][0]).lower() not in stop_words:
            words.append(tokens[i][0])

    # counts = collections.defaultdict(int)
    # for phrase in Repetition(words):
    #     counts[phrase] += 1

    # print(counts)

    counts = dict()
    for phrase in Repetition(words):
        counts[phrase] = counts.get(phrase, 0) + 1

    print(counts)

    sum_of_repetition = 0
    List_of_set = []
    List_of_set.append({"$"})
    for k, v in counts.items():
        if v >= 3:
            K = set(k)
            # print(K)
            # print(List_of_set)
            X = False
            for seet in List_of_set:
                if len(K.intersection(seet)) > 0:
                    X = True
                    break
            if X == False:
                List_of_set.append(K)
                sum_of_repetition = sum_of_repetition + 1

    res = getValue(sum_of_repetition)

    return res
