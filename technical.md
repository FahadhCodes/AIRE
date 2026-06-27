# BA intelligence

| **Actor**             | **Chatbot should ask**                           |
| :-------------------- | :----------------------------------------------- |
| **Actor**             | "Who is performing this action?"                 |
| **Action detail**     | "Can you describe exactly how this should work?" |
| **Expected result**   | "What should happen after this action?"          |
| **Failure condition** | "What should happen if this fails?"              |
| **Business reason**   | "Why is this needed?"                            |

---

**26/06/2026 - Log**

---

- Created `vocab.json`,`vocab.py` files to handle language logic

  ### `vocab.py`,`vocab.json`

  ```Python
  with open('AIRE_project/AIRE/vocab.json', 'r') as f:
    file = json.load(f)
    BASIC_CONV = [] # Keys of Basic conversation [Hi,Hello...]
    QUES = [] # Keys of question parameters[1,2,3...]
    for x, y in file.items():
        if x != 'question':
            BASIC_CONV.append(x)
        else:
            for p, q in file['question'].items():
                QUES.append(p)
    nlp = spacy.load('en_core_web_md')
  ```

  **Note :**

  > This Script took the keys of Basic conversation strings, question keys from `vocab.json` and store it inside `BASIC_CONV `, `QUES`

  > from today I am going to use `vocab.json` as container of vocabulary parameters in `JSON` formate.

---

**27/06/2026 - Log**

---

- Created more efficiant `JSON` thath can response to greetings
- Struncture of JSON:

  ```JSON
  {
  "greetings": {
    "short_simple": {
      "category": "Short & Simple (1-2 words)",
      "words": []
    },
    "casual_slang": {
      "category": "Casual & Slang",
      "words": []
    },
    "time_based": {
      "category": "Time-Based Greetings",
      "words": []
    },
    "polite_formal": {
      "category": "Polite & Formal",
      "words": []
    },
    "indian_regional": {
      "category": "Indian & Regional Greetings",
      "words": []
    },
    "warm_friendly": {
      "category": "Warm & Friendly",
      "words": []
    },
    "checking_in": {
      "category": "Checking In (Beyond Just Hello)",
      "words": []
    },
    "international": {
      "category": "One-Word International Greetings",
      "words": []
    }
  },
  "respons": {
    "common": {
      "short_simple": "",
      "casual_slang": "",
      "time_based": "",
      "polite_formal": "",
      "indian_regional": "",
      "warm_friendly": "",
      "checking_in": "",
      "international": ""
    },
    "question": {
      "1": "",
      "2": "",
      "3": "",
      "4": "",
      "5": ""
    }
  }
  }

  ```

- Introduced new function `greet()` in `vocab.py` its return
  - **max_similarity_value** : With `.similarity(doc)` build in function of `spaCy` used to find the similarity of the prompt
  - **similar_greet_type** : Selecting the most suitable type of greeting type
  - **response** : Selecting the response
- Modified `CSS` for assign specific yellow color to the bubble of chat

| chack Box | Description                                                                                                                                      |
| :-------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [x] l     | Instead of list of words ex:- `['Hi', 'Hello', 'Namasthe']` generating `spacy` synonims so that's can more intelligence                          |
| [ ] l     | Like the `greet()` function, introducing new functionality that select suitable question response once the Bot detect the lacks in requirenments |
| [ ] l     | Still trying yo implement the forms and labeled text box for collect information more pricisely.                                                 |
