#!/usr/bin/env python3

class Csoport:
    def __init__(self,nev,forras):
        self.nev=nev
        self.forras=forras
        self.nevsor=[]
        self.adatok=[]

    def __str__(self):
        nevek = "\n".join(self.nevsor)
        return f"A csoport neve: {self.nev}\nA benne szereplők: \n{nevek()}"

    def __repr__(self):
        return self.__str__()

    def load(self):
        adat={}
        with open(self.forras) as ff:
            for i in ff:
                i=i.strip().split(",")
                if i:
                    print(i)
                    self.nevsor.append(i[0])
                    adat[i[0]]=i[1:]
            self.adatok.append(adat)

        return self.adatok

    def nevek(self):
        for i in self.nevsor:
            print(i)
        
    
