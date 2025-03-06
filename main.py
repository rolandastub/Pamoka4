import math
import random
from math import floor
from operator import length_hint

# print in
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# print(numbers)

# for in range(30):
#
# numb = [random.randint(5,25)  for in range(30)]
#
# print(numb)
#
# nums = []
#
# for number in range(0,30):
#     # print (number)
#
#     rnd_nums = random.randint(5, 25)
#     # print(rnd_nums)
#     nums.append(rnd_nums)
# print (nums)
#
# # Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
#
# digits =0
# for number in nums:
#     if number >10:
#         digits +=1
# print(number)
#
# # Raskite didžiausią masyvo reikšmę
# max_value = nums[0]
# for number in nums:
#     if number > max_value:
#         max_value =number
# print( f'{max_value} didziausia reiksme')
#
# # Suskaičiuokite visų reikšmių sumą
#
# max_value = 0
# sum = sum(nums)
# print (f'{sum} random skaiciu suma')
#
# # Sukurkite naują masyvą, kurio reikšmės yra 1
# # uždavinio masyvo reikšmes minus tos reikšmės indeksas;
#
# new_nums =[]
# position = 0
# for i in nums:
#      # i -nums [:]
#     print (f'{position} indexas, {i} skaicius')
#     new_nums.append(i -(position))
#     position += 1
# print (new_nums)
#
# # Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25,
# # kad bendras masyvas padidėtų iki indekso 39
#
#
# for number in range(0,10):
#     rnd_nums = random.randint(5, 25)
#     nums.append(rnd_nums)
# print (nums)
# print(len(nums))
#
# # Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių,
# # o kitas iš porinių
#
# poriniai= []
# neporiniai =[]
# for i in range(0,len(nums)):
#    if i % 2==0:
#        print (i, nums[i])
#    else:
#        print(neporiniai, end="")
#
#
#
# for i in range(0, len(nums), 2):
#     if nums [i] > 15:
#         nums[i] = 0
#         print(nums)
# # Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10
#
# for i in range(0, len(nums)):
#  if nums[i]  > 10:
#     # [i] = 10
#     print(i)
#     break
#
# # Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D,
# # o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
#
#
#
# raides = ['A','B','C','D']
# ilgis = 200
# seka =[]
# for i in range (ilgis):
#     raides_pozicija = random.randint(0, len(raides)-1)
#     raide = raides[raides_pozicija]
#     seka.append(raide)
#     print(seka)
#
# # Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
#
# raides = ['B','A','D','C']
#
# raides.sort()
# print(raides)
#
# # 5Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# # Paskaičiuokite kiek unikalių reikšmių kombinacijų gavote.
# print(" === 5 uzd. ===")
# raides = ['A','B','C','D']
# ilgis = 200
# seka =[]
# seka1 =[]
# seka2 =[]
# for i in range (ilgis):
#     raides_pozicija = random.randint(0, len(raides)-1)
#     raide = raides[raides_pozicija]
#     seka.append(raide)
#
#     raides_pozicija1 = random.randint(0, len(raides)-1)
#     raide1 = raides[raides_pozicija1]
#     seka1.append(raide1)
#
#     raides_pozicija2 = random.randint(0, len(raides) - 1)
#     raide2 = raides[raides_pozicija2]
#     seka2.append(raide2)
# print("Sekos numeris yra 1")
# print(seka)
#
# print("Sekos numeris yra 2")
# print(seka1)
#
# print ("Sekos numeris yra 3")
# print(seka2)
#
# print(" === 5 uzd. === antra dalis")
# #Sudėkite masyvus, sudėdami atitinkamas reikšmes. Paskaičiuokite kiek unikalių reikšmių kombinacijų gavote.
#
# # raides = ['A','B','C','D']
# # ilgis = 200
#
# # seka = [0:201]
# # seka1 = [:201]
# # seka2 = [:201]
# # print
# # seku_suma = seka1+ seka2+ seka
# # print(seku_suma)
# # 'BDB','DCC','BCD',
#
#
# # PRASUKTI KOKI NORS CIKLA PRO PIRMA MASYVA, TOKIU BUDU, KAD TURETUM INDEXUS, IR ATSPAUSDINTI MASYVO ELEMENTUS
# # PAPILDYTI KODA: TAS REIKSMAS SUKRAUTI I NAUJA MASYVA
# # KLAUSTI NAGLIO KA DARYTI TOLIAU
#
#
# #
# raides = ['A','B','C','D']
# ilgis = 200
# seka =[]
# for i in range (ilgis):
#     raides_pozicija = random.randint(0, len(raides)-1)
#     raide = raides[raides_pozicija]
#     seka.append(raide)
#
# print("Sekos numeris  1")
# print(seka)
#
# masyvas = []
#
# for i in range(len(seka)):
#     print(f"Indeksas: {i}, Reikšmė: {seka[i]}, {seka1[i]}, {seka2[i]} {seka[i]+seka1[i]+seka2[i]}")
#     masyvas.append(seka[i] + seka1[i] + seka2[i])
#
# print(masyvas)
#
# print("======================6 uzduotis ===============================================")
#
# # 6. Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999.
# # Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve
#
#
# ilgis = 100
# reiksme_min = 100
# reiksme_max =999
# masyvas1 = [random.randint(100, 999) for _ in range(ilgis)]
# masyvas2 = [random.randint(100, 999) for _ in range(ilgis)]
# print("Pirmas masyvas")
# print(masyvas1)
# print ("Antras masyvas")
# print (masyvas2)
#
# print("================================7 uzdavinys=========================")
#
# # 7. Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių,
# # kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve
#
# masyvas3 = []
#
# for reiksme1 in masyvas1:
#     skirtingas = True
#     for reiksme2 in masyvas2:
#         if reiksme1 == reiksme2:
#             skirtingas = False
#             break
#     if skirtingas:
#         masyvas3.append(reiksme1)
# print("Skirtingos reiksmes:")
# print(masyvas3)
#
# print( "======================================= 8 uzdavinys ================================")
#
# # Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.
#
# masyvas4 = []
# for reiksme1 in masyvas1:
#     vienodos = False
#     for reiksme2 in masyvas2:
#         if reiksme1 == reiksme2:
#             vienodos = True
#             break
#     if vienodos:
#         masyvas4.append(reiksme1)
# print( "Vienodos reiksmes")
# print(masyvas4)
# #
# # Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25.
# # Trečias, pirmo ir antro suma.
# # ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma
# print("====================================9 uzdavinys=====================================")
#
# print("=====================9 uzdavinio 1 dalis=================")
# masyvas5 = [ 5,25]
# for i in range (0, 9):
#     masyvas5.append(masyvas5[i] + masyvas5[i+1])
# print ("Sprendimas su i+1")
# print(masyvas5)
# print("========================= 9 uzdavinio 2 dalis===============")
#
# masyvas6 = [5, 25]
#
# for i in range(0, 9):
#     masyvas6.append(masyvas6[i-1] + masyvas6[i])
# print("Sprendimas su su i-1" )
# print(masyvas6)
#
# print("========================10 uzdavinys=============================================")
# # Sugeneruokite 101 elemento masyvą su atsitiktiniais skaičiais nuo 0 iki 300.
#
# # Reikšmes kurios tame masyve yra ne unikalios pergeneruokite iš naujo taip, kad visos reikšmės masyve būtų unikalios.
#
# # Išrūšiuokite masyvą taip, kad jo didžiausia reikšmė būtų masyvo viduryje,
# # o einant nuo jos link masyvo pradžios ir pabaigos reikšmės mažėtų.
#
# # Paskaičiuokite pirmos ir antros masyvo dalies sumas (neskaičiuojant vidurinės).
#
# # Jeigu sumų skirtumas (modulis, absoliutus dydis) yra didesnis nei | 30 | rūšiavimą kartokite.
# # (Kad sumos nesiskirtų viena nuo kitos daugiau nei per 30)
#
ilgis = 101
masyvas7 = [random.randint(0, 300) for _ in range(ilgis)]

