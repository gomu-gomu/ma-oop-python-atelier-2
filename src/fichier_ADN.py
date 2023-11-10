def calcule_taille_ADN(chaine):
	return len(chaine)

def nbr_A(chaine):
	return chaine.count('A')

def nbr_C(chaine):
	return chaine.count('C')

def ADN_2_ARN(ADN: str, file):
	ARN = ADN.replace('T', 'U')
	file.write('\n' + ARN)
	return ARN

def main():
	with open('./ADN.txt', 'r+') as file:
		# 1 - Ecrire un script fichie_ADN.py, qui ouvre et lit le contenu du fichier ADN.txt.
		ADN = file.read()
		print('1 - ADN :', ADN)
		
		# 2 - Ajouter la fonction calcule_taille_ADN qui calcule la longueur de la chaine ADN.
		longeurADN = calcule_taille_ADN(ADN)
		print('2 - Longeur de la chaine :', longeurADN)

		# 3 - Ajouter la fonction nbr_A qui calcule le nombre des « A » dans le fichier ADN.txt
		nombreA = nbr_A(ADN)
		print('3 - Nombre des A :', nombreA)

		# 4 - Ajouter la fonction nbr_C qui calcule le nombre des « C » dans le fichier ADN.txt.
		nombreC = nbr_C(ADN)
		print('4 - Nombre des C :', nombreC)

		# 5 - Ré-ouvrir le fichier ADN.txt en mode écriture et ajouter la fonction ADN_2_ARN qui génère l’ARN depuis l’ADN (en changeant le T par le U).
		ARN = ADN_2_ARN(ADN, file)
		print('5 - ARN :', ARN)

if __name__ == '__main__':
	main()