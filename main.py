# import pandas as pd
from voxpopuli import Voice

# taille moyenne des phrases en phonèmes

CORPUS_PATH = "french_corpus.txt"

voice = Voice(lang="fr")
phonemes_count = []

def extract_sentence(corpus):
    for x in corpus:
        phonetized_sentence = voice.to_phonemes(x)
        yield phonetized_sentence.phonemes_str.strip("_")

phonemes_count = []
with open(CORPUS_PATH, "r") as corpus:
    for x in extract_sentence(corpus):
        phonemes_count.append(len(x))

print(sum(phonemes_count ) / len(phonemes_count))
