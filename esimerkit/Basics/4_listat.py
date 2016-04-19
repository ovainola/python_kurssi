# -*- coding: utf-8 -*-
import copy
import base64
    
if __name__ == '__main__':
    ################################################################
    #    Esim. 1
    # Ekassa esimerkissä käydään kaksi listaa läpi,
    # kerrotaan niiden alkiot keskenään ja otetaan summa
    ################################################################

    # Luodaan pari listaa
    nums_1 = [3,6,3,7,8,5,7,2,6,3,1,6]
    nums_2 = [34,16,45,3,99,5,-1,42,24.,5,.1,2.6]
    
    # voisi myös tehdä näin: print(len(nums_1), len(nums_2))
    print(map(len, [nums_1, nums_2]))
    
    # lista tuleville arvoille
    vals = []
    
    for each_1, each_2 in zip(nums_1, nums_2):
        arvo = each_1 * each_2 
        vals.append(arvo)
    
    summa = sum(vals)
    
    print("Yhteistulos: {0}".format(summa))
    
    ################################################################
    #    Esim. 2
    # Filteröidään listasta kaikki 1:stä pienemmät arvot pois
    ################################################################
    
    # luodaan jokin lista
    values = [43, -36, 29, -36, 17, 8, 49, 0, 23, -2, -4, -18, -12, 35, 14]
    # Kopioidaan esimerkin loppua varten
    values_copy = copy.copy(values)
    # delete indexi lista    
    delete_idx = []
    
    for idx, each in enumerate(values):
        if each <= 0:
            delete_idx.append(idx)
    
    # Lista loopattu läpi ja kaikki nollaa pienemmän luvut haettu.
    # Nyt kun poistetaan listasta kaikki halutut arvot, tulee 
    # delete_idx lista loopata väärin päin. Muuten indeksi ja arvot eivät mätsää
    for del_idx in delete_idx[-1::-1]:
        del values[del_idx]
    
    print("Vain positiiviset arvot: {0}".format(values))
    
    # Tietenkin, korkeamman asteen funktiolla homman voisi tehdä yhdellä rivillä
    filtered_arvot = filter(lambda x: x > 0, values_copy)
    print("filtered arvot:          {0}".format(filtered_arvot))

    ################################################################
    #    Esim. 3
    # Olet salainen agentti ja olet juuri saanut käsiisi 74 vihollisvaltion
    # salasanaa. Valitettavasti vain yksi salasanoista toimii mutta olet
    # saanut vinkin, että kyseisessä salasanassa lisältää "key_" -sana.
    # Olet myös saanut selville, että onneton viholliskoodari ei ole muistanut
    # hashata ollenkaan salasanoja, vaan pelkästään base64:llä enkoodannut.
    # Sinun täytyy kääntää stringit takaisin luettavaksi ja etsiä oikea salasana
    ################################################################


    
    keys = ['J0xvcmVtTJE\\BMZdCKJhBMmE',
 'aXBzdW0=T\\HWPlhFa^DCbifI',
 'ZG9sb3I=mJGH`ggLmDQQAYfH',
 'c2l0TGcf\\aVbQROFPP\\EIbEQ',
 'YW1ldCw=TO]hP]bEBlF_EmMG',
 'Y29uc2VjdGV0dXI=[mIFNcfC',
 'YWRpcGlzY2luZw==NhlTDeAU',
 'ZWxpdC4=KdNZ\\\\iUX_mCLFFR',
 'VmVzdGlidWx1bQ==kVYaRFFE',
 'bm9uCkVcPB_aceZfPdBLN]Ul',
 'bmVxdWU=^OQUCgcXZdQ_mSKV',
 'c2NlbGVyaXNxdWUsSlilQ]id',
 'dGluY2lkdW50WIJalOmUJRPS',
 'bWk=KfQPglm\\h_`D`Q]Ybd[M',
 'ZXQsEG]WBeORCGT_fjVdOIgL',
 'cHU=NbZXIZhCDQNcAPV\\ZNLl',
 'bHZpbmFyaJ_O_fBYUmiPDfGO',
 'bmliaC4=^ihRkCMJTd]BENMQ',
 'U3VzcGVuZGlzc2U=JAeZfWSR',
 'cGxhY2VyYXQ=LZlcRKPZaFSK',
 'YXVndWU=PaPjh\\fGRckWghaT',
 'dml0YWU=XjeHhPbQEdLOWYSG',
 'bGVjdHVzHP[^D`[bAGFAgGki',
 'dHJpc3RpcXVl`QdSgLY_VLGU',
 'bHVjdHVzLg==HAHQfLkS_Gcf',
 'VmVzdGlidWx1bQ==bVIkNGFO',
 'YW50ZQ==YlHNGKB^MjiBlVJ[',
 'aXBzdW0=PJQVSPh_ZHFgBPhe',
 'cHJpbWlzFGHCS\\HYcYC\\QX`[',
 'aW4=FkfaQAfejYTDNmdNCE^R',
 'ZmF1Y2lidXM=MeEdm`mB]]WW',
 'b3JjaQ==aQJeOdfhJbYa^OLI',
 'bHVjhb\\MSTgeSGjYeb\\mS]RA',
 'dHVzTlhP]^IG`W]HgiPbBbKI',
 'ZXQ=jYIIYMImdZFX\\ZWSCMMa',
 'dWx0cmljZXM=UUQUXWcaibK[',
 'cG9zdWVyZQ==GTHiOP`ffgZD',
 'Y3ViaWxpYQ==[fZRBa]FOd\\R',
 'Q3VyYWU7XeZMTlEObhPBMK`i',
 'TWFlY2VuYXM=MW\\B_f_HVGgB',
 'bWFsZXN1YWRhCeaHC^]LAE^C',
 'cGxhY2VyYXQ=YkmFBNmffAIf',
 'c2NlbGVyaXNxdWUuia`NBZfH',
 'U3VzcGVuZGlzc2U=WEGA_jlm',
 'bm9uG^IEHdeEiiDlJZECLTm^',
 'dm9sdXRwYXQ=gddDDSHJ\\Njj',
 'ZW5pbSw=`bG^QbXcKLVAZb^U',
 'YWM=iA[eXgND`hGh`]]TIYmR',
 'bHVjdHVzSafSSL`PaN^UIPBK',
 'bmliaC4=TLRJIV\\Ac[eiLkKh',
 'Q2xhc3M=TYSjeWfZLNUNRKfL',
 'YXB0ZW50QWLSN]EJQUY]fObU',
 'dGFjaXRpFfkJ[ZdcdPYDeaRi',
 'c29jaW9zcXU=TChORSGkXWbm',
 'YWQ=_a]DBJNWdOI_[MGDZZ`b',
 'bGl0b3JhdG9ycXVlbnQ=`NM[',
 'a2V5X3RvX2xpZmVfaXNfNDI=',
 'Y29udWJpYQ==GUQTVhVkZi]D',
 'bm9zdHJhLA==BFdbYYNQFaTE',
 'cGVygFMcQICUh^ZODfSWRSmP',
 'aW5jZXB0b3M=QZ]M`cLJaY`Z',
 'aGltZW5hZW9zLg==BK^QS\\Nf',
 'Vml2YW11cw==FV]KfH[JWjVa',
 'ZXVpc21vZA==hgY`cd`bHGfR',
 'ZWdldA==]IEDFEk\\[ecEjOfA',
 'YQ==h_dLAXGUV\\M\\\\jdbReKB',
 'cmN1DFfTkTGgZeeHLGj]aQhH',
 'dmVsgHBYEXHNFFVIJdXfONPO',
 'cGxhY2VyYXQudkUG_DJXATBZ',
 'TnVuYw==GHUiWk_DR^Ade[Ag',
 'dWx0cmljaWVzUejF]abcBbGX',
 'Y29tbW9kbw==bYCDAJC`MCNB',
 'ZGlhbSw=jE^YQfKcBMVGcBc\\',
 'ZWdldA==XfY^kD^DFJXXB]GZ',
 'aGVuZHJlcml0b2Rpbw==_LAT',
 'bW9sZXN0aWU=JTmX[^jeMNJS',
 'dXQuJw==jNWLDfM\\[^`afGH]']
 
    for each in keys:
        try:
            word = base64.b64decode(each)
            if "key_" in word:
                print("salasana loytynyt")
                print(word)
        except TypeError:
            pass
         