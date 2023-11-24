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

def DNA():
    def is_valid_sequences(chaine):
        return chaine.isalnum() and (("A" or "T" or "G" or "C") in chaine.capitalize())

    def valid_sequences():
        while True:
            sequences = input("Enter a DNA sequences: ")

            if is_valid_sequences(sequences):
                return sequences, len(sequences)
            error = "The DNA sequeces is not valid\nTry again!"
            print(error)
    
    def proportion_valide(validChaine, lenValidChaine):
        while True:
            deux_elem = input("Enter a sequence of two DNA bases: ")

            if len(deux_elem) == 2:
                nb  = validChaine.count(deux_elem)
                proportion = round(((nb*2)/ lenValidChaine) * 100, 2)
                return proportion, deux_elem
            error = "The DNA sequeces is not made of only two bases\n Try again!"
            print(error)
    
    chaîne, lenChaine = valid_sequences()
    porportion, deux_bases = proportion_valide(chaîne, lenChaine)

    return f'chaîne : {chaîne}\nséqueence: "{deux_bases}"\nIl y a {porportion} % de "{deux_bases}".'




    







if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(mass_volume_ellipsoide(5,3,7, 0.7))
    print(DNA())
    

    pass
