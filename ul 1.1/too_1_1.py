#ulesanne 1
from os import *
nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
#ulesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
#ulesanne 3
import random
candy = random.randint(1, 100)
print(f"on laudal {candy} kommi")
kogus = float(input("Sisesta kui palju sa soovid: "))
kokku = candy - kogus
print(f"laual on alles {kokku} kommi")
#ulesanne 4
läbimõõt = float(input("Sisesta Puu ringjoone: "))
import math
raadius = läbimõõt / (math.pi)
print(f"Puu raadius on {raadius} m")
#ulesanne 5
a = float(input("Sisesta esimene arv: "))
b = float(input("Sisesta teine arv: "))
dioganaal = math.sqrt(a**2 + b**2)
print(f"Dioganaal on {dioganaal} m")
#ulesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus #see on segamini vale, õige on kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")
#ulesanne 7
arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
arv3 = float(input("Sisesta kolmas arv: "))
arv4 = float(input("Sisesta neljas arv: "))
arv5 = float(input("Sisesta viies arv: "))
keskmine = (arv1 + arv2 + arv3 + arv4 + arv5) / 5
print(f"Arvude keskmine on {keskmine}")