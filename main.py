import random

# print in
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# print(numbers)

# for in range(30):
#
# numb = [random.randint(5,25)  for in range(30)]
#
# print(numb)

nums = []

for number in range(0,30):
    # print (number)

    rnd_nums = random.randint(5, 25)
    # print(rnd_nums)
    nums.append(rnd_nums)
print (nums)

# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;

digits =0
for number in nums:
    if number >10:
        digits +=1
print(number)

# Raskite didžiausią masyvo reikšmę
max_value = nums[0]
for number in nums:
    if number > max_value:
        max_value =number
print( f'{max_value} didziausia reiksme')

# Suskaičiuokite visų reikšmių sumą

max_value = 0
sum = sum(nums)
print (f'{sum} random skaiciu suma')

# Sukurkite naują masyvą, kurio reikšmės yra 1
# uždavinio masyvo reikšmes minus tos reikšmės indeksas;

new_nums =[]
position = 0
for i in nums:
     # i -nums [:]
    print (f'{position} indexas, {i} skaicius')
    new_nums.append(i -(position))
    position += 1
print (new_nums)

# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25,
# kad bendras masyvas padidėtų iki indekso 39


for number in range(0,10):
    rnd_nums = random.randint(5, 25)
    nums.append(rnd_nums)
print (nums)
print(len(nums))

# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių,
# o kitas iš porinių

poriniai= []
neporiniai =[]
for i in range(0,len(nums)):
   if i % 2==0:
       print (i, nums[i])
   else:
       print(neporiniai, end="")



for i in range(0, len(nums), 2):
    if nums [i] > 15:
        nums[i] = 0
        print(nums)
# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10

for i in range(0, len(nums)):
 if nums[i]  > 10:
    # [i] = 10
    print(i)
    break

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D,
# o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.



raides = ['A','B','C','D']
ilgis = 200
seka =[]
for i in range (ilgis):
    raides_pozicija = random.randint(0, len(raides)-1)
    raide = raides[raides_pozicija]
    seka.append(raide)
    print(seka)

# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.

raides = ['B','A','D','C']

raides.sort()
print(raides)

# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# Paskaičiuokite kiek unikalių reikšmių kombinacijų gavote.

raides = ['A','B','C','D']
ilgis = 200
seka =[]
for i in range (ilgis):
    raides_pozicija = random.randint(0, len(raides)-1)
    raide = raides[raides_pozicija]
    seka.append(raide)
    print(seka*3)

