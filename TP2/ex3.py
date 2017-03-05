#!/usr/bin/env python
#-*- coding: utf-8 -*-

def reste(x, n, p):
	resultat = [1]
	initial = x
	courant = 0
	while courant != p and x not in resultat:
		resultat.append(x%n)
		x = (x*initial)%n
		courant +=1
		print resultat
	courant +=1
	resultat.append(x%n)
	if courant == p:
		return x
	else :
		reste = p%courant
		return resultat[reste]


x = input("Entrez un nombre : ")
p = input("Entrez la puissance du nombre : ")
n = input("Entrez le modulo : ")
r = reste(x, n, p)
print "Le reste de",x,"puissance",p,"modulo",n,"est égale à",r 
