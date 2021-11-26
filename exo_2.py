"""Exo2 serie 1 RI"""
from utilities import openPkl


def get_term(doc_number, inverse_file):
    """
    Retourne la liste des termes avec leurs fréquences dans ce document.
    """
    terme_freq={}
    for i in inverse_file:
        # (term, docum_num)
        if ( i[1] == doc_number ):
            terme_freq[i[0]] = inverse_file[i]

    return terme_freq


def get_documents(terme, inverse_file):
    """Get the documents that have the term

    Returns:
        dict of this form :{"doc num_doc": number of occurences}, ex: {'doc 2': 1}
    """

    term_freq={}
    for i in inverse_file:
        # (term, docum_num)
        if ( i[0]==terme and inverse_file[i]!=0  )  :
            term_freq[ "doc "+str(i[1]) ] = inverse_file[i]

    return term_freq


def main():
    inverse_file = openPkl("inverse_file.pkl","")
    res = get_term(1,inverse_file)
    lis_doc = get_documents("paris",inverse_file)
    print(lis_doc)
    #print(res)



if __name__=='__main__':
    main()