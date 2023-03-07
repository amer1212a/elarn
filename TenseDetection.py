import spacy
from PresentTenseDetection import *
from FutureTenseDetection import *
from PastTenseDetection import *

nlp = spacy.load("en_core_web_sm")


def determine_tense_input(sentence):
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
    tense = {}

    tense["Present Simple"] = PresentSimple(tagged)
    tense["Present Continuous"] = PresentContinuous(tagged)
    tense["Present Perfect"] = PresentPerfect(tagged)
    tense["Present Perfect Continuous"] = PresentPerfectContinuous(tagged)
    tense["Future Simple"] = SimpleFuture(tagged)
    tense["Future Continuous"] = FutureContinuous(tagged)
    tense["Future Perfect"] = FuturePerfect(tagged)
    tense["Future Perfect Continuous"] = FuturePerfectContinuous(tagged)
    tense["Past Simple"] = PastSimple(tagged)
    tense["Past Perfect"] = PastPerfect(tagged)
    tense["Past Continuous"] = PastContinuous(tagged)
    tense["Past Perfect Continuous"] = PastPerfectContinuous(tagged)
    return tense

# sentence1 = "We're going to get married."
# res1 = determine_tense_input(sentence1)
# print(res1)


# sentence1 = "Had I been buying?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Had we been buying?"
# res1 = determine_tense_input(sentence1)
# print(res1)


##########
# sentence1 = "Had they decided?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Had you decided?"
# res1 = determine_tense_input(sentence1)
# print(res1)


###########
# sentence1 = "Was he playing?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Were you playing?"
# res1 = determine_tense_input(sentence1)
# print(res1)


# sentence1 = "Did she arrive?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Didn't you play?"
# res1 = determine_tense_input(sentence1)
# print(res1)


#######
# sentence1 = "Will I have been living?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Won't I have been living?"
# res1 = determine_tense_input(sentence1)
# print(res1)


##############
# sentence1 = "Will you have arrived ?"
# res1 = determine_tense_input(sentence1)
# print(res1)

#
# sentence1 = "Won't he have arrived?"
# res1 = determine_tense_input(sentence1)
# print(res1)


# sentence1 = "when will you be coming back ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "Will I be staying?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Won't he be staying?"
# res1 = determine_tense_input(sentence1)
# print(res1)


#########
# sentence1 = "when will i help ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "Shall I open the window?"
# res1 = determine_tense_input(sentence1)
# print(res1)


##################
# sentence1 = "why have you been working all week ?"
# res1 = determine_tense_input(sentence1)
# print(res1)

################
# sentence1 = "How many times have you seen this film ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "How many times have you been boss ?"
# res1 = determine_tense_input(sentence1)
# print(res1)


##############
# sentence1 = "where is she sleeping ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "where am i sleeping ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "where are you sleeping ?"
# res1 = determine_tense_input(sentence1)
# print(res1)


# sentence1 = "How do you work ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "How does it work ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "How does sally work ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Are they at home?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Am i at home?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "Is he at home?"
# res1 = determine_tense_input(sentence1)
# print(res1)


###############

# sentence1 = "i am not able to help you at the moment"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i will probably be able to get there by 9"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i was able to swim when i was five"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i was not able to understand it"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i have been able to swim since i was five"
# res1 = determine_tense_input(sentence1)
# print(res1)

# sentence1 = "she could apeak several language"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "they could come by car"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "they could have arrived by now"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "it could be very cold"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i could give you a lift to the station"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "we could meet at th weekend"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "you could eat out tonight"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she could speak several language"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "it couldn't be very cold"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i couldn't give you a lift to the station"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "we could not meet at th weekend"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "you couldn't eat out tonight"
# res1 = determine_tense_input(sentence1)
# print(res1)

# sentence1 = "i can see you"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she can speak several language"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i can't breathe"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "you can go home now"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i can do that for you if you like"
# res1 = determine_tense_input(sentence1)
# print(res1)


# Past Perfect Continuous
# sentence1 = "we had been trying to open the door"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "it had been raining hard"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i hadn't been buying"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "you hadn't been buying"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")
# past perfect
# sentence1 = "she had met him"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she had written articles"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "kate had wanted to see the movie"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i had been to mexico once before"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she had never been to the symphony before last week"
# res1 = determine_tense_input(sentence1)
# print(res1)
#

# past continuous
# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")
# sentence1 = "i was writing article"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "we were shopping in that market"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i was not watching the cricket match"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "you weren't watching the cricket match"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# #past simple
# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")
# sentence1 = "she did not arrive"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "she did not swim"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she didn't arrive"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "she didn't swim"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she arrived yesterday"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she swam yesterday"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she bought yesterday"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "she shone yesterday"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i was not at home"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "you were not at home"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "i saw a movie last week"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "i often played football"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "i went to the theatre last night"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "she had a headache yesterday"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "we gave her a doll"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# sentence1 = "my parents came to visit me"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "we didn't do our homework last night"
# res1 = determine_tense_input(sentence1)
# print(res1)

# sentence1 = "she had gone to bed earlier"
# res1 = determine_tense_input(sentence1)
# print(res1)


# #simple present with adverbs
# sentence1 = "He gets up early in the morning."
# res1 = determine_tense_input(sentence1)
# print(res1)


# Present Continuous question form
# sentence1 = "where am i sleeping ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "where are you sleeping ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "where is he sleeping ?"
# res1 = determine_tense_input(sentence1)
# print(res1)


# Present Simple question form
# sentence1 = "Do you know ?"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "How much does Pauline love pie ?"
# res1 = determine_tense_input(sentence1)
# print(res1)


# # FuturePerfectContinuous
# sentence1 = "I will have been playing."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "I won't have been living"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# print("------------------------------------------------------------------")
#
# # # FuturePerfect
# sentence1 = "They will have written a letter"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "You will not have written a letter."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# print("------------------------------------------------------------------")
#
#
#
# # # FutureContinuous
# sentence1 = "You will be watching"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "I won't be staying."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# print("------------------------------------------------------------------")
#
#
#
# # # SimpleFuture
# sentence1 = "They will help."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "They will not help."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
#
#
# print("------------------------------------------------------------------")
# print("------------------------------------------------------------------")
# print("------------------------------------------------------------------")
#
#
#
#
#
# PresentPerfectContinuous
# sentence1 = "It has not been raining."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "I have not been waiting for one hour."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# print("------------------------------------------------------------------")
#
#
# # PresentPerfect
# sentence1 = "She has not been to the cinema"
# res1 = determine_tense_input(sentence1)
# print(res1)
#
# sentence1 = "She has not visited."
# res1 = determine_tense_input(sentence1)
# print(res1)
#
#
# print("------------------------------------------------------------------")
#
#
#
# #PresentContinuous
# sentence = "it is not sleeping"
# res = determine_tense_input(sentence)
# print(res)
#
# sentence = "they are not sleeping"
# res = determine_tense_input(sentence)
# print(res)
#
#
# print("------------------------------------------------------------------")
#
#
#
# #Simple Present
# sentence = "i don’t write a message"
# res = determine_tense_input(sentence)
# print(res)
#
# sentence = "she doesn’t goes to school"
# res = determine_tense_input(sentence)
# print(res)
#
# sentence = "They are doctors"
# res = determine_tense_input(sentence)
# print(res)
#
# sentence = "lola is a doctors"
# res = determine_tense_input(sentence)
# print(res)
#
# sentence = "boys are a doctors"
# res = determine_tense_input(sentence)
# print(res)