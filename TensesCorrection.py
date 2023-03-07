# from GrammarCorrection.PresentTenseCorrection import *
# from GrammarCorrection.PastTenseCorrection import *
# from GrammarCorrection.FutureTenseCorrection import *
# import spacy

# nlp = spacy.load("en_core_web_sm")


# def Tenses_Checker(sentence):
#     doc = nlp(sentence)
#     tagged = [
#         (
#             word,
#             word.tag_,
#             word.pos_,
#             word.head.text,
#             word.head.tag_,
#             word.head.pos_,
#             word.dep_,
#             [child for child in word.head.children],
#         )
#         for word in doc
#     ]
#     # print(tagged)
#     Tenses = {}

#     Tenses["Present Simple"] = PresentSimple(tagged)
#     Tenses["Present Continuous"] = PresentContinuous(tagged)
#     Tenses["Present Perfect"] = PresentPerfect(tagged)
#     Tenses["Present Perfect Continuous"] = PresentPerfectContinuous(tagged)
#     Tenses["Past Simple"] = PastSimple(tagged)
#     Tenses["Past Continuous"] = PastContinuous(tagged)
#     Tenses["Past Perfect"] = PastPerfect(tagged)
#     Tenses["Past Perfect Continuous"] = PastPerfectContinuous(tagged)
#     Tenses["Future Simple"] = FutureSimple(tagged)
#     Tenses["Future Continuous"] = FutureContinuous(tagged)
#     Tenses["Future Perfect"] = FuturePerfect(tagged)
#     Tenses["Future Perfect Continuous"] = FuturePerfectContinuous(tagged)

#     return Tenses


# # sentence3 = "It will not have stopped raining."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "I will not have been play."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)


# # sentence3 = "we will be eat breakfast."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)


# # sentence3 = "You will not been late."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "I will meet him later."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "I will not met him later."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "I not meet him later."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)


# # sentence3 = "She has been sleeping."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "She has not been crying."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)


# # sentence3 = "You had went."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "He have not played."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)


# # error
# # sentence3 = "I am not a pupil."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "We aren't happy."
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "He haven't been lucky!"
# # res3 = Tenses_Checker(sentence3)
# # print(res3)

# # sentence3 = "I haven't be lucky!"
# # res3 = Tenses_Checker(sentence3)
# # print(res3)
