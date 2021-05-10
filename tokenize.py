##Tokenizing Words and Sentences with NLTK

#nltk package is imported
from nltk.tokenize import sent_tokenize, word_tokenize

#create an example sentence
example_syntacticUnit = "Hi, I am Khosiyat. And I am writing this text to show you how nltk can tokenize it. Never stop coding!"
#tokenize the sentence
tokened_words=sent_tokenize(example_syntacticUnit)
#print the result
print(tokened_words)
