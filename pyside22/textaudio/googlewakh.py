from GoogleTTS import GoogleTTS
txt='Moi djibril Thiongane je suis la.'
txt="""
Le fer est l'élément chimique de numéro atomique 26, de symbole Fe.
Le corps simple est le métal et le matériau ferromagnétique le plus 
courant dans la vie quotidienne, le plus souvent sous forme d'alliages divers.
 Le fer pur est un métal de transition ductile, mais l'adjonction de très faibles 
 quantités d'éléments additionels modifie considérablement ses propriétés mécaniques.
  Allié au carbone et avec d'autres éléments d'additions il forme les aciers,
   dont la sensibilité aux traitements thermomécaniques permet de diversifier
    encore plus les propriétés du matériau. 

"""

def google_wakh(txt,lang,genre,filename,ds):
    tts = GoogleTTS()
    # print(dir(tts.tts))
    tts.set_language_code(lang)
    tts.set_ssml_gender(genre)
    print('debut ... '+ds+'/'+ filename+'.mp3')
    ret = tts.tts(txt,ds+'/'+ filename+'.mp3')
    print("fin ...")
    if 'audioContent' in ret:
        b64 = ret['audioContent']
        print(b64)
        import os
        os.system(f"vlc {filename}.mp3")
    else:
        error = ret['error']
        code = error['code']
        message = error['message']
        status = error['status']
        print(error,code,message,status)
    try:
        pass
    except :
        pass
    


import nltk
from nltk import tokenize
nltk.download('punkt')


def decoupe(ch,n):

    p=print
    lg=len(ch.strip())

    data=[]
    part=''
    nmax=lg//n
    pd=tokenize.sent_tokenize(ch)
    p(pd)
    p('long = ',lg,' max = ',nmax,'pd = ',len(pd))
    # for i in range(0,lg,nmax):
    #     p(ch[i:i+nmax])
    #     data.append(ch[i:i+nmax])
    
    p('long = ',lg,' max = ',nmax,' long data=',len(data))
    return pd


c="je suis la un monde de fou. fatigue de vivre et de respirer "
ch="""Le Sénégal est positionné par 14° de latitude Nord et 14° de longitude Ouest. Son territoire, plus précisément, est compris entre 12°8 et 16°41 de latitude nord et 11°21 et 17°32 de longitude Ouest.

S’étendant sur une surface de 196 712 km23, le Sénégal dispose d'une importante façade maritime, à l'ouest, avec l'océan Atlantique (530 km de côtes)4. Le fleuve Sénégal constitue, au nord et au nord-est, une frontière avec la Mauritanie tandis qu'à l'est-sud-est il constitue une frontière avec le Mali. Au sud-est, la frontière avec la Guinée est traversée par les contreforts de la montagne du Fouta-Djalon, et celle avec la Guinée-Bissau, au sud-sud-ouest, est traversée par une forêt tropicale. Au sud, la Gambie forme une enclave et sépare la région de la Casamance du reste du pays. À l'ouest, la presqu'île du Cap-Vert constitue la partie la plus occidentale du pays et de toute l’Afrique continentale.

Le Sénégal partage des frontières maritimes avec le Cap-Vert, la Mauritanie, la Gambie et la Guinée-Bissau. Et avec 720 km de côtes, la ZEE du Sénégal s'étend sur 212 000 km25. 
je suis la c'est moi thiongy.
"""

# tb=decoupe(ch,10)

# i=0
# for g in tb:

#     google_wakh(g,'fr','male','tmp-'+str(i),'./tmp/')
#     i+=1


    

ar="بحقك, انهم لا يعلمون حتى بتواجدي"

es="Lo sé, por eso he venido a hablar con usted."
# google_wakh(ar,'ar','male','arabe1')
# google_wakh(es,'es','male','espagnol')



txt="""

La programmation réseau

Nos programmes peuvent à présent effectuer des tâches complexes et peuvent s'interfacer entre eux par le biais de fichiers ou de bases de données. Voyons à présent comment faire communiquer plusieurs programmes fonctionnant sur des ordinateurs différents via le réseau informatique. L'objectif de ce chapitre est d'aborder la communication entre plusieurs ordinateurs avec le mécanisme de sockets.

Un socket, que nous pouvons traduire par connecteur réseau, est une interface aux services réseaux offerte par le système d'exploitation permettant d'exploiter facilement le réseau. Cela permet d'initier une session TCP, d'envoyer et de recevoir des données par cette session. Nous utiliserons pour ce chapitre le module socket.

Nous travaillerons avec deux scripts, le serveur permettant d'écouter les demandes des clients et d'y répondre. Le client se connectera sur le serveur pour demander le service. Il est possible d'exécuter à la fois le client et le serveur sur un même ordinateur. Pour cela, il vous suffit de renseigner 127.0.0.1 comme adresse IP pour la partie client.

"""

p=print


txt=txt*4
p(len(txt))

taille=len("".join(txt.split(" ")))
p(taille)
import os

# os.mkdir("./hello")
lim="moi ferme . "
google_wakh(lim*200,'fr','male','limtext','./')

"""
    0. creer un bondata=[]
    1. calcule len de txt
        if >2000
            - on decoupe en paragraphe 
            - on partage la liste de paragraphe en deux
            - on transforme la partie 1 en chaine de caractere avec tmp1="".join(tabadata[0:len(tabdata)/2])
                - if len(tmp1)<2000
                    - c ok
                    - on creer les 2 parts
                    - p1="".join(tabadata[0:len(tabdata)/2])
                    - p2="".join(tabadata[len(tabdata)/2:len(tabdata)])
                    - bondata.append(p1)
                    - bondata.append(p2)
                    -for g in bondata:
                        googlewakh(g,lg,gr,filename,ds+'tmp_'+str(i))
                    - on merge les tmp_mp3 en filname.mp3
                    -on quitte
                    -return ['status':'ok']

                -else :
                    -on partage en 3
                        tmp2="".join(tabadata[0:len(tabdata)/3])
                        -if len(tmp2)<2000
                            -c ok
                        else:
                            return ['status':'ok']


"""


def google_decoupe(txt,lang,genre,filename,user,premium=False):
    """
    . on teste la longueur de txt
    . si len(txt)> 2500 et < 5000
        - alors on decoupe en deux parties
        - si >5000 <7500
            .. on decoupe en 3 partie
            
    - on boucle sur le tableau cree pour enregistrer dans un dossier username/tmp/...
    - on merge l'ensemble des mp3 dans un fichier filename.mp3 dans le dossier media/username/
    - 

    """
    
    tab1=[]
    tab2=[]
    tab3=[]
    
    if len(txt)<2500:
        google_wakh(txt,lang,genre,filename,user,premium=False)
        return 'ok'
    else:
        paragraphe=decoupe(txt)
        d=len(paragraphe)

        if len(txt)>=2500 and len(txt)<5000:
            size_2=int(d/2)
            
            tab1=" ".join(paragraphe[:size_2])
            tab2=" ".join(paragraphe[size_2:])
        
            return "ok"

        elif len(txt)>=5000 and len(txt)<7500:
            size_3=int(d/3)

            tab1=" ".join(paragraphe[:size_3])
            tab2=" ".join(paragraphe[size_3:(2*size_3)])
            tab3=" ".join(paragraphe[(2*size_3):])
            
            return "ok"
        else:
            return "Error"

