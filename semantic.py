import spacy


def nlp_experiements():
    word1 = nlp("cat")
    word2 = nlp("monkey")
    word3 = nlp("banana")
    print(word1.similarity(word2))
    print(word3.similarity(word2))
    print(word3.similarity(word1))

    tokens = nlp('cat apple monkey banana ')
    for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

    sentence_to_compare = "Why is my cat on the car"
    sentences = ["where did my dog go",
                "Hello, there is my car",
                "I\'ve lost my car in my car",
                "I\'d like my boat back",
                "I will name my dog Diana"]
    model_sentence = nlp(sentence_to_compare)
    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ", similarity)


#Run the experiments with 2 different language models
nlp = spacy.load('en_core_web_md')
nlp_experiements()

print(""" 


OTHER MODEL


""")

nlp = spacy.load('en_core_web_sm')
nlp_experiements()


# There are significant differences between the similarity results of the two models. For example the monkey-banana similarity is less than monkey-apple similarity 
# in the second model whereas the first model is able to grasp the relationship between monkeys and bananas that humans understand, which is that monkeys are 
# known to eat bananas.