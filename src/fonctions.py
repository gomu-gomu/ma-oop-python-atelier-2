# 36 - Ecrire un script fonctions.py, qui demande à l’utilisateur de saisir 2 valeurs numériques. Et puis s’assurer est-ce l’utilisateur a bien saisi des valeurs numériques en utilisant les conditions.
def question36():
  def is_numerique(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

  def input_valeur():
    while True:
      user_input = input('Entrer une valeur numerique: ')
      if is_numerique(user_input):
          return float(user_input)
      else:
          print("Erreur : Veuillez saisir une valeur numérique valide.")
  
  val1 = input_valeur()
  val2 = input_valeur()

  return val1, val2

# 37 - Ajouter la fonction somme qui calcule et affiche la somme des deux valeurs saisies dans la question (36).
def question37(val1, val2):
  def somme(val1, val2):
    s = val1 + val2
    print(f'La somme de {val1} et {val2} est: {s}')
     
  somme(val1, val2)

# 38 - Ajouter la fonction multiplication qui calcule et retourne la multiplication des deux valeurs saisies dans la question (36) sans les afficher en utilisant return.
def question38(val1, val2):
  def multiplication(val1, val2):
    return val1 * val2
     
  return multiplication(val1, val2)

# 39 - Ajouter la fonction multiplication qui calcule et retourne la multiplication des deux valeurs saisies dans la question (36) sans les afficher en utilisant return.
def question39(val1, val2, val):
  print(f'La multiplication de {val1} par {val2} est: {val}')

# 40 - Ajouter la fonction division qui calcule la division des deux valeurs saisies dans la question (1). Et puis ajouter la condition pour empêcher la division par Zéro. 
def question40(val1, val2):
  def division(val1, val2):
    if val2 == 0:
        return "(Erreur -> Division par zéro impossible)"
    return val1 / val2
  
  d = division(val1, val2)
  print(f'La division de {val1} sur {val2} est: {d}')

# 41 - Ajouter la fonction table_multiplication qui affiche la table de multiplication (du 0 jusqu’à 10) d’une variable numérique donnée en paramètre, comme mentionné ci-dessous.
def question41():
  num = int(input('Entrez un nombre pour calculer la table de multiplication pour: '))

  def table_multiplication(val):
    for i in range(11):
       print(f'{val} * {i} = {val * i}')
  
  table_multiplication(num)

# 42 - Travailler la question (41) en utilisant lambda et map.
def question42():
  num = int(input('Entrez un nombre pour calculer la table de multiplication pour: '))

  def table_multiplication(val):
    result = map(lambda i: f'{val} * {i} = {val * i}\n', range(11))
    print(''.join(result))
  
  table_multiplication(num)
    

def main():
  print("[36 - Ecrire un script fonctions.py, qui demande à l’utilisateur de saisir 2 valeurs numériques. Et puis s’assurer est-ce l’utilisateur a bien saisi des valeurs numériques en utilisant les conditions]:")
  val1, val2 = question36()
  print("------------------------------------------------------\n\n")
  
  print("[37 - Ajouter la fonction somme qui calcule et affiche la somme des deux valeurs saisies dans la question (36)]:")
  question37(val1, val2)
  print("------------------------------------------------------\n\n")
  
  print("[38 - Ajouter la fonction multiplication qui calcule et retourne la multiplication des deux valeurs saisies dans la question (36) sans les afficher en utilisant return]:")
  val = question38(val1, val2)
  print("------------------------------------------------------\n\n")
  
  print("[39 - Afficher le résultat de la question (38)]:")
  question39(val1, val2, val)
  print("------------------------------------------------------\n\n")
  
  print("[40 - Ajouter la fonction division qui calcule la division des deux valeurs saisies dans la question (1). Et puis ajouter la condition pour empêcher la division par Zéro]:")
  question40(val1, val2)
  print("------------------------------------------------------\n\n")
  
  print("[41 - Ajouter la fonction table_multiplication qui affiche la table de multiplication (du 0 jusqu’à 10) d’une variable numérique donnée en paramètre, comme mentionné ci-dessous]:")
  question41()
  print("------------------------------------------------------\n\n")
  
  print("[42 - Travailler la question (41) en utilisant lambda et map]:")
  question42()
  print("------------------------------------------------------\n\n")

if __name__ == '__main__':
  main()