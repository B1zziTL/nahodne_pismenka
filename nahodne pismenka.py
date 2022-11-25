#importovanie modulu
import random

#otvorenie suborov
subor = open("poprehadzovany_text1_vstup.txt", "r")
subor1 = open("poprehadzovany_text1.txt", "w")

#zadeklarovanie premennych a zoznamov
prve = "nic"
posledne = "nic"
daco = 0
povodny_text = []
prerobeny_text = []
poprehadzovanie = []
nove_slovo = []
novy_riadok = []
pouzite = []

for riadok in subor: #cyklus na prechadzanie riadkov v subore
    #priradenie vycisteneho riadku do zoznamu
    povodny_text.append(riadok.strip())

    #rozdelenie riadku
    riadocek = riadok.split()
    
    for slovo in riadocek: #cyklus na prechadzanie slov v riadku
        for pismeno in slovo: #cyklus na prechadzanie pismen v slove
            #podmienka na zapisanie pismena ako prveho, posledneho, alebo vlozenie do zoznamu na poprehadzovanie
            if daco == 0:
                prve = pismeno
            elif daco == len(slovo)-1:
                posledne = pismeno
            else:
                poprehadzovanie.append(pismeno)
                
            #zmena pomocnej funkcie    
            daco += 1

        #zadeklarovanie pomocnej funkcie
        daco = 0    
        
        def funkcia(): #funkcia na poprehadzovanie pismen
            #zadeklarovanie globalnych premennych
            global poprehadzovanie, indexik, nahodne, nove_slovo
            
            for i in poprehadzovanie: #cyklus pre polozky v zozname
                #vylosovanie nahodne pismena, zistenie jeho indexu, zapisanie do zoznamu a odstranenie z povodneho zoznamu
                nahodne = random.choice(poprehadzovanie)
                indexik = poprehadzovanie.index(nahodne)
                nove_slovo.append(nahodne)
                poprehadzovanie.pop(indexik)

                #podmienka na opakovanie funkcie alebo zrusenie
                if len(poprehadzovanie) > 1:
                    funkcia()
                else:
                    if not len(poprehadzovanie) == 0:
                        funkcia()
                        return None
                    return None

        #vyvolanie funkcie        
        funkcia()

        #vytvorenie noveho riadku
        spojene = "".join(nove_slovo)
        finalne_slovo = prve + spojene + posledne
        novy_riadok.append(finalne_slovo)

        #vymazanie poloziek zoznamov
        poprehadzovanie.clear()
        nove_slovo.clear()

    #vytvorenie prerobeneho suboru
    novy_riadocek = " ".join(novy_riadok)  
    prerobeny_text.append(novy_riadocek)
    subor1.write(novy_riadocek + "\n")

    #vymazanie poloziek zo zoznamu
    novy_riadok.clear()

#vypisanie pozadovanych hodnot    
print(*povodny_text,sep="\n")
print("----------")
print(*prerobeny_text,sep="\n")

#zatvorenie suborov
subor.close()
subor1.close()
