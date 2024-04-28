#fix le fichier json, il est sous un mauvais format, ajoute les accol au debut et fin aussi : [ligne 1 -- lignefin]
import json

# Chemin vers le fichier d'entrée et de sortie
input_file_path = "C:/Users/Elitebook 845 G8/pythonprojects/Software_Complet.json"
output_file_path = "C:/Users/Elitebook 845 G8/pythonprojects/Software_Complet_Propre.json"

# Ouvrir les fichiers d'entrée et de sortie
with open(input_file_path, "r") as input_file:
    with open(output_file_path, "w") as output_file:
        first_line = True  # Indique si c'est la première ligne
        for line in input_file:
            if not first_line:
                output_file.write(",\n")  # Ajoute une virgule suivie d'un retour à la ligne avant chaque objet JSON (à l'exception du premier)
            first_line = False
            output_file.write(line.rstrip("\n"))  # Écrit la ligne sans le saut de ligne

print("succès.")

