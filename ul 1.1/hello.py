#1.2 Esimene programm
print("Tere, maailm!")
print("Ma õppin Pythonit.")
print("Mul on", 3, "kassi")
print("Aasta on", 2026, sep="-") #, -> ""
print("2026", "10", "01", sep="-")

print("Sama ", end="") # end="\n" =Enter, "\t"=tab
print("rida")
nimi= "Python" #str-sõne
vanus= 30 #int-täisarv
laius=25 #float-ujukomaarv
täna_on_koolis= True #bool-tõeväärtus

print(nimi*3)
print(nimi+nimi)
print(vanus+laius)
print(täna_on_koolis)

KABEMAKS = 0.24
hind = 100
print("hind koos käibemaksuga on", hind * (1 + KABEMAKS))
nimi = input("Sisesta oma nimi: ") #tagastab str formaadis
print(f"Tere, {nimi} !")
a = int(input("Sisesta esimene arv: ")) # "2" int("2")-> 2
b = int(input("Sisesta teine arv: ")) #tagastab str formaadis, int-ks konverteerimine
print(a+b) #str + str = str 2+5=25

#Aritmeetilised põhioperatsioonid
print(f"astendamine: {a} ** {b} = {a**b}")
print(f"korrutamine: {a} * {b} = {a*b}")
print(f"jagamine: {a} / {b} = {a/b}")
print(f"jagamisjääk: {a} % {b} = {a%b}")
print(f"liitmine: {a} + {b} = {a+b}")
print(f"lahutamine: {a} - {b} = {a-b}")
print(f"jagamise täisarvuline osa: {a} // {b} = {a//b}")

