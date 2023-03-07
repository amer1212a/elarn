def PastSimple(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() == "did"
            and str(tagged[i + 1][0]).lower() in ["not", "n't"]
            and tagged[i + 2][1] in ["VB"]
            and "?" not in mymap
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )
        elif tagged[i][1] in ["VBD"] and "?" not in mymap:
            if i + 1 >= len(tagged):
                res.append(str(tagged[i][0]))
            elif i + 1 < len(tagged) and tagged[i + 1][1] not in ["VBG", "VBN"]:
                if i + 2 == len(tagged):
                    res.append(str(tagged[i][0]))
                if i + 2 < len(tagged) and tagged[i + 2][1] not in ["VBG", "VBN"]:
                    res.append(str(tagged[i][0]))

        # Question
        if tagged[i][1] in ["VB"] and "?" in mymap and "did" in mymap:
            if "n't" in mymap:
                res.append("didn't __ " + str(tagged[i][0]) + " ?")
            else:
                res.append("did __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VBD"]
            and "?" in mymap
            and "did" not in mymap
            and tagged[i][4] not in ["VBG", "VBN"]
        ):
            res.append(str(tagged[i][0]) + " ?")

    return res


def PastContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            i + 1 < len(tagged)
            and tagged[i][1] in ["VBD"]
            and tagged[i + 1][1] in ["VBG"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
        if (
            i + 2 < len(tagged)
            and tagged[i][1] in ["VBD"]
            and str(tagged[i + 1][0]).lower() in ["not", "n't"]
            and tagged[i + 2][1] in ["VBG"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        # Question
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["was", "were"]
            and tagged[i][4] in ["VBG"]
            and "?" in mymap
        ):
            res.append(str(tagged[i][0]) + " __ " + str(tagged[i][3]) + " ?")
    return res


def PastPerfect(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and tagged[i + 1][2] in ["ADV"]
            and tagged[i + 2][1] in ["VBN", "VBD"]
            and tagged[i + 3][1] not in ["VBG"]
        ) or (
            i + 3 >= len(tagged)
            and i + 2 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and tagged[i + 1][2] in ["ADV"]
            and tagged[i + 2][1] in ["VBN", "VBD"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        elif (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and tagged[i + 1][1] in ["VBN", "VBD"]
            and tagged[i + 2][1] not in ["VBG"]
        ) or (
            i + 2 >= len(tagged)
            and i + 1 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and tagged[i + 1][1] in ["VBN", "VBD"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))

        elif (
            i + 4 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and str(tagged[i + 1][0]) in ["not", "n't"]
            and tagged[i + 2][2] in ["ADV"]
            and tagged[i + 3][1] in ["VBN", "VB"]
            and tagged[i + 4][1] not in ["VBG"]
        ) or (
            i + 4 >= len(tagged)
            and i + 3 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and str(tagged[i + 1][0]) in ["not", "n't"]
            and tagged[i + 2][2] in ["ADV"]
            and tagged[i + 3][1] in ["VBN", "VB"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
            )

        elif (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and str(tagged[i + 1][0]) in ["not", "n't"]
            and tagged[i + 2][1] in ["VBN", "VB"]
            and tagged[i + 3][1] not in ["VBG"]
        ) or (
            i + 3 >= len(tagged)
            and i + 2 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and str(tagged[i + 1][0]) in ["not", "n't"]
            and tagged[i + 2][1] in ["VBN", "VB"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        # Question
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["had"]
            and tagged[i][4] in ["VBN"]
            and "?" in mymap
        ):
            res.append(str(tagged[i][0]) + " __ " + str(tagged[i][3]) + " ?")
    return res


def PastPerfectContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and str(tagged[i + 1][0]).lower() in ["been"]
            and tagged[i + 2][1] in ["VBG"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
            )

        elif (
            i + 3 < len(tagged)
            and str(tagged[i][0]).lower() == "had"
            and str(tagged[i + 1][0]).lower() in ["not", "n't"]
            and str(tagged[i + 2][0]).lower() in ["been"]
            and tagged[i + 3][1] in ["VBG"]
        ):
            res.append(
                str(tagged[i][0])
                + " "
                + str(tagged[i + 1][0])
                + " "
                + str(tagged[i + 2][0])
                + " "
                + str(tagged[i + 3][0])
            )

        # Question
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["had"]
            and tagged[i][4] in ["VBG"]
            and "?" in mymap
            and "been" in mymap
        ):
            res.append(str(tagged[i][0]) + " __ been " + str(tagged[i][3]) + " ?")
    return res