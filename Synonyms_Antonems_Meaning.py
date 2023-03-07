from PyDictionary import PyDictionary
import spacy
from nltk.corpus import wordnet

nlp = spacy.load('en_core_web_sm')
dictionary=PyDictionary()

def Synonyms(text):
    synonyms = []
    words = text.split()
    for syn in wordnet.synsets(words[0]):
        for lm in syn.lemmas():
                synonyms.append(lm.name())
    # s = dictionary.synonym(words[0])[0:3]
    return set(synonyms)

print(Synonyms("beautiful boy"))

def Antonym(text):
    words = text.split()
    antonyms = []

    for syn in wordnet.synsets(words[0]):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())

    # s = dictionary.antonym(words[0])[0:3]
    return set(antonyms)

print(Antonym("beautiful boy"))

def Meaning(text):
    doc = nlp(text)
    tagged = [(word,word.pos_,) for word in doc]
    s = dictionary.meaning(str(tagged[0][0]))
    if s is not None:
        if tagged[0][1] in ['ADJ','DET']:
            if len(s["Adjective"]) >1:
                return '###'.join(s["Adjective"])
            else:
                return s["Adjective"]
        elif tagged[0][1] in ['NOUN']:
            if len(s["Noun"]) > 1:
                return '###'.join(s["Noun"])
            else:
                return s["Noun"]
        elif tagged[0][1] in ['ADP']:
            if len(s["Adverb"]) > 1:
                return '###'.join(s["Adverb"])
            else:
                return s["Adverb"]
        elif tagged[0][1] in ['VERB','AUX']:
            if len(s["Verb"]) > 1:
                return '###'.join(s["Verb"])
            else:
                return s["Verb"]
        else:
            return "No meaning available"
    else:
        return "No meaning available"

# print(Meaning("are used"))

#############
# import spacy
# import numpy as np
#
# nlp = spacy.load('en_core_web_lg')
#
# def Synonyms(your_word):
#     ms = nlp.vocab.vectors.most_similar(
#         np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=3)
#     words = [nlp.vocab.strings[w] for w in ms[0][0] if ms[2] != 1.0]
#     distances = ms[2]
#     print(distances)
#     return words
#
# print(Synonyms("dog"))

#############################3
# import spacy
# import numpy as np
#
# nlp = spacy.load('en_core_web_lg')
#
# def most_similar(word, topn=3):
#     word = nlp.vocab[str(word)]
#     queries = [
#         w for w in word.vocab
#         if w.is_lower == word.is_lower and w.prob >= -15 and np.count_nonzero(w.vector)
#     ]
#
#     by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
#     # return [(w.lower_,w.similarity(word)) for w in by_similarity[:topn+1] if w.lower_ != word.lower_]
#     return [w.lower_ for w in by_similarity[:topn+1] if w.lower_ != word.lower_]
#
# print(most_similar("dog"))