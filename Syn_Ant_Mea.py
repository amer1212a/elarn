import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
import spacy

nlp = spacy.load("en_core_web_sm")
dictionary = PyDictionary()


def synonyms(term):
    response = requests.get("http://www.thesaurus.com/browse/{}".format(term))
    soup = BeautifulSoup(response.text, "html")
    synonym = []
    div1 = soup.find("div",{"id": "meanings"})
    div = div1.find("div", {"data-testid": "word-grid-container"})
    ultag = div.find("ul")
    for litag in ultag.find_all("li"):
        synonym.append(litag.a.text.strip())
    return synonym


print(synonyms("good"))


def antonyms(term):
    response = requests.get("http://www.thesaurus.com/browse/{}".format(term))
    soup = BeautifulSoup(response.text, "html")
    antonym = []
    div1 = soup.find("div",{"id": "antonyms"})
    div = div1.find("div", {"data-testid": "word-grid-container"})
    ultag = div.find("ul")
    for litag in ultag.find_all("li"):
        antonym.append(litag.a.text.strip())
    return antonym


# print(antonyms("good"))


def Meaning(text):
    doc = nlp(text)
    tagged = [
        (
            word,
            word.pos_,
        )
        for word in doc
    ]
    s = dictionary.meaning(str(tagged[0][0]))
    if s is not None:
        if tagged[0][1] in ["ADJ", "DET"]:
            if len(s["Adjective"]) > 1:
                return "###".join(s["Adjective"])
            else:
                return s["Adjective"]
        elif tagged[0][1] in ["NOUN"]:
            if len(s["Noun"]) > 1:
                return "###".join(s["Noun"])
            else:
                return s["Noun"]
        elif tagged[0][1] in ["ADP"]:
            if len(s["Adverb"]) > 1:
                return "###".join(s["Adverb"])
            else:
                return s["Adverb"]
        elif tagged[0][1] in ["VERB", "AUX"]:
            if len(s["Verb"]) > 1:
                return "###".join(s["Verb"])
            else:
                return s["Verb"]
        else:
            return "No meaning available"
    else:
        return "No meaning available"


# print(Meaning("hello"))
