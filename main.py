import re
import nltk
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace("_", " ").replace("-", " ").lower()
            synonyms.add(synonym)
    return list(synonyms)

def paraphrase_word(word):
    synonyms = get_synonyms(word)
    return synonyms[0] if len(synonyms) > 0 else word

def paraphrase_text(text):
    words = nltk.word_tokenize(text)
    paraphrased_words = [paraphrase_word(word) for word in words]
    return " ".join(paraphrased_words)

with open("input.txt", "r") as input_file:
    text = input_file.read()

paraphrased_text = paraphrase_text(text)

with open("output.txt", "w") as output_file:
    output_file.write(paraphrased_text)
