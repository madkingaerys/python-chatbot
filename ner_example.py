import spacy

my_string = "Google has its headquarters in Mountain View, California having revenue amounted to 109.65 billion US " \
            "Dollars"

nlp = spacy.load('en_core_web_sm')
doc = nlp(my_string)

for ent in doc.ents:
    print(ent.text, ent.label_)

my_string = "Mark Zuckerberg born May 14, 1984 in New York is an American technology entrepreneur and philanthropist " \
            "best known for co-founding and leading Facebook and its chairman and CEO"

doc = nlp(my_string)

for ent in doc.ents:
    print(ent.text, ent.label_)

my_string = "I usually wake up at 9:00 AM. 90% of my daytime goes in learning new things."
doc = nlp(my_string)

for ent in doc.ents:
    print(ent.text, ent.label_)

# Similar words example
print("\n")
my_string1 = "Imagine Dragons are the best band."
my_string2 = "Imagine dragons come and take over the city."

doc1 = nlp(my_string1)
doc2 = nlp(my_string2)

for ent in doc1.ents:
    print(ent.text, ent.label_)

for ent in doc2.ents:
    print(ent.text, ent.label_)