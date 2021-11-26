"""Fichier envoyé par la prof de tp."""

# ouverture du fichier stopwords_fr
stopwordsfile = "files/stopwords_fr.txt"
# Récupération de la liste des mots vides
stopwords_list = open(stopwordsfile, "r", encoding="utf-8").read().splitlines()

ponctuation_list = ['?', '.', '!', '<', '>', '}', '{', ':', '(', ')', '[', ']', '\"', ',', '-', "»", "«", '\'', '’',
                    '#', '+', '_', '-', '*', '/', '=']



def stopword_elimination(text):
    """Eliminer les mots vides et la ponctuation."""

    word_list = []
    # Eliminer la punctuation
    for character in ponctuation_list:
        text = text.replace(character, ' ')

    # str -> list
    words = text.split()
    for word in words:
        if word.lower() not in stopwords_list:
            word_list.append(word.lower())
    return word_list


def dict_freq(word_list):
    """Create dict of frequecey for word_list"""
    frequence_dict = {}
    for word in word_list:
        if word not in frequence_dict:
            frequence_dict[word] = word_list.count(word)
    return frequence_dict


def all_freq(n,path="files"):  # n est le nombre des documents txt
    """Get the ffrequences of words in every document.
    
    Keyword arguments:
    n  --    number of documents
    path -- path to the documents

    Returns:
        dictionnary with this format: {document_number:{word:frequencey}}
    """

    i = 1
    frequences = {}
    while (i <= n):
        with open(path+'/D' + str(i) + '.txt', 'r', encoding='utf-8') as file:
            lines = file.read()
            data = stopword_elimination(lines)
            frequences[i] = dict_freq(data)

        print("D"+str(i), ":", frequences[i])
        print("-------------------------------\n"*3)
        i = i + 1
    return frequences


def create_inverse_file(frequences):
    """create inverse file.

    Keyword arguments:
    frequences --  dictionary that contains the frequences of words for
                    every document {doc_number:{word:freq,word2:freq2,..},doc_number2:{word:freq,..}} .

    Returns:
        the inverse file format: {(term,doc_number):occurence}
    """
    inverse_file = {}
    for i in frequences:
        for word in frequences[i]:
            #check if exists
            if (word,i) not in inverse_file:
                inverse_file[(word,i)] = frequences[i][word]
            else:
                print("there is a problem somewhere!")
    # TODO: optimiser !
    # ajouter les mot de frequence 0:
    for doc in frequences:
        for word in frequences[doc]:
            if (word,i) not in inverse_file:
                # sinon creer et mettre a 0
                inverse_file[(word,i)] = 0
            

    return inverse_file

def main():
    # Création des dictionnaires ( pour 4 documents )
    frequences = all_freq(3)
    inverse_file= create_inverse_file(frequences)
    # save inverse file
    with open ("inversefile","w",encoding="utf-8") as file:
        file.write(str(inverse_file))
    
    print("\n\n Inverse File:\n\n")
    print(inverse_file)

if __name__=='__main__':
    main()