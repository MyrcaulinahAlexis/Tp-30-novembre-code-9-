#1 - Nan on chen karakte mmete tout karakte yo en miniskil

chenn_original= 'LIFE IS WORTH LIVING'
chenn_miniskil = chenn_original.lower() 


print(chenn_miniskil)

#2 - Koupe chen lan tout kote ki gen espas,epi ajoute yon lis ki gen chak eleman yo

chenn_original= 'LIFE IS WORTH LIVING'
list_mo = chenn_original.split()

print(list_mo)


#3 - Mete tout premye let chak mo an majiskil 

chenn_original = 'LIFE IS WORTH LIVING'
chenn_modifye = chenn_original.title()

print(chenn_modifye)


#4 - Rekipere premye let chak mo., epi ajoute yon nouvo cheb ak tout inisyal sa yo

chenn_original = 'LIFE IS WORTH LIVING'
premye_let_chak_mo= ''.join([mot[0] for mot in chenn_original.split()])

print(premye_let_chak_mo)


#5  Ranplase tout karakte i ki nan chen lan pa @

chenn_original = 'LIFE IS WORTH LIVING'

if 'i' in chenn_original:
    nouvo_chenn = chenn_original.replace('a', '@')
    print(nouvo_chenn)
else:
    print(chenn_original)


#6 - Mete on chen karakte devan deye pi metel an majiskil 

chenn_original = 'life is worth living'

chenn_inves_majiskil = chenn_original[::-1].upper()

print(chenn_inves_majiskil)


#7 - afiche endeks premye karakte "i" ki nan yon chen

chenn_original = 'life is worth living'

endeks_i = chenn_original.index('i')

print(" index premye let 'i' an se :", endeks_i)


#8 - affiche total endeks karakte:"i"

chenn_original = 'life is worth living'

# Inisyakise som des indices
total_endeks_i = 0

for index, karakte in enumerate(chenn_original):
    if karakte == 'i':
        total_endeks_i += index

print(" Total index tout karakte 'i' se :", total_endeks_i)


#9 - Kreye yon lis ki gen endeks tout karakte a ki nan on chen selman si a minikil

chenn_original = 'Life is worth living'

endeks_karakte_i_miniskil= []
for index, karakte in enumerate(chenn_original):
    if karakte == 'i' and karakte.islower():
        endeks_karakte_i_miniskil.append(index)

print("endeks 'i' miniskil yo se :", endeks_karakte_i_miniskil)


#10 - Retire tout espas ki gen nan chen lan

chenn_original = 'Life is worth living'

chenn_san_espas = chenn_original.replace(' ', '')

print("Chenn san espas lan se :", chenn_san_espas)

