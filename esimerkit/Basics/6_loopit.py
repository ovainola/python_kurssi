# -*- coding: utf-8 -*-
import numpy as np
import time


if __name__ == '__main__':
    ################################################################
    #    Esim. 1
    # Luodaan random lista, nostetaan kolmanteen potenssiin ja summataan alkiot
    ################################################################

    # luodaan 100 mittainen lista, joka sisältää random numeroita välillä 0 - 1
    vals = np.random.rand(100)

    summa_ja_pow = 0    
    for each in vals:
        summa_ja_pow += each ** 3
    
    print("Summa ja pow: {0:.3f}".format(summa_ja_pow))
    
    ################################################################
    # Esim. 2
    # 
    # While loop esimerkki. Loop jatkuu, kunnes 5 sekuntia on kulunut
    ################################################################
    
    is_true = True
    start = time.time()
    while is_true:
        if time.time() - start > 5:
            is_true = False
            print("Ready !")
        else:
            print("Not ready, sleeping")
            time.sleep(0.5)
                