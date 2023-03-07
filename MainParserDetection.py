from TenseDetection import determine_tense_input
from ConditionalsDetection import ConditionalDet
from ModalsDetection import determine_modals
from PronounsDetection import determine_pronouns
from DeterminersAndQuantifiersDetection import determine_Determiners
from PossessivesDetection import determiners_Possessives
from AdjectivesDetection import determiners_Adjectives
from AdverbialsDetection import determine_adverbials
from NounDetection import determine_nouns


def ParserAnalyzer(text):
    # print(text)
    tenses = determine_tense_input(text)
    conditionals = ConditionalDet(text)
    modals = determine_modals(text)
    pronouns = determine_pronouns(text)
    determiners = determine_Determiners(text)
    possessives = determiners_Possessives(text)
    adjectives = determiners_Adjectives(text)
    adverbials = determine_adverbials(text)
    nouns = determine_nouns(text)

    maindict = {}
    maindict.update(tenses)
    maindict.update(conditionals)
    maindict.update(modals)
    maindict.update(pronouns)
    maindict.update(determiners)
    maindict.update(possessives)
    maindict.update(adjectives)
    maindict.update(adverbials)
    maindict.update(nouns)

    dic = {}
    for k, v in maindict.items():
        if len(maindict[k]) != 0:
            dic[k] = v

    return dic


parse = ParserAnalyzer("I Playing football yesterday.")
print(parse)
#
# parse = Parser("i am not able to help you")
# print(parse)
#
# parse = Parser("i will probably be able to get there by 9")
# print(parse)


# remove pronouns from nouns##################
# parse = Parser("Alice had a little juice and nothing else.")
# print(parse)


# parse = Parser("I haven't been able to solve this problem. Can you help?")
# print(parse)


# parse = Parser("how long will you have been living here ?")
# print(parse)