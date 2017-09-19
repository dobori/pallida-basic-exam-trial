dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]
hun_word = ""
eng_word = ""
dict_item={}

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'

def add_word(hun_word, eng_word): 
    dict_item[hun_word] = eng_word
    dictionary.append(dict_item)
    return(dictionary)

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'

# def translate_to_hun(eng_word): 
#     value=""
#     for i in dictionary:
#         for value in dict_item:
#             if eng_word == value:
#                 hun_word = value[eng_word]
#                 print(hun)      

def translate_to_eng(hun_word):
    value=""
    for i in dictionary:
        for value in dict_item:
            if hun_word == value:
                eng = value[eng_word]
            print(eng)  

add_word("csinal", "make")
#translate_to_hun("apple")
translate_to_eng("alma")