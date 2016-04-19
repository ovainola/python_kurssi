# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # https://docs.python.org/2/library/exceptions.html

    vals = {}

    # Haetaan arvolle lukuarvo vals dictistä.
    # Jos arvoa ei ole, otetaan virhe kiinni ja asetetaan arvo dictiin
    # Lopuksi haetaan arvo dictistä uudelleen    
    try:
        arvo = vals["test"]
    except KeyError: # Tämä ottaa vain KeyErrorit kiinni
        vals["test"] = 1.0
    finally:
        arvo = vals["test"]
    
    try:
        faillaa = ["eaf"] - [1]
    except: # Tämä ottaa kaikki virheet kiinni
        print("I failed")
        
    
        
    