from FuzzyExpertSystem import Compute_Score
from Spelling_Error import Spelling_Error
from Repetition_phrases import Repetition_phrases
from Grammars import Grammars
from LinkingWords import LinkingWords
from NewVocabulary import NewVocabulary
import spacy

nlp = spacy.load("en_core_web_sm")

# f.close()


def Evaluater(level, text, grammaranalyzer, grammarcorrecter, autocomplete, translate):

    Grammars_score = Grammars(level, grammaranalyzer, grammarcorrecter)
    Repetition_phrases_score = Repetition_phrases(nlp, text)
    SpellingError_score, Listofwordspellerror = Spelling_Error(nlp, text, autocomplete)
    Vocabulary_score = NewVocabulary(nlp, text, translate)
    LinkingWords_score = LinkingWords(nlp, text)

    print(Grammars_score)
    print(Repetition_phrases_score)
    print(SpellingError_score)
    print(Listofwordspellerror)
    print(Vocabulary_score)
    print(LinkingWords_score)

    # res = (
    # Grammars_score
    # + Repetition_phrases_score
    # + SpellingError_score
    # + Vocabulary_score
    # + LinkingWords_score
    # )
    # try:
    #     res = Compute_Score(
    #         Grammars_score,
    #         LinkingWords_score,
    #         Vocabulary_score,
    #         Repetition_phrases_score,
    #         SpellingError_score,
    #     )
    # except:
    #     res = (
    #         Grammars_score
    #         + Repetition_phrases_score
    #         + SpellingError_score
    #         + Vocabulary_score
    #         + LinkingWords_score
    #     )


# analyzer = {"Present Continuous": ["am playing", "am swimming"]}
# correction = {"Past Continuous": ["i was playing", "i was swimming"]}
# Evaluater("A1", "i am playing and i am swiming", analyzer, correction, True, False)

# aa = NewVocabulary(
#     nlp,
#     "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity.",
# )
# print(aa)


# aa = LinkingWords(
#     nlp,
#     "The university tuition fee can be paid monthly. In addition, students are granted free access to the online library. Five houses had been burgled over three weeks. Eventually, the burglar was arrested. There has been a forest fire in the north of the country. As a consequence, smaller villages around the area have been evacuated",
# )
# print(aa)

# aa = Spelling_Error(nlp, "This is my new job. My first neme is Jack.")
# print(aa)

# aa = Repetition_phrases(
#     nlp,
#     "yes It was the best of times, yes it was the worst of times, yes it was the age of wisdom, yes it was the age of foolishness,yes it was the epoch of belief,yes it was the epoch of incredulity. you can do that if you swim , you can do that if you dream, you can do that if you play ",
# )
# print(aa)

# Grammars(
#     "A2",
#     {
#         "Future Simple": ["can play"],
#         "Modals (can)": ["can"],
#         "Specific Determiners": ["the piano"],
#         "Singular Noun": ["tom", "piano"],
#     },
#     {"Past Perfect": ["tom had played", "tom had played"], "Future Simple": ["tom will play"]},
# )
