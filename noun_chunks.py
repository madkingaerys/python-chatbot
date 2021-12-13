import spacy


nlp = spacy.load('en_core_web_sm')
doc = nlp("Boston Dynamics is gearing up to produce thousands of robot dogs")
print(list(doc.noun_chunks))

doc = nlp("Deep learning cracks the code of messenger RNAs and protein-coding potential")
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)

doc = nlp("How are you doing today?")
for token in doc:
    print(token.text, token.vector[:5])

hello_doc = nlp("hello")
hi_doc = nlp("hi")
hella_doc = nlp("hella")
print(hello_doc.similarity(hi_doc))
print(hello_doc.similarity(hella_doc))

got_1 = nlp("When will next season of Game of Thrones be releasing?")
got_2 = nlp("Game of Thrones next season release date?")

print(got_1.similarity(got_2))

example_doc = nlp("car truck google")

for t1 in example_doc:
    for t2 in example_doc:
        similarity_perc = int(t1.similarity(t2) * 100)
        print("Word {} is {}% similar to word {}".format(t1.text, similarity_perc, t2.text))