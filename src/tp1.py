import math

# 1 - Créer un nouveau projet sur PyCharm, et saisir le script suivant et l’enregistrer sous le nom tp1.py
def question1():
    a = 5
    print("a = ", a) 

    b = 5.50
    print("b = ", b) 

    c = 5,50,14
    print("c = ",c)

    texte = "Mon texte"
    print(texte)

    print("type de a: ",type(a))
    print("type de b: ",type(b))
    print("type de c: ",type(c))
    print("type de texte: ",type(texte))

# 2 a - Écrire un programme, qui définit 3 variables : une variable de type texte, une variable de type nombre entier, une variable de type nombre décimal et qui affiche leur type.
def question2a():
	text = "Hello"
	numInt = 13
	numDec = 0.369
	
	print("type de text: ",type(text))
	print("type de numInt: ",type(numInt))
	print("type de numDec: ",type(numDec))

# 2 b - Affecter dans une même ligne les 3 variables précédemment définies.
def question2b():
	text, numInt, numDec = "World", 369, 1036.7803

# 3 - Écrire un programme qui, à partir de la saisie d’un rayon et d’une hauteur, calcule le volume d’un cône droit
def question3():
	r = float(input("Enter un rayon: "))
	h = float(input("Enter une hauteur: "))

	v = 1/3 * math.pi * math.pow(r, 2) * h
	print(f"Le volume d'un cône qui a une hauteur de {h} et un rayon de {r} est {v}")
	

# 4 - Une machine découpe dans une plaque, des disques circulaires de rayon rExt, percés d’un trou circulaire de rayon rInt avec rInt < rExt et ne débordant pas du disque Quelle est la surface d’un disque découpé ?
def question4():
	# a - trouver les données
	rExt = float(input("Enter une valeur pour rExt: "))
	rInt = float(input("Enter une valeur pour rInt: "))

	# b - effectuer les calculs
	sExt = math.pi * math.pow(rExt, 2)
	sInt = math.pi * math.pow(rInt, 2)
	surface = sExt - sInt

	# c - afficher le résultat
	print(f"La curface de cercle est: {surface}")

# 5 - Écrire un programme qui affiche le type du résultat des instructions suivantes: a = 3 / a = =3
def question5():
	a = 3
	print("Type de a=3 est:", type(a))

	a = '=3'
	print("Type de a=3 est:", type(a))

# 6 - Écrire un programme, qui ajoute une chaîne de caractères à un nombre entier (Exemple la chaîne ”le chat” et le nombre 3 pour donner le chat 3), et puis renvoyer la taille de chaine
def question6():
	a = "le chat"
	b = 3
	c = a + " " + str(b)

	print(f"La taille de '{c}' est: {len(c)}")

# 7 - Écrire un programme qui réalise la saisie d’un nombre entier puis affiche la valeur ainsi saisie et son type. Essayer de dépasser la taille maximale des entiers. Expliquer.
def question7():
	num = int(input("Entrer un nombre: "))

	print(f"Num = {num}, type = {type(num)}")

# 8 -  Ecrire un programme qui transforme un nombre de base décimale vers la base binaire, et puis renvoyer son adresse mémoire.
def question8():
	base10 = float(input('Entrer un décimale: '))
	base2 = bin(int(base10))

	print(f"la valeur {base10} est {base2} en binaire")
	
def main():
	print("[1 - Créer un nouveau projet sur PyCharm, et saisir le script suivant et l’enregistrer sous le nom tp1.py]:")
	question1()
	print("------------------------------------------------------\n\n")
	
	print("2 [a - Écrire un programme, qui définit 3 variables : une variable de type texte, une variable de type nombre entier, une variable de type nombre décimal et qui affiche leur type]:")
	question2a()
	print("------------------------------------------------------\n\n")
	
	print("2 [b - Affecter dans une même ligne les 3 variables précédemment définies]:")
	question2b()
	print("------------------------------------------------------\n\n")
	
	print("[3 - Écrire un programme qui, à partir de la saisie d’un rayon et d’une hauteur, calcule le volume d’un cône droit]:")
	question3()
	print("------------------------------------------------------\n\n")
	
	print("[4 - Une machine découpe dans une plaque, des disques circulaires de rayon rExt, percés d’un trou circulaire de rayon rInt avec rInt < rExt et ne débordant pas du disque Quelle est la surface d’un disque découpé ?]:")
	question4()
	print("------------------------------------------------------\n\n")
	
	print("[5 - Écrire un programme qui affiche le type du résultat des instructions suivantes: a = 3 / a = =3]:")
	question5()
	print("------------------------------------------------------\n\n")
	
	print("[6 - Écrire un programme, qui ajoute une chaîne de caractères à un nombre entier (Exemple la chaîne ”le chat” et le nombre 3 pour donner le chat 3), et puis renvoyer la taille de chaine]:")
	question6()
	print("------------------------------------------------------\n\n")
	
	print("[7 - Écrire un programme qui réalise la saisie d’un nombre entier puis affiche la valeur ainsi saisie et son type. Essayer de dépasser la taille maximale des entiers. Expliquer]:")
	question7()
	print("------------------------------------------------------\n\n")
	
	print("[8 - Ecrire un programme qui transforme un nombre de base décimale vers la base binaire, et puis renvoyer son adresse mémoire]:")
	question8()
	print("------------------------------------------------------\n\n")

if __name__ == '__main__':
	main()
