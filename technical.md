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

- next plans
  - Instead of list of words ex:- `['Hi', 'Hello', 'Namasthe']` generating `spacy` synonims so that's can more intelligence
  - Generating forms and textbox with labeles inside chatbot based in defects in the providing requirement so clients directly provide our needed informations so later we do not need to extract the information from raw texts
