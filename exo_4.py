"""Exo4 """
from utilities import openPkl


def fonc_1(doc_number, dic_ponder):
    """Take the document number and the weighted inversefile and
        returns the list to wighted terms

    Keyword arguments:
    doc_number --   document number
    dic_ponder --   inverse file weighted! {(term,doc):value}  
    
    Returns:
        list of term with their weight{(term,doc_number):occurence}
    """

    # (term, doc)
    term_out = {}
    for i in dic_ponder:
        # get doc number
        if i[1] ==doc_number:
            term_out[i[0]] = dic_ponder[i]

    return term_out


def fonc_2(terme, dic_ponder,n):
    """Return list de documents et les poinds de ce terme dans chaque document

    Keyword arguments:
    n -- number of documents


    Returns:
        {doc_number: term weight} 

    """

    term_out = {}
    for i in range(1,n+1):
        term_out[i] = dic_ponder[(terme,i)]

    return term_out


def main():
    # get inverse file ponderer
    dic_ponder = openPkl("dic_ponder.pkl","")
    f1 = fonc_1(1,dic_ponder)
    print("fonc1 :\n",f1)
    f2 = fonc_2("paris",dic_ponder,3)
    print("fonc2:\n", f2)

if __name__=='__main__':
    main()