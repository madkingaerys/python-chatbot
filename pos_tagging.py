import spacy

nlp = spacy.load('en_core_web_sm') # Loads the spacy en model into a python object
doc = nlp('I am learning how to build chatbots') # Creates a doc object
for token in doc:
    print(token.text, token.pos_) # prints the text and pos tags

print('\n')

doc = nlp('I am going to London next week for a meeting')
for token in doc:
    print(token.text, token.pos_)

print('\n')

doc = nlp('Google release "Move Mirror" AI experiment that matches your pose from 80,000 images')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

print('\n')

doc = nlp('I am learning how to build chatbots')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)