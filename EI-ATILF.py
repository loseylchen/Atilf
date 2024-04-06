#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:50:06 2024

@author: flora


pour récupérer les expresssions idiomatiques qu'il y a dans le dictionnaire français/portuguais de l'ATILF année 2012 environ
Pour LIAN

"""

# librairie pour parser les XML
from lxml import etree

# on ouvre un fichier en lecture
infile = open("fp.xml", "r")
# on ouvre un fichier en écriture
outfile = open("fp.csv", "w")

# on utilise la librairie pour lire le fichier xml et pouvoir requeter directement sur les balises
tree = etree.parse(infile)

outfile.write("entrees idiomatiques ATILF\tsynonymes\n")

# je vais chercher toutes les balises nommées "entry" sans me soucier de son chemin depuis la racine
# correspond au final au chemin TEI/text/body/entry
for entry in tree.findall("//entry"):
    #on parcourt toutes les formes orthographiques
    form = entry.findall("form/orth")
    for orth in form:
        # on récupère le texte sous la balise
        idiom = orth.text
        # on l'écrit dans le fichier
        outfile.write(idiom+"\t")
    # on met à chaine de caractère vide les synonymes
    synonymes = ""
    # on va aller repécher aussi les synonymes
    for syn in entry.findall("sense/xr"):
    #     # on vérifie que c'est bien un synonyme
    #     # je récupère l'attribut
       attriType = syn.get("type")
       if attriType == "syn":
           for ref in syn.findall("ref"):
               synonymes += ref.text+" - "
    outfile.write(synonymes.strip(" - "))
    # on saute une ligne après chaque entrée
    outfile.write('\n')    
    
outfile.close()
    
    
