#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import turtle

# TODO: Importez vos modules ici
def mass_volume_ellipsoide(a,b,c,mass_density):
    def volume_ellipsoide(a,b,c):
        return (4/3)* math.pi * a * b * c
    mass = volume_ellipsoide(a, b, c) * mass_density
    return (volume_ellipsoide(a,b, c), mass)
def arbre(nombre):
    leo = turtle.Turtle()
    if nombre == 0:
        return(leo.forward(0))
    else:
        if nombre == 1:
            return(leo.forward(1))
        else:
            return(arbre(nombre -1) + arbre(nombre - 2))
    




# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(mass_volume_ellipsoide(5,3,7, 0.7))
    arbre(5)

    pass
