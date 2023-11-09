# 32 - Écrire un script longeur_chaine.py, qui demande de saisir 2 chaînes de caractères et qui affiche la plus grande et la plus petite des 2 chaînes (celle qui a le plus et moins de caractères).
def question32():
  str1 = input('Entrer la premier chaine: ')
  str2 = input('Entrer la deuxième chaine: ')

  if str1 > str2:
    print(f'La plus grande chaine est: "{str1}"')
    print(f'La plus petite chaine est: "{str2}"')
  else:
    print(f'La plus grande chaine est: "{str2}"')
    print(f'La plus petite chaine est: "{str1}"')

def main():
  print("[32 - Écrire un script longeur_chaine.py, qui demande de saisir 2 chaînes de caractères et qui affiche la plus grande et la plus petite des 2 chaînes (celle qui a le plus et moins de caractères)]:")
  question32()
  print("------------------------------------------------------\n\n")

if __name__ == '__main__':
  main()