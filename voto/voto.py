import math
import operator
from dataclasses import dataclass
import flet
cfuTot = 180

@dataclass
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool
    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    #def __eq__(self, other):
        #return (self.materia == other.materia and
                #self.punteggio == other.punteggio and
                #self.lode == other.lode)

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto):
        if (self.hasConflitto(voto) is False
            and self.hasVoto(voto) is False):
            self.voti.append(voto)
        else:
            raise ValueError("Il voto è già presente")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        """
        restituisce la media dei voti attualmente presenti nel libretto
        :return: valore numerico della media, oppure ValueError in caso la lista fosse vuota
        """

        #media = sommaVoti / numeroEsamisami
        # v = []
        # for v1 in self.voti:
        #     v.append(v1.punteggio)
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota.")

        v = [v1.punteggio for v1 in self.voti]
        return sum(v)/len(v)
        # return math.mean(v)

    def getVotiByPunti(self, punti, lode):
        """
        restituisce una lista di esami con punteggio uguale a punti (e lode se applicabile)
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se presente la lode
        :return: lista di voti
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)
        return votiFiltrati

    def getVotoByName(self, nome):
        """
        restituisce un oggetto Voto il cui campo materia è uguale a nome
        :param nome: stringa che indica il nome della materia
        :return: oggetto di tipo Voto, oppure None in caso di voto non trovato
        """
        for v in self.voti:
            if v.materia == nome:
                return v


    def hasVoto(self, voto):
        '''

        verifica se il libretto contiene già il voto; due voti sono considerati uguali se hanno
        lo stesso campo materia e lo stesso punteggio. Punteggio è formato da punteggio e lode
        :param voto: istanza dell'oggetto voto
        :return: True se il voto è gia presente, False altrimenti

        '''

        for v in self.voti:
            # modo numero 1
            #if v==voto:
             #   pass
            if (v.materia == voto.materia and v.lode == voto.lode
                and v.punteggio == voto.punteggio):
                return True
        return False

    def hasConflitto(self, voto):
        '''
        controlla che il voto non rappresenti un conflitto con i voti già presenti nel libretto
        consideriamo conflitto quando due voti hanno lo stesso campo materia ma diverso voto
        :param voto: istanza della classe voto'
        :return: True se voto è in conflitto, False altrimenti
        '''
        for v in self.voti:
            if (v.materia == voto.materia and not
            (v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        '''
        crea una nuova copia del libretto e restituisce un'istanza della classe libretto
        :return:
        '''
        nuovo = Libretto(self.proprietario.copy(), [])
        for v in self.voti:
            nuovo.append(v.copy())
        return nuovo

    def creaMigliorato(self):
        '''
        crea un nuovo oggetto libretto in cui i voti sono migliorati secondo la seguente
        logica:
        se il voto è compreso tra 18 e 24 aggiungo 1, se il voto è compreso tra 24 e 28 aggiungo 2,
        se il voto è 29 aggiungo 1, se è 30 rimane 30
        :return: nuovo Libretto
        '''
        nuovo = self.copy()

        for v in nuovo.voti:
            if 18 <= v.punteggio < 24:
                v.punteggio += 1
            elif 24 <= v.punteggio <29:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30
        return nuovo

    def sortByMateria(self):
        #self.voti.sort(key=estraiMateria)
        self.voti.sort(key=operator.attrgetter('materia'))
    # ozione 1: creo due metodi stampa che ordinano e poi stampano
    # opzione 2: creo due metodi che ordinano la lista di self e poi un unico metodo di stampa
    # opzione 3:

    def creaLibOrdinatoPerMateria(self):
        '''
        crea un nuovo oggetto libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        '''
        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        '''
        crea un nuovo oggetto libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        '''
        nuovo = self.copy()
        nuovo.voti.sort(key=lambda v: (v.punteggio, v.lode), reverse=True)
        return nuovo

    def cancellaInferiori(self, punteggio):
        #modo 1
        #for i in range(len(self.voti)):
            #if self.voti[i].punteggio < punteggio:
                #self.voti.pop(i)

        #modo 2
        #for v in self.voti:
            #if v.punteggio < punteggio:
                #self.voti.remove(v)
        #modo 3
        #nuovo = []
        #for v in self.voti:
            #if v.punteggio >= punteggio:
                #nuovo.append(v)
        #self.voti = nuovo

        return [v for v in self.voti if v.punteggio >= punteggio]

def estraiMateria(voto):
    '''
    questo metodo restituisce il campo materia dello stesso voto
    :param voto: istanza della classe voto
    :return: stringa rappresentante il nome della materia
    '''
    return voto.materia

def testVoto():
    print("Ho usato Voto in maniera standalone")
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    print(v1)

    mylib = Libretto(None, [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)
    print((flet.Text(mylib)))

if __name__ == "__main__":
    testVoto()


# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"
