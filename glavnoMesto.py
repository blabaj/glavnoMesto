# -*- coding: utf-8 -*-
def glavnoMesto(drzava):
    drzava = drzava.upper()
    drzave = {"SLOVENIJA" : "LJUBLJANA", "HRVAŠKA" : "ZAGREB", "SRBIJA" : "BEOGRAD", "ITALIJA" : "RIM"}

    if drzava in drzave.keys():
        glavnoMestoDrzave = drzave[drzava]
        return glavnoMestoDrzave
    else:
        napaka = "Države še ni v bazi"
        return napaka


def preveriMesto(drzava, mesto):
    drzava = drzava.upper()
    mesto = mesto.upper()
    mestoPrimerjava = glavnoMesto(drzava)
    if mesto == mestoPrimerjava:
        print "Drži, mesto je pravilno!"

    else:
        print "Vpisano mesto ni glavno mesto te države!"



def main():
    drzava = raw_input("Vnesi ime države: ")
    mesto = raw_input("Vnesi njeno glavno mesto: ")
    preveriMesto(drzava, mesto)

if __name__ == '__main__':
    main()