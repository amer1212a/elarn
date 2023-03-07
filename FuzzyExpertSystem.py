import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

grammar = ctrl.Antecedent(np.arange(0, 13, 0.1), "grammar")
linking_words = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "linking_words")
new_vocabulary = ctrl.Antecedent(np.arange(0, 1.1, 0.1), "new_vocabulary")
repetation_error = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "repetation_error")
spell_error = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "spell_error")
# print(grammar)
# print(linking_words)
# print(new_vocabulary)
# print(repetation_error)
# print(spell_error)

score = ctrl.Consequent(np.arange(0, 21, 1), "score")
# print(score)

grammar.automf(3)
linking_words.automf(3)
new_vocabulary["low"] = fuzz.trimf(new_vocabulary.universe, [0, 0, 0.7])
new_vocabulary["high"] = fuzz.trimf(new_vocabulary.universe, [0.5, 0.7, 1])
repetation_error.automf(3)
spell_error.automf(3)

score["low"] = fuzz.trimf(score.universe, [0, 0, 10])
score["medium"] = fuzz.trimf(score.universe, [5, 10, 15])
score["high"] = fuzz.trimf(score.universe, [10, 15, 20])

# You can see how these look with .view()
# quality['average'].view()
# grammar.view()
# linking_words.view()
# new_vocabulary.view()
# repetation_error.view()
# spell_error.view()
# score.view()
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [10, 20, 30])
# plt.show()

rule0 = ctrl.Rule(grammar["poor"], score["low"])
rule1 = ctrl.Rule(
    grammar["poor"]
    & linking_words["poor"]
    & new_vocabulary["low"]
    & repetation_error["good"]
    & spell_error["good"],
    score["low"],
)
rule2 = ctrl.Rule(
    grammar["average"]
    & linking_words["poor"]
    & new_vocabulary["low"]
    & repetation_error["good"]
    & spell_error["good"],
    score["low"],
)
rule3 = ctrl.Rule(
    grammar["average"]
    & (
        linking_words["poor"]
        | new_vocabulary["low"]
        | repetation_error["good"]
        | spell_error["good"]
    ),
    score["low"],
)
rule4 = ctrl.Rule(
    grammar["average"]
    & (
        linking_words["good"]
        | new_vocabulary["high"]
        | repetation_error["poor"]
        | spell_error["poor"]
    ),
    score["medium"],
)
rule5 = ctrl.Rule(
    grammar["poor"]
    & linking_words["good"]
    & new_vocabulary["high"]
    & repetation_error["poor"]
    & spell_error["poor"],
    score["medium"],
)
rule6 = ctrl.Rule(
    grammar["average"]
    & linking_words["average"]
    & repetation_error["average"]
    & spell_error["average"],
    score["medium"],
)
rule7 = ctrl.Rule(
    grammar["good"]
    & linking_words["good"]
    & repetation_error["good"]
    & spell_error["good"],
    score["high"],
)
rule8 = ctrl.Rule(
    grammar["good"]
    & linking_words["average"]
    & repetation_error["poor"]
    & spell_error["average"],
    score["high"],
)
rule9 = ctrl.Rule(
    grammar["good"] & new_vocabulary["high"] & repetation_error["poor"],
    score["high"],
)
rule10 = ctrl.Rule(
    grammar["good"] & repetation_error["poor"] & spell_error["poor"], score["high"]
)
rule11 = ctrl.Rule(
    grammar["good"] & new_vocabulary["low"] & linking_words["good"] & repetation_error["poor"] & spell_error["poor"], score["high"]
)

scorring_ctrl = ctrl.ControlSystem(
    [rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,rule10,rule11]
)
scorring = ctrl.ControlSystemSimulation(scorring_ctrl)


def Compute_Score(grammar, linking_word, new_vocabulary, repetation_error, spell_error):
    scorring.input["grammar"] = round(grammar, 1)
    scorring.input["linking_words"] = round(linking_word, 1)
    scorring.input["new_vocabulary"] = round(new_vocabulary, 1)
    scorring.input["repetation_error"] = round(repetation_error, 1)
    scorring.input["spell_error"] = round(spell_error, 1)

    scorring.compute()
    # score.view(sim=scorring)
    res_score = scorring.output["score"]
    
    # import matplotlib.pyplot as plt
    # plt.plot([1, 2, 3], [10, 20, 30])
    # plt.show()
    return res_score


# res = Compute_Score(
#     grammar=11.34531,
#     linking_word=1.34531,
#     new_vocabulary=0.6768,
#     repetation_error=0.34531,
#     spell_error=0.34531,
# )
# print(res)
