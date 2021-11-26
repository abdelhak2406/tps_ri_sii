"""Exo3"""
# TODO:add new ddirectory to save outputed files
from exo_2 import get_documents
from utilities import openPkl,savePkl
from math import log10


def get_all_terms(inverse_file):
    """Get all the terms of the inverse_file"""
    all_terms = set()
    for i in inverse_file:
        all_terms.add(i[0])

    return all_terms


def create_dic_pond(inverse_file,n):
    """Create ponderated dictionnary
    
    Keyword arguments:
    inverse_file -- the inverse file! 
    n   -- number off documents

    Returns:
        the ponderated dict format: {term:value}
    """
    dic_pond = {}
    #import pdb; pdb.set_trace()
    for i in inverse_file:

        #calculer poid
        freq = inverse_file[i] 
        max_f = max_freq(i[1],inverse_file)
        ni = len(get_documents(i[0], inverse_file))#number off doc contenant 
        poid =  freq / max_f * log10( (n/ni) + 1 ) 
        dic_pond[i] = poid

        # check if exists in the dic?
    return dic_pond


def max_freq(docu_num,inverse_file):
    """Max frequency in docu_num"""
    max = 0
    for i in inverse_file:
        # get the i'th doc
        if i[1] ==docu_num:
            if inverse_file[i]> max:
                max = inverse_file[i]
    return max


def main():
    inverse_file = openPkl("inverse_file.pkl","")
    # freq = inverse_file[(term,doc)] 
    a = max_freq(1,inverse_file)
    b = get_all_terms(inverse_file)
    dic_pond = create_dic_pond(inverse_file,3)

    with open ("dic_ponder","w",encoding="utf-8") as file:
        file.write(str(dic_pond))

    savePkl(dic_pond,"dic_ponder.pkl","") 
    print(dic_pond)


if __name__=='__main__':
    main()