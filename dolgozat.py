#!/usr/bin/env python3

import datetime as date
from csoport import Csoport


class Doga:
    def __init__(self,ido,path):
        self.ido=ido
        self.path=path
        self.darab = len(path[0]['Max_Peter'])
        # ha szolfezs True "szolfezs", ha False "zeneelmelet" 
        self.targy= ['szolfézs','zeneelmélet']
        self.max_szolfezs = sum([int(b) for b in path[0]['Max_Peter'][:3]])
        self.max_zeneelm = sum([int(b) for b in path[0]['Max_Peter'][3:]])
        self.max_points = 0

    def __str__(self):
        return f"{self.ido:12} |{self.targy:12} | Feladatok száma: {self.darab} | Max pont: {self.max_score}"

    def szamol(self,s_points,m_points):
        szazalek = (s_points/m_points) * 100
        szazalek = f"{szazalek:.2f}" 
        return float(szazalek)

    def print_results(self):
        print(f"Maximális pontszám szolfézs: {self.max_szolfezs}")
        print(f"{'nev':20}|{'elért pont':12}|{'sz/z':15}|{'max':10}|{'%':7}|{'jegy':7}|")
        for nev,value in self.path[0].items():
            value=[float(b) for b in value]
            value=value[:3]
            szazalek=self.szamol(sum(value),self.max_szolfezs)
            print(f"{nev:20}|{sum(value):<12}|{self.targy[0]:15}|{self.max_szolfezs:<10}|{szazalek:7}|{self.jegy(szazalek):<7}|")
        
        print(f"Maximális pontszám zeneelmélet: {self.max_zeneelm}")
        print(f"{'nev':20}|{'elért pont':12}|{'sz/z':15}|{'max':10}|{'%':7}|{'jegy':7}|    ")  
        for nev,value in self.path[0].items():
            value=[float(b) for b in value]
            value=value[3:]
            szazalek = self.szamol(sum(value),self.max_zeneelm)
            print(f"{nev:20}|{sum(value):<12}|{self.targy[1]:15}|{self.max_zeneelm:<10}|{szazalek:<7}|{self.jegy(szazalek):<7}|")

    def jegy(self,rdm):
        if rdm < 50.5:
            return "1"
        elif 50.5 <= rdm < 63:
            return "2"
        elif 62.5 <= rdm < 74.6:
            return "3"
        elif 74.5 <= rdm < 87.5:
            return "4"
        elif rdm  >= 87.5:
            return "5"
