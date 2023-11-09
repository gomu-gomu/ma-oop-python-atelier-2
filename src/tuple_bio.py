data = ('ADN', 'ARN', 'Protéine', 'Virus', 'Bactérie')

# 18 - Écrire un programme tuple_bio.py qui initialise et affiche le tuple dont les éléments sont : ADN, ARN, Protéine, Virus, Bactérie
def question18():
	print(data)

# 19 - Donner le nombre d’éléments du tuple
def question19():
	print(len(data))

# 20 - Déterminer si l’élément Corona spécifié est présent dans le tuple.
def question20():
	if 'Corona' in data:
		print('Corona est présent danse le tuple')
	else:
		print('Corona n\'est présent danse le tuple')

# 21 - Renvoyer la position de l’élément Protéine.
def question21():
	print(data.index('Protéine'))

# 22 - Afficher le nombre de caractères de chaque élément du tuple.
def question22():
	for word in data:
		print(f'Element: {word} - Nombre de caractères: {len(word)}')

# 23 - Supprimer complétement le tuple
def question23():
	exemple_tuple = ('ADN', 'ARN', 'Protéine', 'Virus', 'Bactérie')
	del exemple_tuple


def main():
	print("[18 - Écrire un programme tuple_bio.py qui initialise et affiche le tuple dont les éléments sont : ADN, ARN, Protéine, Virus, Bactérie]:")
	question18()
	print("------------------------------------------------------\n\n")
	
	print("[19 - Donner le nombre d’éléments du tuple]:")
	question19()
	print("------------------------------------------------------\n\n")
	
	print("[20 - Déterminer si l’élément Corona spécifié est présent dans le tuple]:")
	question20()
	print("------------------------------------------------------\n\n")
	
	print("[21 - Renvoyer la position de l’élément Protéine]:")
	question21()
	print("------------------------------------------------------\n\n")
	
	print("[22 - Afficher le nombre de caractères de chaque élément du tuple]:")
	question22()
	print("------------------------------------------------------\n\n")
	
	print("[23 - Supprimer complétement le tuple]:")
	question23()
	print("------------------------------------------------------\n\n")

if __name__ == '__main__':
	main()
