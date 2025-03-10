from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry", "Potter", 11, "castani",
                "castani", "Grifondoro", "civetta",
                "Expecto Patronum")
mylib = Libretto(Harry, [])

v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-12", False)
mylib.append(v1)
mylib.append(v2)

mylib.append(Voto("Pozioni", 21, "2022-06-14", False))
mylib.append(Voto("Trasfigurazione", 21, "2022-06-14", False))

mylib.calcolaMedia()

votiFiltrati = mylib.getVotiByPunti(21, False)
print(votiFiltrati)

votoTrasfigurazione = mylib.getVotoByName("Trasfigurazione")

if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione.materia)

print(mylib.hasVoto(v1))
print(mylib.hasVoto(Voto("Magia", 30, "2023-07-10", False)))
print(mylib.hasVoto(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)))

print(mylib.hasConflitto(Voto("Pozioni", 27, "2022-02-12", False)))

print("Test append modificata")
mylib.append(Voto("Magia", 30, "2023-07-10", False))
#mylib.append(Voto("Pozioni", 27, "2022-02-12", False))


mylib.append(Voto("Divinazione", 27, "2021-02-08", False))
mylib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))

print("----------------------------------------")


print("----------------------------------------")
nuovoLib = mylib.creaMigliorato()
print("Libretto migliorato")
print(nuovoLib)
print("----------------------------------------")
print("Libretto originario")
print(mylib)

print("----------------------------------------")
print("----------------------------------------")
ordinato = mylib.creaLibOrdinatoPerMateria()
print("Libretto ordinato per materia")
print(ordinato)
print("----------------------------------------")
ordinato2 = mylib.creaLibOrdinatoPerVoto()
print("Libretto ordinato per materia")
print(ordinato2)

print("-----------------------------------------")
print("Libretto a cui ho eliminato i voti inferiori a 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)