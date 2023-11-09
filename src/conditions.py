# 31 a - Écrire un programme conditions.py qui demande de saisir 2 valeurs numériques et qui affiche la plus petite des 2 valeurs.
def question31a(val1, val2):
    if val1 < val2:
       print('La premier valeur est inférieur que la deuxième')
    elif val1 > val2:
       print('La deuxième valeur est inférieur que la premier')

# 31 b - Dans le même programme précédant, afficher la plus grande des 2 valeurs déjà saisis dans la première question.
def question31b(val1, val2):
    if val1 > val2:
       print('La premier valeur est supérieur que la deuxième')
    elif val1 < val2:
       print('La deuxième valeur est supérieur que la premier')

# 31 c - Dans le même programme précédant, afficher si les deux valeurs sont égaux.
def question31c(val1, val2):
    if val1 == val2:
       print('La premier et la deuxième valeurs sont égaux')
    else:
       print('La premier et la deuxième valeurs sont pas égaux')

def main():
    val1 = float(input('Entrer la premier valeur:'))
    val2 = float(input('Entrer la deuxième valeur:'))

    print("[31 a - Écrire un programme conditions.py qui demande de saisir 2 valeurs numériques et qui affiche la plus petite des 2 valeurs]:")
    question31a(val1, val2)
    print("------------------------------------------------------\n\n")

    print("[31 b - Dans le même programme précédant, afficher la plus grande des 2 valeurs déjà saisis dans la première question]:")
    question31b(val1, val2)
    print("------------------------------------------------------\n\n")

    print("[31 c -  Dans le même programme précédant, afficher si les deux valeurs sont égaux]:")
    question31c(val1, val2)
    print("------------------------------------------------------\n\n")

if __name__ == '__main__':
  main()