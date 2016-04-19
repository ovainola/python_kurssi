# -*- coding: utf-8 -*-
# Ajokomento esim. python system_arguments 6112 maukka
import sys

if __name__ == '__main__':
    
    sys_args = sys.argv
    print(sys_args)
    if len(sys_args) < 3 or len(sys_args) > 3:
        raise Exception("tarkista argumenttien maara")
    python_file = sys_args[0]
    other_args = sys_args[1:]
    len_args = len(other_args)
    print("Ajetun python tiedoston nimi: {0}".format(python_file))
    print(u"Muita argumentteja on yhteensä: {0}".format(len_args))
    
    # system arguments ovat stringejä, kun ne tulevat sisään
    # muutetaan numero int komennolla
    try:        
        numero = int(other_args[0])
    except ValueError:
        raise ValueError("eka argumentti ei ollut numero")
    nimi = other_args[1]
    
    print("numero: {0} ja nimi {1}".format(numero, nimi))
    
    user_input = raw_input("Kirjoita jotain: ")
    print("kirjoitit %s" % user_input)
    
