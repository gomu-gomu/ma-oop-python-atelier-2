data = ['Python', 'Java', 'PHP', 'C', 'C++', 'Français', 'SQL', 'Arabe', 'PLSQL']

# 9 - Écrire un programme liste_langages.py qui initialise et affiche la liste dont les éléments sont : Python, Java, PHP, C, C++, Français, SQL, Arabe et PLSQL
def question9():
	print(data)

# 10 - Donner le nombre d’éléments de la liste.
def question10():
	print(len(data))

# 11 - Afficher la liste de manière inversée
def question11():
	data.reverse()
	print(data)

# 12 - Afficher la liste de manière triée.
def question12():
	data.sort()
	print(data)

# 13 - Ajouter le langage Assembleur dans la liste,
def question13():
	data.append('Assembleur')
	print(data)

# 14 - Supprimer les langages qui n’ont aucune relation avec la programmation informatique. Et puis afficher la liste après la suppression. 
def question14():
	data.remove('Français')
	data.remove('Arabe')

	print(data)

# 15 - Donner le nombre des éléments de la liste après la suppression.
def question15():
	print(len(data))

# 16 - Afficher le nombre de caractères de chaque élément de la liste
def question16():
	for word in data:
		print(f'Element: {word} - Nombre de caractères: {len(word)}')

# 17 - Vider les éléments de la liste
def question17():
	data.clear()
	print(data)

def main():
	print("9 - Écrire un programme liste_langages.py qui initialise et affiche la liste dont les éléments sont : Python, Java, PHP, C, C++, Français, SQL, Arabe et PLSQL")
	question9()
	print("------------------------------------------------------\n\n")

	print("[10 - Donner le nombre d’éléments de la liste]:")
	question10()
	print("------------------------------------------------------\n\n")

	print("[11 - Afficher la liste de manière inversée]:")
	question11()
	print("------------------------------------------------------\n\n")

	print("[12 - Afficher la liste de manière triée]:")
	question12()
	print("------------------------------------------------------\n\n")

	print("[12 - Afficher la liste de manière triée]:")
	question12()
	print("------------------------------------------------------\n\n")

	print("[13 - Ajouter le langage Assembleur dans la liste]:")
	question13()
	print("------------------------------------------------------\n\n")

	print("[14 - Ajouter le langage Assembleur dans la liste]:")
	question14()
	print("------------------------------------------------------\n\n")

	print("[15 - Donner le nombre des éléments de la liste après la suppression]:")
	question15()
	print("------------------------------------------------------\n\n")

	print("[16 - Afficher le nombre de caractères de chaque élément de la liste]:")
	question16()
	print("------------------------------------------------------\n\n")

	print("[17 - Vider les éléments de la liste]:")
	question17()
	print("------------------------------------------------------\n\n")

if __name__ == '__main__':
	main()
