#!/usr/bin/env python3

class Feladat:
    def __init__(self,sorszam, max_pont):
        self.sorszam=sorszam
        self.max_pont=max_pont
        

    def __str__(self):
        return f"{self.sorszam}. feladat - max pont: {self.maxpont}"

