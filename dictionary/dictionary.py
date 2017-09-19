dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]
hun_word = ""
eng_word = ""

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'

def add_word(hun_word, eng_word): 

    dict_item={}
    dict_item[hun_word] = eng_word
    dictionary.append(dict_item)
    #while hun_word != "" and eng_word != "":
    #    count += 1
    return(dictionary)

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    pass


def translate_to_eng(hun_word):
    pass

add_word("csinal", "make")