# from GrammarCorrection.TensesCorrection import Tenses_Checker
from FutureTenseCorrection import FutureTense_Checker
from PresentTenseCorrection import PresentTense_Checker
from PastTenseCorrection import PastTense_Checker

# from ConditionalsDetection import ConditionalDet
from ModalsVerbCorrection import ModalsVerb_Checker
from PronounsCorrection import Pronouns_Checker
from DeterminersCorrection import Determiners_Checker
from PossessivesCorrection import Possessives_Checker
from AdjectiveCorrection import Adjective_Checker

# from AdverbialsDetection import determine_adverbials
from NounCorrection import Noun_Checker


def ParserCorrection(text):
    # tenses = Tenses_Checker(text)
    futuretense = FutureTense_Checker(text)
    pasttense = PastTense_Checker(text)
    presenttense = PresentTense_Checker(text)
    # conditionals = ConditionalDet(text)
    modals = ModalsVerb_Checker(text)
    pronouns = Pronouns_Checker(text)
    determiners = Determiners_Checker(text)
    possessives = Possessives_Checker(text)
    adjectives = Adjective_Checker(text)
    # adverbials = determine_adverbials(text)
    nouns = Noun_Checker(text)

    maindict = {}
    # maindict.update(tenses)
    maindict.update(futuretense)
    maindict.update(pasttense)
    maindict.update(presenttense)
    # maindict.update(conditionals)
    maindict.update(modals)
    maindict.update(pronouns)
    maindict.update(determiners)
    maindict.update(possessives)
    maindict.update(adjectives)
    # maindict.update(adverbials)
    maindict.update(nouns)

    dic = {}
    for k, v in maindict.items():
        if len(maindict[k]) != 0:
            dic[k] = v

    return dic


# parse = ParserCorrection(
#     "The girl hands were chapped by the cold."
# )
# print(parse)
