import json
import spacy
with open('AIRE_project/AIRE/vocab.json', 'r') as f:
    Vocab = json.load(f)
BASIC_CONV = []
QUES = []
for x, y in Vocab.items():
    if x != 'question':
        BASIC_CONV.append(x)
    else:
        for p, q in Vocab['question'].items():
            QUES.append(p)
nlp = spacy.load('en_core_web_md')
print(BASIC_CONV)
print(QUES)
# Placeholder label set - replace with your real Label_BA_x / Label_QA_x etc.
DUMMY_LABELS = ["1", "2", "3", "4", "5"]
greets = ['Hi', 'Hello', 'Namasthe']
