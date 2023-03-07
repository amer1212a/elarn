import spacy

nlp = spacy.load("en_core_web_sm")


def ADV(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][2] in ["ADV"]
            and tagged[i][1] in ["RB"]
            and str(tagged[i][0]).lower() not in ["n't", "not"]
        ):
            res.append(str(tagged[i][0]))
        if (
            tagged[i][2] in ["ADP"]
            and i + 1 <= len(tagged)
            and str(tagged[i][0]).lower() not in ["if"]
        ):
            if i + 2 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["the", "a"]:
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
            else:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
        if (
            str(tagged[i][0]).lower() in ["like"]
            and i - 1 > 0
            and tagged[i - 1][2] in ["VERB"]
        ):
            if i + 2 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["the", "a"]:
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
            else:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
    return res


def determine_adverbials(sentence):
    doc = nlp(sentence)
    tagged = [
        (
            word,
            word.tag_,
            word.pos_,
            word.head.text,
            word.head.tag_,
            word.head.pos_,
            [child for child in word.head.children],
        )
        for word in doc
    ]
    # print(tagged)
    adverbials = {}
    adverbials["adverbials"] = ADV(tagged)

    return adverbials


# sentence1 = "i will probably be able to get there by 9"
# res1 = determine_adverbials(sentence1)
# print(res1)

# sentence1 = "Perhaps the weather will be fine."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "Maybe it won't rain."
# res1 = determine_adverbials(sentence1)
# print(res1)

# sentence1 = "She was born in 1978."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "They have lived here since 2004."
# res1 = determine_adverbials(sentence1)
# print(res1)

# sentence1 = "Birmingham is 250 kilometres from London."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "We live in Birmingham. London is 250 kilometres away."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "There was a storm during the night."
# res1 = determine_adverbials(sentence1)
# print(res1)

# sentence1 = "They are abroad at present."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "You'll find it inside."
# res1 = determine_adverbials(sentence1)
# print(res1)

# sentence1 = "She slept like a baby."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "Her hands felt like ice."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "It smells like fresh bread."
# res1 = determine_adverbials(sentence1)
# print(res1)

# sentence1 = "He spoke angrily."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "He opened the door quietly."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "They all worked hard."
# res1 = determine_adverbials(sentence1)
# print(res1)
#
# sentence1 = "We usually spent our holidays with our grandparents."
# res1 = determine_adverbials(sentence1)
# print(res1)