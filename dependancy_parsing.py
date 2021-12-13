import spacy
from spacy import displacy


nlp = spacy.load('en_core_web_sm')
doc = nlp("Book me a flight from Bangalore to Goa")
blr, goa = doc[5], doc[7]
print(list(blr.ancestors))
print(list(goa.ancestors))

doc = nlp("Book a table at the restaurant and the taxi to the hotel")
tasks = doc[2], doc[8]
tasks_target = doc[5], doc[11]

for task in tasks_target:
    for tok in task.ancestors:
        if tok in tasks:
            print("Booking of {} belongs to {}".format(tok, task))
    break

print(list(doc[2].children))

displacy.serve(doc, style="dep")