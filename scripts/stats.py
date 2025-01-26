from config import *
from db_functions import get_stats

def show_stats(datas:list) -> None:
        """
        Permet d'afficher les statistiques de jeux en fonction des données en paramètres.

        Args:
            list: Liste des données de jeu. Données de jeu : list
        """
        try:
            if len(datas) == 0:
                print(f"{ROUGE}Aucune données de jeu à afficher... Veuillez jouer des parties.")
            else:
                print(f"{VERT}Statistiques triées en fonction de la victoire, puis du temps, puis du nombre de tours.\n{DEFAULT}")
                for row in datas:
                    colors = get_colors(row[-4], row[-3], row[-2])
                    print(f"{VERT}{row[1]}{DEFAULT} :     Victoire : {colors["win"]}{row[-4]}{DEFAULT}   |   Temps : {colors["temps"]}{row[-3]} sec{DEFAULT}   |   Tour : {colors["tours"]}{row[-2]}{DEFAULT}   |   Mot : {VERT}{row[3]}{DEFAULT}   |   Langue : {VERT}{row[2]}{DEFAULT}   |   {JAUNE}{row[-1]}{DEFAULT}")
                print("\n")

        except:
            print(f"{ROUGE} Une erreur est survenue lors de l'affichage des statistiques...")


def get_colors(win:bool, temps:int, tours:int) -> dict:
    """
    Permet d'obtenir la bonne couleur en fonction des données suivantes : Victoire, temps, tours

    Args:
        win (bool): True si l'utilisateur a gagné, False sinon.
        temps (int): Le temps en second de la durée de la partie.
        tours (int): Le nombre de tour de la partie.
    """
    colorWin = VERT
    colorTemps = VERT
    colorTours = VERT

    if win == "False" or win == False: # Récupéré en string depuis la DB

        colorWin = ROUGE
    if temps > 30:
        colorTemps = ROUGE
    if tours > 8:
        colorTours = ROUGE

    return {"win": colorWin, "temps": colorTemps, "tours": colorTours}

def get_classement(game_id:int) -> int:

    """
    Permet d'obtenir le classement d'une partie en fonction de son id.

    Args:
        game_id (int): correspond à l'id de la partie dont le classement est souhaité.

    Returns:
        int : Le numéro de classement de la partie.
    """
    classement = 0
    for game in get_stats(): # Les statistiques de parties sont dans l'ordre.
        classement+=1
        if game[0] == game_id:
            return classement