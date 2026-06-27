
import spacy
from spacy import displacy
import pandas as pd
import numpy as np
import json

with open('AIRE_project/AIRE/vocab.json', 'r') as f:  # change vocab.json to vocab1.json imple
    Vocab = json.load(f)
nlp = spacy.load('en_core_web_md')


def greet(text):
    prompt = nlp(text)
    type_of_greet = ''
    types_of_greets = np.array([x for x in Vocab['greetings'].keys()])
    greets_list = []
    for greet_type in types_of_greets:
        greets_list.extend(Vocab['greetings'][greet_type]['words'])
    greets_list = list(nlp.pipe(greets_list))  # storing each of the word as doc object
    greets_list_vector = np.array([
        prompt.similarity(doc) if doc.has_vector and prompt.has_vector else 0.0 for doc in greets_list
    ])
    response = ''
    for x, y in zip(greets_list, greets_list_vector):
        if max(greets_list_vector) == y:
            word = x.text
            for greet_type in types_of_greets:
                if word in Vocab['greetings'][greet_type]['words']:
                    type_of_greet = greet_type
                    response = Vocab["respons"]["common"][greet_type]
    return {
        "max_similarity_value": float(max(greets_list_vector)),
        "similar_greet_type": str(type_of_greet),
        "response": response
    }
# BASIC_CONV = []
# QUES = []
# for x, y in Vocab.items():
#     if x != 'question':
#         BASIC_CONV.append(x)
#     else:
#         for p, q in Vocab['question'].items():
#             QUES.append(p)
# nlp = spacy.load('en_core_web_md')
# # Placeholder label set - replace with your real Label_BA_x / Label_QA_x etc.
# greets = ['Hi', 'Hello', 'Namasthe']
# print(Vocab.keys())