print(masyvas7)

for reiksme1 in masyvas7:
    skirtingas = True
    for reiksme2 in masyvas7:
        if reiksme1 == reiksme2:
            skirtingas = False
            break
    if skirtingas:
        masyvas7.append(reiksme1)

# print("Septintas masyvas", masyvas7)
#
#
#
#
# # Reikšmes kurios tame masyve yra ne unikalios pergeneruokite iš naujo taip, kad visos reikšmės masyve būtų unikalios.
#
# counter = 0
# for i in range(len(masyvas7)):
#     while True:
#         counter += 1
#         # if masyvas7[i] in (masyvas7[:i] + masyvas7[i+1:]):
#         if masyvas7.count(masyvas7[i]) > 1:
#             masyvas7[i] = random.randint(0,300)
#         else:
#             break
# print(masyvas7)
# print(counter)




# Išrūšiuokite masyvą taip, kad jo didžiausia reikšmė būtų masyvo viduryje,
# o einant nuo jos link masyvo pradžios ir pabaigos reikšmės mažėtų.

masyvas7c = masyvas7.copy()
masyvas7c.sort(reverse=True)
print(masyvas7c)

masyvas8 = [ 0 for _ in range(len(masyvas7))]

# print(len(masyvas7c))
# print(len(masyvas7c)/2)
# print(math.floor(len(masyvas7c)/2))
# print(math.ceil(len(masyvas7c)/2))
# print(round(len(masyvas7c)/2))

for i in range(0, math.floor(len(masyvas7c) / 2)):
    print(masyvas7c[i],masyvas7c[len(masyvas7c) - i -1])
masyvas8[50] = masyvas7c[0]
puse =  math.floor(len(masyvas7c) / 2)
count =0;
for i in range(1, 101,2 ):
    # if i % 2 == 0:
        masyvas8[ puse - count]  = masyvas7c[i]
    # else:
        masyvas8[ puse + count] = masyvas7c[i+1]
        count +=1
print(masyvas8)
print(len(masyvas7c))


# print(masyvas7c[1 : math.floor(len(masyvas7c) / 2) :2])
# print(masyvas7c[2: math.floor(len(masyvas7c) / 2) : 2])
# print(masyvas7c[0])
ma = masyvas7c[1 : len(masyvas7c):2]
mb = [masyvas7c[0]]
mc = masyvas7c[2 : len(masyvas7):2]
ma.reverse()
result = ma + mb + mc
print(result)
print(len(result))

