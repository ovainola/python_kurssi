# -*- coding: utf-8 -*-
# Ajokomento: python stringit.py
import numpy as np

if __name__ == '__main__':
    # Luodaan pari stringiä
    lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Suspendisse ac justo nunc. Nullam at sapien pharetra,
 molestie purus ac, vehicula tortor. Suspendisse condimentum est nec
 justo fringilla, nec tempus lacus feugiat. Donec id justo massa.
 Sed nisi tortor, convallis a accumsan eu, condimentum vel justo.
 Etiam fringilla ultricies nulla. Aliquam maximus libero vel fringilla
 iaculis. Duis nulla dolor, feugiat non efficitur vel, egestas vel urna.
 In pharetra finibus rutrum. Mauris sit amet nibh ornare, gravida felis vitae,
 lobortis massa"""

    # \n merkillä luodaan rivivaihto. 
    multiline = "Line1-abcdef \nLine2-abc \nLine3-abcd"
    print(multiline)
    
    quote = ("'Oh, you can't help that,' said the Cat: 'we're all mad" +
             " here. I'm mad. You're mad.'")
    
    ##################################################################
    #                   Operaatioita lorem ipsumille                 #
    ##################################################################
    split_lorem = lorem_ipsum.split()
    # u-merkki stringin edessä tarkoittaa, että string on unicode merkistöä
    # näin saadaan ä:t ja ö:t oikein printattua.
    print(u"Yhteensä sanoja: {0}, ja unique sanoja: {1}".
        format(len(split_lorem), len(np.unique(split_lorem))))
    
    # split pisteiden kohdalta
    split_dot = lorem_ipsum.split(".")
    # poistetaan '\n' -rivivaihto merkit
    lauseet = [split_dot[x].replace("\n", "") for x in np.arange(len(split_dot))]
    print(u"Yhteensä lauseita: {0}".format(len(lauseet)))

    # all uppercase and lowercase
    all_upper = lorem_ipsum.upper()
    all_lower = lorem_ipsum.lower()
    
    # Käännetään koko sana väärinpäin
    # slice: aloitetaan -1, seuraavaksi ei ole mitään raja-arvoa, joten jatketaan loppuun asti stepillä -1
    backward_lirum = lorem_ipsum[-1::-1]
    print(backward_lirum)
    
    
    
    
    
 