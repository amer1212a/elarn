def PresentSimple(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["VBP", "VBZ", "VB"] and "?" not in map(str, tagged[i][6]):
            if (
                tagged[i - 1][1] not in ["VBD", "VBP", "VBZ", "MD", "VB"]
                and i + 1 < len(tagged)
                # remove RB from bottom tagged[i + 1][1] not in ["VBG", "VBN", "RB"]
                and tagged[i + 1][1] not in ["VBG", "VBN"]
                and str(tagged[i - 1][0]).lower() != "been"
            ):
                if (
                    i - 2 >= 0
                    and tagged[i - 1][1] in ["RB"]
                    and tagged[i - 2][1] not in ["MD", "VBD"]
                ):
                    res.append(str(tagged[i][0]))
                if i - 1 >= 0 and tagged[i - 1][1] in ["PRP", "NN", "NNS", "NNP"]:
                    if i - 2 < 0:
                        res.append(str(tagged[i][0]))
                    if i - 2 >= 0 and tagged[i - 2][1] not in ["VBP", "VBZ"]:
                        res.append(str(tagged[i][0]))

        # Question
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if tagged[i][1] in ["VB"] and "?" in mymap and "do" in mymap:
            res.append("do __ " + str(tagged[i][0]) + " ?")

        if tagged[i][1] in ["VB"] and "?" in mymap and "does" in mymap:
            res.append("does __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VBP", "VBZ"]
            and tagged[i][4] not in ["VBG", "VBN", "VB"]
            and "?" in mymap
        ):
            res.append(str(tagged[i][0]) + " __ ?")

    return res


def PresentContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        if (
            i + 1 < len(tagged)
            and tagged[i][1] in ["VBZ", "VBP"]
            and tagged[i + 1][1] in ["VBG"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            if (
                i + 3 < len(tagged)
                and str(tagged[i + 1][0]).lower() == "going"
                and str(tagged[i + 2][0]).lower() == "to"
                and str(tagged[i + 3][0]).lower() == "be"
            ):
                res.remove(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
        elif (
            i + 2 < len(tagged)
            and tagged[i][1] in ["VBZ", "VBP"]
            and tagged[i + 1][1] in ["RB"]
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
        if tagged[i][1] in ["VBG"] and "?" in mymap and "are" in mymap:
            res.append("are __ " + str(tagged[i][0]) + " ?")

        if tagged[i][1] in ["VBG"] and "?" in mymap and "is" in mymap:
            res.append("is __" + str(tagged[i][0]) + " ?")

        if tagged[i][1] in ["VBG"] and "?" in mymap and "am" in mymap:
            res.append("am __" + str(tagged[i][0]) + " ?")
    return res


def PresentPerfect(tagged):
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] in ["VBP", "VBZ"]:
            if (
                i + 1 < len(tagged)
                and tagged[i + 1][1] in ["VBN"]
                and str(tagged[i + 1][0]).lower() != "been"
            ):
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif (
                i + 2 < len(tagged)
                and tagged[i + 1][1] in ["VBN"]
                and str(tagged[i + 1][0]).lower() == "been"
                and tagged[i + 2][1] not in ["VBG"]
            ):
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif (
                i + 2 < len(tagged)
                and tagged[i + 1][1] in ["RB"]
                and tagged[i + 2][1] in ["VBN"]
                and str(tagged[i + 2][0]).lower() != "been"
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
                and tagged[i + 1][1] in ["RB"]
                and tagged[i + 2][1] in ["VBN"]
                and str(tagged[i + 2][0]).lower() == "been"
                and tagged[i + 3][1] not in ["VBG"]
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
                and tagged[i + 1][2] in ["ADV"]
                and tagged[i + 2][2] in ["ADV"]
                and tagged[i + 3][1] in ["VBN"]
            ):
                if i + 3 < len(tagged) and str(tagged[i + 3][0]).lower() != "been":
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
                    and str(tagged[i + 3][0]).lower() == "been"
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
            tagged[i][1] in ["VBN"]
            and "?" in mymap
            and "have" in mymap
            and str(tagged[i][0]).lower() not in ["been"]
        ):
            res.append("have __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VBN"]
            and "?" in mymap
            and "has" in mymap
            and str(tagged[i][0]).lower() not in ["been"]
        ):
            res.append("has __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VBN"]
            and "?" in mymap
            and "have" in mymap
            and str(tagged[i][0]).lower() in ["been"]
            and i + 1 < len(tagged)
            and tagged[i + 1][1] not in ["VBG"]
        ):
            res.append("have __ " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VBN"]
            and "?" in mymap
            and "has" in mymap
            and str(tagged[i][0]).lower() in ["been"]
            and i + 1 < len(tagged)
            and tagged[i + 1][1] not in ["VBG"]
        ):
            res.append("has __ " + str(tagged[i][0]) + " ?")
    return res


def PresentPerfectContinuous(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))

        if tagged[i][1] in ["VBP", "VBZ"] and "?" not in mymap:
            if (
                i + 3 < len(tagged)
                and tagged[i + 1][1] in ["RB"]
                and str(tagged[i + 2][0]).lower() == "been"
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
            elif (
                i + 2 < len(tagged)
                and str(tagged[i + 1][0]).lower() == "been"
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
        if (
            tagged[i][1] in ["VBG"]
            and "?" in mymap
            and "have" in mymap
            and "been" in mymap
            and ("will" not in mymap and ("wo" not in mymap and "n't" not in mymap))
        ):
            res.append("have __ been " + str(tagged[i][0]) + " ?")

        if (
            tagged[i][1] in ["VBG"]
            and "?" in mymap
            and "has" in mymap
            and "been" in mymap
            and ("will" not in mymap and ("wo" not in mymap and "n't" not in mymap))
        ):
            res.append("has __ been " + str(tagged[i][0]) + " ?")
    return res