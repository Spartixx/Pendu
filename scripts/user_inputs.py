from db_functions import *
from config import JAUNE, VERT, ROUGE, DEFAULT

def ask_user_language(error_loop:int=0) -> str:
    """
    Permet d'obtenir le langage des mots souhaité pour le jeu.

    Returns:
        str: Une chaîne correspondant au langage.
    """

    langues = {1:"fr_FR", 2:"en", 3:"es_ES", 4:"de_DE"}

    try:
        return langues[int(input(f"{DEFAULT}Veuillez choisir une langue parmi celles ci :\n{VERT}1: Français (France)\n2: Anglais\n3: Espagnol (Espagne)\n4: Allemand (Allemagne)\n{DEFAULT}Votre réponse : {JAUNE}"))]
    
    except ValueError:
        print(f"{ROUGE}Choix invalide. Veuillez séléctionner un nombre entre 1 et {len(langues)}{DEFAULT}")
        return ask_user_language()
    
    except:
        print(f"{ROUGE}Une erreur est survenue... Veuillez réessayer.{DEFAULT}")
        if error_loop >=3: # Sécurité anti tour de boucle infini
            raise f"{ROUGE}Erreur... Fermeture du jeu..."
        return ask_user_language(error_loop+1)
    

def ask_letter(used_letter:list, error_loop:int=0) -> str:
    """
    Cette fonction permet de demander à l'utilisateur une lettre.

    Args:
        used_letter(list): Liste dont les lettres ont déjà été demandé.

    Returns:
        str: La lettre choisie par l'utilisateur, mise en majuscule.
    """
    try:
        letter = str(input(f"{DEFAULT}Les lettres déjà choisies sont les suivantes : \n-{"\n-".join(used_letter)}\nVeuillez choisir une lettre : {JAUNE}"))
        if letter.upper() in used_letter:
            print(f"{ROUGE}Cette lettre a déjà été demandé... Choisissez-en une autre.{DEFAULT}")
            return ask_letter(used_letter)
        
        elif len(letter) != 1:
            print(f"{ROUGE}Ne choisissez qu'une seule lettre. Ni plus, ni moins.{DEFAULT}")
            return ask_letter(used_letter)
        
        else:
            return letter.upper()
        
    except:
        print(f"{ROUGE}Une erreur est survenue... Veuillez réessayer.{DEFAULT}")
        if error_loop >=3: # Sécurité anti tour de boucle infini
            raise f"{ROUGE}Erreur... Fermeture du jeu..."
        return ask_letter(used_letter, error_loop+1)
    
def ask_replay(error_loop:int=0) -> bool:
    """
    Permet de demander à l'utilisateur si il souhaite relancer une partie.

    Returns:
        bool: Retourne True si la réponse est positive. Retourne False le cas inverse.
    """
    try:
        reponse = str(input(f"{DEFAULT}Voulez vous relancer une partie ({VERT}Y{DEFAULT}/{ROUGE}N{DEFAULT}) : "))
        if reponse in ["Y", "y"]:
            return True
        
        elif reponse in ["N", "n"]:
            return False
        
        else:
            print(f"{ROUGE}Réponse invalide, veuillez entrer soit \"Y\", soit \"N\". Réessayez.{DEFAULT}")
            return ask_replay()
        
    except:
        print(f"{ROUGE}Une erreur est survenue. Veuillez réessayer.{DEFAULT}")
        if error_loop >=3: # Sécurité anti tour de boucle infini
            raise f"{ROUGE}Erreur... Fermeture du jeu..."
        return ask_replay(error_loop+1)
    
def ask_username(error_loop:int=0) -> str:
    """
    Permet d'obtenir le nom d'utilisateur.

    Returns:
        str: Retourne le nom d'utilisateur.
    """


    try:
        pseudo = str(input(f"Veuillez entrer votre pseudo : {JAUNE}"))
        if len(pseudo) > 50 or len(pseudo) < 1:
            raise ValueError
        return pseudo
    
    except ValueError:
        print(f"{ROUGE}Veuillez entrer un pseudo entre 1 et 50 charactères !{DEFAULT}")
        return ask_username()
    
    except:
        print(f"{ROUGE}Une erreur est survenue... Veuillez réessayer.{DEFAULT}")
        if error_loop >=3: # Sécurité anti tour de boucle infini
            raise f"{ROUGE}Erreur... Fermeture du jeu..."
        return ask_username(error_loop+1)
    

def ask_show_stats(error_loop:int=0) -> bool:
    """
    Permet de demander à l'utilisateur si il veut afficher les statistiques ou lancer une partie.

    Returns:
        bool: True si il a demandé à afficher les statistiques. False si il a demandé à lancer une partie.
    """
    try:
        reponse = int(input(f"{DEFAULT}Voulez afficher les statistiques des parties ou jouer ? \n1: Afficher les statistiques\n2: Jouer\nEntrer votre réponse : "))
        
        if reponse not in [1, 2]:
            return ValueError
        
        if reponse == 1:
            return True
        
        else:
            return False
        
    except ValueError:
        print(f"{ROUGE}Veuillez entrer une valeur valide !{DEFAULT}")
        return ask_show_stats()
    
    except:
        print(f"{ROUGE}Une erreur est survenue. Veuillez réessayer.{DEFAULT}")
        if error_loop >=3: # Sécurité anti tour de boucle infini
            raise f"{ROUGE}Erreur... Fermeture du jeu..."
        return ask_replay(error_loop+1)
