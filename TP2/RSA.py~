#!/usr/bin/env python
#-*- coding: utf-8 -*-

def eratosthene(n):
	"""retourne la liste_premiers des nombres premiers <= n (crible d'eratosthene)"""
	n += 1
	liste_premiers = [0,0] + [i for i in xrange(2, n)]
	for i in xrange(2, n):
		if liste_premiers[i] != 0:
			# c'est un nombre 1er: on garde, mais on neutralise ses multiples
			for j in xrange(i*2, n, i):
				liste_premiers[j] = 0
	return [p for p in liste_premiers if p!=0]

def decomposition_primaire(n):
	resultat = []
	liste_premiers = eratosthene(n)
	while n != 1:
		m = liste_premiers[0]
		if n%m == 0:
			resultat.append(m)
			n = n/m
		else:
			liste_premiers=liste_premiers[1:]
	return resultat
	
def indicatrice_euler(n):
	decomp=decomposition_primaire(n)
	resultat = 1
	k = 1
	n = decomp[0]
	while len(decomp)>1:
		decomp = decomp[1:]
		if decomp[0] == n:
			k += 1 
		else:
			resultat = resultat * ((n-1)*(n**(k-1)))
			k=1
		n = decomp[0]
	resultat = resultat * ((n-1)*(n**(k-1)))
	return resultat

def euclide(b, n): 
	"""renvoi un le triplet : le pgcd, l'inverse pour la multiplication de b modulo n et l'inverse pour la multiplication modulo b de n"""
	x0, x1, y0, y1 = 1, 0, 0, 1
	while n != 0:
		q, b, n = b // n, n, b % n #q = la partie entière de la division de b et n, b prend la valeur de n et n prend la valeur du modulo de b et n
		x0, x1 = x1, x0 - q * x1 #x0 prend la valeur de x1, x1 prend la valeur de x0 - q * x1
		y0, y1 = y1, y0 - q * y1 #y0 prend la valeur de y1, 1 prend la valeur de y0 - q * y1
	return b, x0, y0 #b = b*x0 + n*y0

def reste(x, n, p):
	resultat = [1]
	initial = x
	courant = 0
	while courant != p and x not in resultat:
		resultat.append(x%n)
		x = (x*initial)%n
		courant +=1
	courant +=1
	resultat.append(x%n)
	if courant == p:
		return x
	else :
		reste = p%courant
		return resultat[reste]

n = input("Entrez n : ")
p = input("Entrez p : ")
N = n*p
phi = indicatrice_euler(N)
print "Phi(N) = ",phi

e = input("Entrez e : ")
x,x0,y0=euclide(phi, e)
print "Le pgcd est",x,", on obtient donc",x,"=",x0,"*",N,"+",y0,"*",e,". d =",y0

x = input("Entrez un nombre : ")
p = y0
r = reste(x, N, p)
print "Le reste de",x,"puissance",p,"modulo",N,"est égale à",r,". M = ",r











