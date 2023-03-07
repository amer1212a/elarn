import spacy

nlp = spacy.load("en_core_web_sm")


def PossessivesSingularNouns(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["NN"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["'s"]
        ):
            res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))

    return res


def PossessivesPluralNouns(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            tagged[i][1] in ["NNS"]
            and str(tagged[i][0]).endswith("s")
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["'"]
        ):
            res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))

        if (
            tagged[i][1] in ["NNS"]
            and not str(tagged[i][0]).endswith("s")
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["'s"]
        ):
            res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))

    return res


def PossessivesAdjectives(tagged):
    res = []
    listofP = ["my", "your", "his", "her", "its", "our", "their"]
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in listofP and tagged[i][5] in ["NOUN"]:
            res.append(str(tagged[i][0]) + " " + str(tagged[i][3]))

    return res


def PossessivesPronouns(tagged):
    res = []
    listofP = ["mine", "yours", "his", "hers", "ours", "theirs"]
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in listofP:
            res.append(str(tagged[i][0]))

    return res


def determiners_Possessives(sentence):
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
    Possessives = {}
    Possessives["Possessives Singular Nouns"] = PossessivesSingularNouns(tagged)
    Possessives["Possessives Plural Nouns"] = PossessivesPluralNouns(tagged)
    Possessives["Possessives Adjectives"] = PossessivesAdjectives(tagged)
    Possessives["Possessives Pronouns"] = PossessivesPronouns(tagged)

    return Possessives


#####
# sentence1 = "it's mine"
# res1 = determiners_Possessives(sentence1)
# print(res1)


##########
# sentence1 = "that's our house"
# res1 = determiners_Possessives(sentence1)
# print(res1)
#
# sentence1 = "my great mother"
# res1 = determiners_Possessives(sentence1)
# print(res1)
#
# sentence1 = "he's broken his beautiful arm"
# res1 = determiners_Possessives(sentence1)
# print(res1)

###########
# sentence1 = "sally drove her friend's car"
# res1 = determiners_Possessives(sentence1)
# print(res1)
#
# sentence1 = "this is my parents' house"
# res1 = determiners_Possessives(sentence1)
# print(res1)
#
# sentence1 = "there are men's shoes"
# res1 = determiners_Possessives(sentence1)
# print(res1)

# sentence1 = "My beautiful car is very old"
# res1 = determiners_Possessives(sentence1)
# print(res1)
