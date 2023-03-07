# output[0,3] for incorrect grammar and [0,3] for correct grammar
# for correct grammar : if count ++ --> result ++
# for incorrect grammar : if count ++ --> result --
from helper_function import ScallingDomain
import json

f = open(
    "levels.json",
)
data = json.load(f)


def getValue(count_incorrect_grammar, count_correct_grammar):
    A = count_correct_grammar / (count_incorrect_grammar + count_correct_grammar)
    # A == [0,1]
    A_new = ScallingDomain(A, 0, 1, 0, 13)
    return A_new


def Grammars(level, grammaranalyzer, grammarcorrecter):
    Grammar = []
    listgrammarforonelevel = []
    if level == "A1":
        listgrammarforonelevel = data["A1"]
    if level == "A2":
        listgrammarforonelevel = data["A1"] + data["A2"]
    if level == "B1":
        listgrammarforonelevel = data["A1"] + data["A2"] + data["B1"]
    if level == "B2":
        listgrammarforonelevel = data["A1"] + data["A2"] + data["B1"] + data["B2"]
    if level == "C1":
        listgrammarforonelevel = (
            data["A1"] + data["A2"] + data["B1"] + data["B2"] + data["C1"]
        )
    if level == "C2":
        listgrammarforonelevel = (
            data["A1"] + data["A2"] + data["B1"] + data["B2"] + data["C1"] + data["C2"]
        )

    for i in listgrammarforonelevel:
        Grammar.append(i)

    count_incorrect_grammar = 0
    for key, value in grammarcorrecter.items():
        if str(key) in Grammar:
            count_incorrect_grammar = count_incorrect_grammar + len(value)

    count_correct_grammar = 0
    for key, value in grammaranalyzer.items():
        if str(key) in Grammar:
            count_correct_grammar = count_correct_grammar + len(value)

    res = getValue(count_incorrect_grammar, count_correct_grammar)
    return res
