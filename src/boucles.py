# 33 - Écrire un programme, qui affiche 9 fois ”Je suis un bon programmeur en Python ” à l’aide de l’instruction for
def question33():
  for _ in range(9):
    print("Je suis un bon programmeur en Python")

# 34 - Écrire un programme qui affiche la table de multiplications de « 2 » (de 0 jusqu’à 10) en affichant : 2 * 0 = 0
def question34():
  for i in range(11):
    print(f'2 * {i} = {2 * i}')

# 35 - Écrire un programme qui affiche un joli sapin de Noël, dont la taille est donnée par l’utilisateur. Exemple pour une taille de 12 lignes
def question35():
  height = 12
  for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '^' * (2 * i - 1)
    print(spaces + stars)
    

def main():
  print("[33 - Écrire un programme, qui affiche 9 fois ”Je suis un bon programmeur en Python ” à l’aide de l’instruction for]:")
  question33()
  print("------------------------------------------------------\n\n")
  
  print("[34 - Écrire un programme qui affiche la table de multiplications de « 2 » (de 0 jusqu’à 10) en affichant : 2 * 0 = 0]:")
  question34()
  print("------------------------------------------------------\n\n")
  
  print("[35 - Écrire un programme qui affiche un joli sapin de Noël, dont la taille est donnée par l’utilisateur. Exemple pour une taille de 12 lignes]:")
  question35()
  print("------------------------------------------------------\n\n")

if __name__ == '__main__':
  main()