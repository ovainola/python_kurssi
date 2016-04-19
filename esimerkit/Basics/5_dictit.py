# -*- coding: utf-8 -*-

if __name__ == '__main__':
    
    # luodaan dict
    puppe = {"nimi": "puppe",
             "ika": 5,
             "rotu": "koira"}

    karvis = {"nimi": "karvis",
             "ika": 2,
             "rotu": "koira"}

    porro = {"nimi": "pörrö",
             "ika": 3,
             "rotu": "kissa"}

    tassu = {"nimi": "tassu",
             "ika": 9,
             "rotu": "kissa"}
             
    musti = {"nimi": "musti",
             "ika": 16,
             "rotu": "mursu"}
     
                 
    lemmikit = {"kissat": [tassu, porro],
                "koirat": [puppe, karvis],
                "mursut": [musti]}
    
    for each in lemmikit["mursut"]:
        nimi = each["nimi"]
        if nimi == "musti":
            print("mustin rotu on: %s" % each["rotu"])
            each["koko"] = "valtava"
    
    print(lemmikit)