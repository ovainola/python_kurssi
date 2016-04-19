import os
"""
Esimerkki elävästä elämästä

Juhliin oltiin tekemässä tietovisaa openshot -ohjelmalla. Kuitenkin, kone
kaatui kesken työteon ja korruptoi Tietovisa.osp tiedostoa, ettei sitä
enää saanut auki kyseisellä tietokoneella. Tiedosto siirrettiin kirjoittajan
koneelle. Kun tiedostoa yritettiin avata, virheilmoitus kertoi,
että haluttuja video polkuja ei enää ollut olemassa. Kun Tietovisa.osp
tiedoston avaa (esim. notepad / gedit), voi löytää polkuja, jotka
alkavat /home/olli/... . Koska alkuperäiset videot oli ripoteltu pitkin tieto-
koneen levyä, kerättiin kaikki videot yhteen kansioon ja pythonilla vain 
muutettiin Tietovisa.osp tiedostosta polut oikeaan osoitteeseen.

Tämä esimerkki toimii vain unix koneessa (linux). Jos haluaa muuttaa windows
muotoon, pitää '/' merkki muuttaa '\\' merkiksi
"""

if __name__ == '__main__':
    # Tietovisaa tehdessä kuvat oli sijoitettu samaan kansioon
    # kuin missä esit_tietovisa_paths.py ja Tietovisa.osp olivat
    # Napataan siis ajokansio
    path = os.getcwd() 
    
    # Avataan tiedosto ja luetaan rivit muistiin
    with open("Tietovisa.osp", "r") as f:
        lines = f.readlines()
    
    # Avataan uusi tiedosto, jonne kirjoitetaan uudet polut
    with open("new_tietovisa.osp", "w") as g:
        
        # Luetaan polut
        for line in lines:
            # Jos polku sisältää /home/olli
            if "/home/olli/" in line:
                # Splitataan, ja otetaan viimeinen alkio, joka on tässä
                # tapauksessa tiedosto nimi
                file_ = line.split("/")[-1]
                
                # kirjoitetaan uusi polku, joka mätsää alkuperäiseen paitsi polku
                line = "S'" + path + "/" + file_
            
            # Kirjoitetaan polku uuteen tiedostoon
            g.write(line)
