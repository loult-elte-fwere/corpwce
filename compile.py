import os

RESSOURCES_DIR = "/home/kaoro/Documents/vocal_synthesis/mboshi-french-parallel-corpus/full_corpus_newsplit/all/"

paths = os.listdir(RESSOURCES_DIR)

with open('french_corpus.txt', 'a') as corpus:
    for path in paths:
        if path.endswith(".fr"):
            with open(RESSOURCES_DIR + path, 'r') as sentence:
                corpus.write(sentence.read())
                
                
        
