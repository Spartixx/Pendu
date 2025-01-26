import sqlite3
from config import ROUGE

con = sqlite3.connect("db.db")
cur = con.cursor()


def save_game_stats(username:str, langue:str, mot:str, win:bool, time:int, rounds:int, start_date, send_game_id:bool = False) -> None:
    """
    Permet d'ajouter les données relatives à la partie dans la base de données.
    Args:
        username (str): Pseudo du joueur
        langue (str): Langue choisie par le joueur pour la partie.
        mot (str): Mot choisit par le système pour la partie.
        win: (bool) True pour une victoire, False pour une défaite.
        time (int): Correspond au temps écoulé en seconde depuis le début de la partie.
        rounds (int): Correspond au nombre de tour effectués pour la partie.
    """

    try:
        cur.execute(f"INSERT INTO Score('username', 'langue', 'mot', 'win', 'temps', 'tour', 'date') VALUES('{username}', '{langue[0:2]}', '{mot}', '{win}', '{time}', '{rounds}', datetime('now','localtime'));")
        con.commit()
    
        if send_game_id:
            game_id = cur.execute("SELECT game_id FROM Score ORDER BY game_id DESC LIMIT 1;")
            return game_id.fetchone()[0]
        

    except:
        print(f"{ROUGE}Un problème est survenu lors de la sauvegarde des données, la partie ne sera pas sauvegardée.")

def get_stats() -> list:
    """
    Permet d'obtenir les données de toutes les parties dans une liste. Chaque partie est également stockée dans une liste.

    Returns:
        list[list]: Tableau à 2 dimensions correspondant aux données des parties.
    """

    try:
        req = cur.execute('SELECT * FROM Score ORDER BY win DESC, temps ASC, tour ASC;')
        return req.fetchall()
    except:
        pass # L'erreur sera levée dans les fonctions utilisant les statistiques. L'exécution continuera néanmoins.


def delete_stats() -> None:
    """
    Permet de supprimer les statistiques des données précédentes.
    """
    cur.execute("DELETE FROM Score;")
    con.commit()