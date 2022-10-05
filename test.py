import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = "Đường rộng thênh thang bước chân em đi về đâu"
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)