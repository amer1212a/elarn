def SimpleFuture(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["MD"]:
            if (
                (i + 2 < len(tagged)
                and tagged[i + 1][1] in ["VB"]
                and tagged[i + 2][1] not in ["VBG", "VBN"]) or (
                    i + 2 >= len(tagged)
                    and i+1 < len(tagged)
                and tagged[i + 1][1] in ["VB"]
                )
            ):
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            if (
                (i + 2 < len(tagged)
                and tagged[i + 1][1] in ["RB"]
                and tagged[i + 2][1] in ["VB"])
            ):
                if i + 3 >= len(tagged):
                    res.append(
                        str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                        + " "
                        + str(tagged[i + 2][0])
                    )
                elif i + 3 < len(tagged) and tagged[i + 3][1] not in ["VBG", "VBN"]:
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
            tagged[i][1] in ["VB"]
            and "will" in mymap
            and "?" in mymap
            and tagged[i][4] not in ["VBG", "VBN"]
        ):
            res.append("will __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VB"]
            and "shall" in mymap
            and "?" in mymap
            and tagged[i][4] not in ["VBG", "VBN"]
        ):
            res.append("shall __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VB"]
            and "wo" in mymap
            and "n't" in mymap
            and "?" in mymap
            and tagged[i][4] not in ["VBG", "VBN"]
        ):
            res.append("won't __ " + str(tagged[i][0]) + " ?")

    return res


def FutureContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["MD"]:
            if (
                i + 2 < len(tagged)
                and tagged[i + 1][1] in ["VB"]
                and tagged[i + 2][1] in ["VBG"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
            if (
                i + 3 < len(tagged)
                and tagged[i + 1][1] in ["RB"]
                and tagged[i + 2][1] in ["VB"]
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

        if (
            i + 2 < len(tagged)
            and str(tagged[i][0]).lower() == "going"
            and str(tagged[i + 1][0]).lower() == "to"
            and str(tagged[i + 2][0]).lower() == "be"
        ):
            if i + 3 < len(tagged) and tagged[i + 3][1] in ["VBG"]:
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                    + " "
                    + str(tagged[i + 3][0])
                )
            if (
                i + 4 < len(tagged)
                and tagged[i + 3][1] in ["RB"]
                and tagged[i + 4][1] in ["VBG"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                    + " "
                    + str(tagged[i + 3][0])
                    + " "
                    + str(tagged[i + 4][0])
                )

        # Question
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["be"]
            and "will" in mymap
            and "?" in mymap
            and tagged[i][4] in ["VBG"]
        ):
            res.append("will __ be " + str(tagged[i][3]) + " ?")

        if (
            str(tagged[i][0]).lower() in ["be"]
            and "wo" in mymap
            and "n't" in mymap
            and "?" in mymap
            and tagged[i][4] in ["VBG"]
        ):
            res.append("won't __ be " + str(tagged[i][3]) + " ?")

    return res


def FuturePerfect(tagged):
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["MD"]:
            if (
                i + 3 < len(tagged)
                and str(tagged[i + 1][0]) == "have"
                and tagged[i + 2][1] in ["VBN"]
                and tagged[i + 3][1] not in ["VBG"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
            if (
                i + 4 < len(tagged)
                and tagged[i + 1][1] in ["RB"]
                and str(tagged[i + 2][0]) == "have"
                and tagged[i + 3][1] in ["VBN"]
                and tagged[i + 4][1] not in ["VBG"]
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
            str(tagged[i][0]).lower() in ["have"]
            and "will" in mymap
            and tagged[i][4] in ["VBN"]
        ):
            if "?" in mymap:
                res.append("will __ have " + str(tagged[i][3]) + " ?")
            else:
                mymap2 = map(str, tagged[i + 1][6])
                mymap2 = list(map(str.lower, mymap2))
                if "?" in mymap2:
                    res.append("will __ have " + str(tagged[i][3]) + " ?")

        if (
            str(tagged[i][0]).lower() in ["have"]
            and "wo" in mymap
            and "n't" in mymap
            and tagged[i][4] in ["VBN"]
        ):
            if "?" in mymap:
                res.append("won't __ have " + str(tagged[i][3]) + " ?")
            else:
                mymap2 = map(str, tagged[i + 1][6])
                mymap2 = list(map(str.lower, mymap2))
                if "?" in mymap2:
                    res.append("won't __ have " + str(tagged[i][3]) + " ?")

    return res


def FuturePerfectContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["MD"]:
            if (
                i + 3 < len(tagged)
                and str(tagged[i + 1][0]) == "have"
                and str(tagged[i + 2][0]) == "been"
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
            if (
                i + 3 < len(tagged)
                and tagged[i + 1][1] in ["RB"]
                and str(tagged[i + 2][0]) == "have"
                and str(tagged[i + 3][0]) == "been"
                and tagged[i + 4][1] in ["VBG"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                    + " "
                    + str(tagged[i + 3][0])
                    + " "
                    + str(tagged[i + 4][0])
                )

        # Question
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if (
            str(tagged[i][0]).lower() in ["have"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["been"]
            and "will" in mymap
            and "?" in mymap
            and tagged[i][4] in ["VBG"]
        ):
            res.append("will __ have been " + str(tagged[i][3]) + " ?")

        if (
            str(tagged[i][0]).lower() in ["have"]
            and i + 1 < len(tagged)
            and str(tagged[i + 1][0]).lower() in ["been"]
            and "wo" in mymap
            and "n't" in mymap
            and "?" in mymap
            and tagged[i][4] in ["VBG"]
        ):
            res.append("won't __ have been " + str(tagged[i][3]) + " ?")

    return res
