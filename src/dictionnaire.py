data = {
	'votre nom': 'Essamadi',
	'votre prénom': 'Oussama',
	'votre âge': 25,
	'votre spécialité': 'Developpeur'
}

# 24 - Écrire un programme dictionnaire.py qui initialise et affiche le dictionnairedont les éléments sont : votre nom, votre prénom, votre âge, votre spécialité
def question24():
	print(data)

# 25 - Parcourir les valeurs du dictionnaire.
def question25():
	for value in data.values():
		print(value)

# 26 - Parcourir les clés du dictionnaire.
def question26():
	for key in data.keys():
		print(key)

# 27 - Modifier la valeur d’âge en réduisant 2ans.
def question27():
	data['votre âge'] -= 2
	print(data)

# 28 - Ajouter l’élément date d’obtention du Bac au dictionnaire.
def question28():
	data['date d’obtention du Bac'] = '2016-06-27'
	print(data)

# 29 - Supprimer l’élément votre spécialité.
def question29():
	del data['votre spécialité']
	print(data)

# 30 - Vider le dictionnaire.
def question30():
	data.clear()
	print(data)

def main():
	print("[24 - Écrire un programme dictionnaire.py qui initialise et affiche le dictionnairedont les éléments sont : votre nom, votre prénom, votre âge, votre spécialité]:")
	question24()
	print("------------------------------------------------------\n\n")
	
	print("[25 - Parcourir les valeurs du dictionnaire]:")
	question25()
	print("------------------------------------------------------\n\n")
	
	print("[26 - Parcourir les clés du dictionnaire]:")
	question26()
	print("------------------------------------------------------\n\n")
	
	print("[27 - Modifier la valeur d’âge en réduisant 2ans]:")
	question27()
	print("------------------------------------------------------\n\n")
	
	print("[28 - Ajouter l’élément date d’obtention du Bac au dictionnaire]:")
	question28()
	print("------------------------------------------------------\n\n")
	
	print("[29 - Supprimer l’élément votre spécialité]:")
	question29()
	print("------------------------------------------------------\n\n")
	
	print("[30 - Vider le dictionnaire]:")
	question30()
	print("------------------------------------------------------\n\n")

if __name__ == '__main__':
	main()
