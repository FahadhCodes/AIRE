import json
with open('AIRE_project/tests/vocab.json', 'r') as f:
    file = json.load(f)
print(file.get('hello'))
greets = ['Hi', 'Hello', 'Namasthe']
doc = "Hi how can I help you".split()
print(True in [greet.lower() in [x.lower() for x in doc] for greet in greets])
