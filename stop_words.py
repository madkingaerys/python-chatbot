from spacy.lang.en.stop_words import STOP_WORDS
import spacy


nlp = spacy.load('en_core_web_sm')
# print(STOP_WORDS)

print(nlp.vocab["is"].is_stop)
print(nlp.vocab["hello"].is_stop)
print(nlp.vocab["with"].is_stop)
