import time
from pendu_class import Pendu
from user_inputs import *
from db_functions import *
from stats import *
from config import VERT


def game() -> None:
    """
    Représente la boucle du jeu. Elle instantie la partie et gère son déroulement.
    """
    pendu = Pendu() # Instantiation de la partie.

    pendu.username = ask_username() # Demande du pseudo.
    pendu.langue = ask_user_language() # Demande de la langue.
    pendu.set_words(language=pendu.langue) # Définition des mots en fonction de la langue.
    pendu.choose_random_word() # Choix du mot.

    start_date = time.localtime()
    start_time = time.time() # Date de lancement de la partie

    while pendu.game_loop: # Boucle de jeu
        
        pendu.display_game() # Affichage
        pendu.player_turn(ask_letter(pendu.used_letters)) # Tour du joueur
        pendu.rounds += 1

        win = pendu.check_win()

        if win == True: # Victoire
            pendu.win_procedure(win, "Vous avez gagné !", start_time, time.time(), start_date, game)

        elif win == False: # Défaite
            pendu.win_procedure(win, f"Vous avez perdu... Le mot était : {VERT}{pendu.word}{DEFAULT} !", start_time, time.time(), start_date, game)

if __name__ == '__main__':
    if ask_show_stats(): # Menu : Afficher les statistiques
        show_stats(get_stats())
        if ask_replay(): # Demander après l'affichage si le joueur souhaite démarrer une partie.
            game()
    else: # Menu : Sinon, jouer
        game()