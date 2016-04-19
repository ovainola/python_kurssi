# -*- coding: utf-8 -*-
"""
Ongelma:
Meillä on testeistä saatua mittausdataa x, y pistepareina.
Mittausdatassa on y-akselilla glugoosin konsentraatio ja x-akselilla
absorbanssi. Miellä on nyt mielenkiintoja tutkia, jos annetaan jokin 
glokoosi konsentraatio, mikä on absorbanssi. Tutkittavaksi riittää, kun
luodaan annetulle pistejoukolle palafunktio, joka yhdistää pisteet
"""

import numpy as np
import matplotlib.pyplot as plt

def piecewice_function(y, func_bools, func_values):
    """Piecewise funktio. Funktio palauttaa x-arvon annetulle y-arvolle
    """
    for each in np.arange(len(func_bools)):
        if func_bools[each](y):
            return func_values[each](y)
    raise Exception("No suitable interval!")





def within_interval(y, y_upper, y_lower):
    """ Boolean funktio, jolla tarkistetaan onko y annetulla välillä
    """
    return True if y < y_upper and y >= y_lower else False

def interval_factory(y_upper, y_lower):
    """Factory funktio
    """
    return lambda y: within_interval(y, y_upper, y_lower)





def line_function(y, a, k):
    """Suoran yhtälö x = (y - a) / k
    """
    return (y - a) / k
    
def line_factory(a, k):
    """Factory funktio
    """
    return lambda y: line_function(y, a, k)





def create_piecewise_function(x_values, y_values):
    """Funktio luo piecewise funktion annetulle x-y pistejoukolle
    """
    # Tyhjät listat.
    # Boolean listaan tulee lambda funktiot, joilla määritellään tietty
    # intervalli. Value listaan tulee lambda funktiot, jolla määritellään
    # intervallin x-arvot
    boolean_functions = []
    value_functions = []
    for idx in np.arange(1, len(x_values)): # Käydään läpi
        x_lower = x_values[idx - 1]
        x_upper = x_values[idx]
        y_lower = y_values[idx - 1]
        y_upper = y_values[idx]
        k = (y_upper - y_lower) / (x_upper - x_lower) # Lasketaa kulmakerroin
        a = y_lower - k * x_lower # lasketaan skalaari, yhtälöstä: y = kx + a
        # listätään lambda funktiot listaan
        # Nyt tulee käyttää factory funktioita, jotta scope menee oikein
        boolean_functions.append(interval_factory(y_upper, y_lower)) 
        value_functions.append(line_factory(a, k))
    return lambda y: piecewice_function(y, boolean_functions, value_functions)

if __name__ == '__main__':
    
    # Mittausdata
    x_values = np.array([0.0, 1.0, 1.67, 2.5, 3.33])
    y_values = np.array([0.0, 0.325056, 0.464073, 0.51712, 0.761402])
    
    # Luodaan piecewise funktio
    pala_functio = create_piecewise_function(x_values, y_values)
    
    # Lasketaan testipisteet
    y_test = np.linspace(0, 0.7, 50)
    x_test = map(lambda x: pala_functio(x), y_test)
    
    # plottaillaan alkuperäiset pisteet
    plt.plot(x_values, y_values)
    plt.scatter(x_values, y_values)
    
    # Plottaillaan testipisteet
    plt.scatter(x_test, y_test)
    plt.show()
    
    ###########################
    # Vaihtoehtoinen ratkaisu
    # Käytetään numpyn lineaarista interpolointi funktiota
    # Tämä kuitenkin toimii toisinpäin, eli f(x) = k*x + a
    ###########################
    
    inter_func = lambda x: np.interp(x, x_values, y_values)
    y_interp = map(lambda x: inter_func(x), x_test)  
    plt.scatter(x_test, y_interp)
    plt.show()    
