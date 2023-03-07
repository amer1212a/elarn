import spacy

nlp = spacy.load("en_core_web_sm")


def Can(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["can"] and tagged[i][1] in ["MD"]:
            res.append(str(tagged[i][0]))
        if (
            str(tagged[i][0]).lower() in ["ca"]
            and tagged[i][1] in ["MD"]
            and i + 1 <= len(tagged)
            and str(tagged[i + 1][0]).lower() in ["not"]
        ):
            res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
        if (
            str(tagged[i][0]).lower() in ["ca"]
            and tagged[i][1] in ["MD"]
            and i + 1 <= len(tagged)
            and str(tagged[i + 1][0]).lower() in ["n't"]
        ):
            res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
    return res


def Could(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["could"] and tagged[i][1] in ["MD"]:
            if i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            elif i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))
    return res


def Past_BeAbleTo(tagged):
    res = []
    listofverbmodal = [
        "able",
        "allowed",
        "about",
        "bound",
        "going",
        "likely",
        "obliged",
        "supposed",
    ]
    for i in range(len(tagged)):
        if (
            i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in listofverbmodal
            and tagged[i + 1][1] in ["TO"]
        ):
            if i - 1 > 0 and str(tagged[i - 1][0]).lower() in ["was", "were"]:
                res.append(
                    str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
            if (
                i - 2 > 0
                and tagged[i - 1][1] in ["RB"]
                and str(tagged[i - 2][0]).lower() in ["was", "were"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
    return res


def Present_BeAbleTo(tagged):
    res = []
    listofverbmodal = [
        "able",
        "allowed",
        "about",
        "bound",
        "going",
        "likely",
        "obliged",
        "supposed",
    ]
    for i in range(len(tagged)):
        if (
            i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in listofverbmodal
            and tagged[i + 1][1] in ["TO"]
        ):
            if i - 1 > 0 and tagged[i - 1][1] in ["VBP"]:
                res.append(
                    str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
            if (
                i - 2 > 0
                and tagged[i - 1][1] in ["RB"]
                and tagged[i - 2][1] in ["VBP", "VBZ"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
            if (
                i - 2 > 0
                and str(tagged[i - 1][0]).lower() in ["been"]
                and tagged[i - 2][1] in ["VBP", "VBZ"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
            if (
                i - 3 > 0
                and str(tagged[i - 1][0]).lower() in ["been"]
                and tagged[i - 2][1] in ["RB"]
                and tagged[i - 3][1] in ["VBP", "VBZ"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )

    return res


def Future_BeAbleTo(tagged):
    res = []
    listofverbmodal = [
        "able",
        "allowed",
        "about",
        "bound",
        "going",
        "likely",
        "obliged",
        "supposed",
    ]
    for i in range(len(tagged)):
        if (
            i + 1 < len(tagged)
            and str(tagged[i][0]).lower() in listofverbmodal
            and tagged[i + 1][1] in ["TO"]
        ):
            if (
                i - 2 > 0
                and str(tagged[i - 1][0]).lower() in ["be"]
                and tagged[i - 2][1] in ["MD"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
            if (
                i - 3 > 0
                and str(tagged[i - 1][0]).lower() in ["be"]
                and tagged[i - 2][1] in ["RB"]
                and tagged[i - 3][1] in ["MD"]
            ):
                res.append(
                    str(tagged[i - 3][0])
                    + " "
                    + str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                )
            elif i - 1 > 0 and str(tagged[i - 1][0]).lower() in ["be"]:
                if (
                    (i - 2 > 0 and tagged[i - 2][1] in ["MD"])
                    or (i - 3 > 0 and tagged[i - 3][1] in ["MD"])
                    or (i - 4 > 0 and tagged[i - 4][1] in ["MD"])
                ):
                    res.append(
                        str(tagged[i - 1][0])
                        + " "
                        + str(tagged[i][0])
                        + " "
                        + str(tagged[i + 1][0])
                    )
    return res


def Shall(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["shall"]:
            if i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))
        if str(tagged[i][0]).lower() in ["sha"]:
            if i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
    return res


def Should(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["should"]:
            if i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif i + 1 <= len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))
    return res


def May(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["may"]:
            if i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))

    return res


def Might(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["might"]:
            if i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))
    return res


def Must(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["must"]:
            if i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))

    return res


def Will(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["will", "wo", "'ll"]:
            if i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif i + 1 < len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))

    return res


def Would(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["would"]:
            if i + 2 < len(tagged) and str(tagged[i + 1][0]).lower() in ["not"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            elif i + 2 < len(tagged) and str(tagged[i + 1][0]).lower() in ["n't"]:
                res.append(str(tagged[i][0]) + str(tagged[i + 1][0]))
            else:
                res.append(str(tagged[i][0]))
    return res


def HadBetter(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["better"]:
            if i - 1 > 0 and str(tagged[i - 1][0]).lower() in ["'d", "had"]:
                res.append(str(tagged[i - 1][0]) + " " + str(tagged[i][0]))
            if (
                i - 2 > 0
                and str(tagged[i - 1][0]).lower() in ["not", "n't"]
                and str(tagged[i - 2][0]).lower() in ["'d", "had"]
            ):
                res.append(
                    str(tagged[i - 2][0])
                    + " "
                    + str(tagged[i - 1][0])
                    + " "
                    + str(tagged[i][0])
                )
    return res


def OughtTo(tagged):
    res = []
    for i in range(len(tagged)):
        if str(tagged[i][0]).lower() in ["ought"]:
            if i + 1 < len(tagged) and tagged[i + 1][1] in ["TO"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            if (
                i + 2 < len(tagged)
                and str(tagged[i + 1][0]).lower() in ["not", "n't"]
                and tagged[i + 2][1] in ["TO"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
    return res


def UsedTo(tagged):
    res = []
    for i in range(len(tagged)):
        mymap = map(str, tagged[i][6])
        mymap = list(map(str.lower, mymap))
        if str(tagged[i][0]).lower() in ["used"]:
            if i + 1 < len(tagged) and tagged[i + 1][1] in ["TO"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            if (
                i + 2 < len(tagged)
                and str(tagged[i + 1][0]).lower() in ["not", "n't"]
                and tagged[i + 2][1] in ["TO"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
        if (
            str(tagged[i][0]).lower() in ["use"]
            and i - 2 >= 0
            and str(tagged[i - 1][1]) == "RB"
            and str(tagged[i - 2][0]).lower() == "did"
        ) or (str(tagged[i][0]).lower() in ["use"] and "did" in mymap and "?" in mymap):
            if i + 1 < len(tagged) and tagged[i + 1][1] in ["TO"]:
                res.append(str(tagged[i][0]) + " " + str(tagged[i + 1][0]))
            if (
                i + 2 < len(tagged)
                and str(tagged[i + 1][0]).lower() in ["not", "n't"]
                and tagged[i + 2][1] in ["TO"]
            ):
                res.append(
                    str(tagged[i][0])
                    + " "
                    + str(tagged[i + 1][0])
                    + " "
                    + str(tagged[i + 2][0])
                )
    return res


def determine_modals(sentence):
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
    modals = {}
    modals["Modals (can)"] = Can(tagged)
    modals["Modals (could)"] = Could(tagged)

    modals["Modals (be able to) in Past tense"] = Past_BeAbleTo(tagged)
    modals["Modals (be able to) in Present tense"] = Present_BeAbleTo(tagged)
    modals["Modals (be able to) in Future tense"] = Future_BeAbleTo(tagged)

    modals["Modals (may)"] = May(tagged)
    modals["Modals (might)"] = Might(tagged)

    modals["Modals (will)"] = Will(tagged)
    modals["Modals (would)"] = Would(tagged)

    modals["Modals (shall)"] = Shall(tagged)
    modals["Modals (should)"] = Should(tagged)

    modals["Modals (must)"] = Must(tagged)
    modals["Modals (Had Better)"] = HadBetter(tagged)

    modals["Semi-Modals (Ought To)"] = OughtTo(tagged)
    modals["Semi-Modals (Used To)"] = UsedTo(tagged)

    return modals


# sentence1 = "We used to love going to the museum, didn’t we?"
# res1 = determine_modals(sentence1)
# print(res1)


# sentence1 = "We shan't know the result of the tests till Tuesday."
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "The management shall not be responsible for damage to personal property."
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "The good news is I shall be able to join you at your meeting next week."
# res1 = determine_modals(sentence1)
# print(res1)

# sentence1 = "dan would help you if you asked him"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you may go home now"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "students may not travel for free"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you might have told me you weren't coming"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you might be more polite"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i might see you tomorrow"
# res1 = determine_modals(sentence1)
# print(res1)
#
#
#
# sentence1 = "they mustn't have been hungry"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "it must be quite late"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you mustn't say anything to her"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you can be really annoying"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you shouldn't be sitting"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "george could really help you"
# res1 = determine_modals(sentence1)
# print(res1)
#
# print("past")
# sentence1 = "i should have booked a table in advance"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you shouldn't have eaten so mach chocolate"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "george could really have helped you"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "anne ought to be at home by now"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "some of you will have met me before"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "the plane should have landed by now"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "that'll be for me"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "that will be for me"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "he won't understand"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you should smoke less"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "we had not better leave soon"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "we'd better leave soon"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you ought to thank her"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you ought not to thank her"
# res1 = determine_modals(sentence1)
# print(res1)
#
#
# sentence1 = "i am not able to help you at the moment"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you are able to help you at the moment"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i have been able to swim since i was five"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i will be able to get there by 9"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i was able to swim when i was five"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i was not able to understand it"
# res1 = determine_modals(sentence1)
# print(res1)
#
#
#
# sentence1 = "she could speak several language"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "they could come by car"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "they could have arrived by now"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "it could be very cold"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i could give you a lift to the station"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "we could meet at th weekend"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you could eat out tonight"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "she could speak several language"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "it couldn't be very cold"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i couldn't give you a lift to the station"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "we could not meet at th weekend"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you couldn't eat out tonight"
# res1 = determine_modals(sentence1)
# print(res1)
#
#
# sentence1 = "i can see you"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "she can speak several language"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i can't breathe"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "you can go home now"
# res1 = determine_modals(sentence1)
# print(res1)
#
# sentence1 = "i can do that for you if you like"
# res1 = determine_modals(sentence1)
# print(res1)