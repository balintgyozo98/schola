#!/usr/bin/env python3

from csoport import Csoport
import dolgozat
import datetime as dt
import valassz
from dolgozat import Doga

def menu():


    """
    Ennek a programnak a célja az, hogy kényelmesen, értelemszerűen tudjuk, tudjam rögzíteni a havi rendszerességgel megírt dolgozatok eredményeit
    """

    while True:
        print("Válassz mit szeretnél csinálni! " )
        print("\t Új dolgozat rögzítése (1)")
        print("\t Régi eredmények megtekintése (2)")
        print("\t Kilépés (10)")
        
        choice = input('Választásod: ')
        if choice== '1':
            hely = valassz
            hely.kiir()
            forras = input('Melyik filéből dolgozunk? ')
            forras = f"/home/balint/work/dolgozatok/{forras}"
            nev='11_b'
            elso = Csoport(nev,forras)
            elso.load()
            ido=dt.datetime(2025,11,7)
            oktober=Doga(ido,elso.adatok)
            oktober.print_results()
        
        elif choice == '2':
            pass
        
        elif choice == '10':
            break
            csoport_neve=input('Írja le, melyik csoport dolgozatait szeretné rögzíteni: ')
            targy = input("Írja meg melyik tárgy (szolfézs/zeneelmélet) eredményeit szeretné rögzíteni: ")
            forras = f'/home/balint/balintenv/home/dolgozatok/{csoport_neve}.txt'
            elso_cs=Csoport(csoport_neve,forras)
            elso_cs.betolt()
            elso_cs.nevek()
            print(elso_cs.__str__())

if __name__=="__main__":
    menu()
