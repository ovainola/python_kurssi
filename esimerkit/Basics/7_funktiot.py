# -*- coding: utf-8 -*-
import glob

# Vähän täydellisempi esimerkki docstring:eineen
def print_all_files(folder):
    """Funktio, jolla voi printata kaikki tiedostot halutusta kansiosta
    
    Parameters
    ----------
        folder: string
            Kansio, josta halutaan tutkia kaikki tiedosts
    
    Returns
    -------
        list
            Lista string:ejä, eli tiedosto nimet
    
    Examples
    --------
        >>> file_name = 'C:\\Program Files (x86)\\Windows Media Player'
        >>> print_all_files(file_name)
        ['mpvis.DLL', 'setup_wm.exe', 'wmlaunch.exe', 'wmpconfig.exe',
        'wmplayer.exe', 'WMPMediaSharing.dll', 'wmpnssci.dll', 'WMPNSSUI.dll',
        'wmprph.exe', 'wmpshare.exe']
    """
    # Otetaan lista kaikista tiedostoista/kansiosta kyseisessä polussa
    all_files = glob.glob(folder + "\\*")
    files = []
    # Käydään läpi
    for each in all_files:
        file_name = each.split("\\")[-1]
        # Jos splitattaessa pituus on vielä yksi, on kyseessä kansio
        # muutoin, tiedosto
        if len(file_name.split(".")) != 1:
            files.append(file_name)
    return files

# Keyword esimerkki
def keyword_func(x, y, printtaa=True, operation="multiply"):
    if operation == "multiply":
        val = x * y
    elif operation == "sum":
        val = x + y
    elif operation == "pow":    
        val = x ** y
    else:
        raise Exception("Could not understand operation")
    if printtaa:
        print("value: {0}".format(val))
    return val

# Joskus voi olla tapauksia, jolloin ei voi tietää montako argumenttia
# funktioon tulee. Tällöin voidaan käyttää * -syntaxia.
def only_stars(*args, **kwargs):
    print("\nasterix arguments")
    print(args)
    print("\nasterix kwarguments")
    print(kwargs)
    
if __name__ == '__main__':
    file_name = 'C:\\Program Files (x86)\\Windows Media Player'
    print(print_all_files(file_name))
    
    keyword_func(2,2)
    
    only_stars(1,2,3,4,mm=1,kk=2)
    
    # Lambda funktiosta pari esimerkkiä
    
    lam_1 = lambda x: x ** 2
    lam_2 = lambda x, y: x * y
    
    print("lam 1: {0} ja lam 2: {1}".format(lam_1(1), lam_2(1,2)))
    