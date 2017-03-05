#!/usr/bin/env python
#-*- coding: utf-8 -*-

def euclide(b, n): 
	"""renvoi un le triplet : le pgcd, l'inverse pour la multiplication de b modulo n et l'inverse pour la multiplication modulo b de n"""
	x0, x1, y0, y1 = 1, 0, 0, 1
	while n != 0:
		q, b, n = b // n, n, b % n #q = la partie entière de la division de b et n, b prend la valeur de n et n prend la valeur du modulo de b et n
		x0, x1 = x1, x0 - q * x1 #x0 prend la valeur de x1, x1 prend la valeur de x0 - q * x1
		y0, y1 = y1, y0 - q * y1 #y0 prend la valeur de y1, 1 prend la valeur de y0 - q * y1
	return b, x0, y0 #b = b*x0 + n*y0

b = input("Entrez b : ")
n = input("Entrez n : ")
x,x0,y0=euclide(b, n)
print "Le pgcd est",x,", on obtient donc",x,"=",x0,"*",b,"+",y0,"*",n

