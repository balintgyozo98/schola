#!/usr/bin/env python3

import os
import pathlib

"""Én fogom navigálni, hogy mi történjen sok sikert kívánok"""
tartalom = "/home/balint/work/dolgozatok"
filek = os.listdir(tartalom)
def kiir():
    for i in filek:
        if "txt" in i:
            print(i)
