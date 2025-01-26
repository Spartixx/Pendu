import random
from faker import Faker
from config import JAUNE, VERT, ROUGE, DEFAULT
from db_functions import save_game_stats, get_stats
from user_inputs import *
from stats import get_colors, get_classement

class Pendu:
    """
    Cette classe reprèsente un Pendu.
    """

    def __init__(self) -> None:
        self.word = ""
        self.structure = {(x,y):[" ", True] for x in range(6) for y in range(6)}
        self.ordre_pendu = [(1,2), (1,3), (0,3), (2,3), (0,4), (2,4)]
        self.create_base_structure()
        self.create_pendu()
        self.used_letters = []
        self.good_letters = []
        self.WORDS_PATH = "./ressources/words"

        self.game_loop = True
        self.username = "Player 1"
        self.langue = ""
        self.rounds = 0
        

    def set_words(self, number:int=50, language:str="fr_FR") -> None:
        """
        Permet d'écrire aléatoirement des mots dans un fichier txt.

        Args: 
            number(int): Correspond au nombre de mots aléatoire à écrire dans le fichier.
        """
        def format_words(words:list) -> list:
            new_liste = []
            formated_chars = {"é":"e", "è": "e", "ê": "e", "à": "a", "ç": "c", "â": "a", "ô": "o", "î": "i"}
            for word in words:
                new_word = ""
                for letter in word:
                    if letter in formated_chars.keys():
                        new_word += formated_chars[letter]
                    else:
                        new_word+=letter
                new_liste.append(new_word)
            return new_liste
        
        
        fake = Faker(language) #On instantie en fonction de la langue choisie.
        words_list = fake.words(number) #Liste de x mots.


        with open(self.WORDS_PATH, "w", encoding="utf-8") as words_file:
            words_file.write("\n".join(format_words(words_list)))

    def choose_random_word(self) -> str:
        """
        Permet de choisir un mot aléatoire en français parmi le fichier de mots.

        Returns:
            str: Un mot aléatoire en français.
        """

        with open(self.WORDS_PATH, "r", encoding="utf-8") as words_file:
            word = random.choice(words_file.readlines())
            if word[-1] == "\n":
                self.word = word[:-1].upper()
            else:
                self.word = word.upper()
        
    def create_base_structure(self) -> None:
        """
        Permet de créer la structure du Pendu
        """

        for y in range(1,6):
            self.structure[(5, y)] = [f"{VERT}|{DEFAULT}", True]

        for x in range(1,6):
            self.structure[(x, 0)] = [f"{VERT}_{DEFAULT}", True]

        self.structure[(1,1)] = [f"{VERT}|{DEFAULT}", True]

    def create_pendu(self):
        """
        Permet de placer les membres au bon endroit. Les membres sont non-visibles par défaut.
        """
        self.structure[(0,3)] = [f"{ROUGE}/{DEFAULT}", False]
        self.structure[(0,4)] = [f"{ROUGE}/{DEFAULT}", False]
        self.structure[(2,3)] = [f"{ROUGE}\\{DEFAULT}", False]
        self.structure[(2,4)] = [f"{ROUGE}\\{DEFAULT}", False]
        self.structure[(1,2)] = [f"{ROUGE}O{DEFAULT}", False]
        self.structure[(1,3)] = [f"{ROUGE}|{DEFAULT}", False]

    def display_word(self) -> str:
        """
        Renvoie l'état du mot formaté pour être affiché dans le jeu.

        Returns:
            str: Mot formaté pour l'affichage.
        """
        word_row = ""
        for letter in self.word:
            if letter in self.good_letters:
                word_row += letter
            else:
                word_row += "_"

        return word_row

    def player_turn(self, letter:str) -> None:
        """
        Effectue les actions relatives au tour d'un joueur en fonction de la lettre qu'il a choisie.

        Args:
            letter(str): Lettre choisie par le joueur.
        """

        if letter not in self.used_letters:
            self.used_letters.append(letter)
            

        if letter in self.word:
            self.good_letters.append(letter)

        else:
            self.structure[self.ordre_pendu.pop(0)][1] = True

    def check_win(self) -> bool:
        """
        Permet de vérifier si le joueur a gagné, ou au contraire, si il a perdu.

        Returns:
            bool: True si le joueur gagne, False si il perd et None si la partie continue.
        """

        if self.ordre_pendu == []:
            return False
        
        elif self.display_word() == self.word:
            return True

    def display_game(self) -> None:
        """
        Permet d'afficher l'état du jeu (Pendu et état du mot)
        """

        for y in range(6):
            row = ""
            for x in range(6):
                if self.structure[(x,y)][1]:
                    row += self.structure[(x,y)][0]
                else:
                    row += " "
            print(row)

        print(f"{VERT}="*9 + f"\n{DEFAULT}")
        print(f"{DEFAULT}L'état du mot est : {VERT}{self.display_word()}{DEFAULT}")


    def win_procedure(self, win:bool, message:str, start_time:float, end_time:float, start_date, game_function):
        self.display_game()
        print(message)
        colors = get_colors(win, int(end_time-start_time), self.rounds)
        self.game_loop = False
        game_id = save_game_stats(self.username, self.langue, self.word, win, int(end_time-start_time), self.rounds, start_date, send_game_id=True) 
        print(f"Statistiques pour {JAUNE}{self.username}{DEFAULT} :   Classement : {JAUNE}{get_classement(game_id)}{DEFAULT}   |   Victoire : {colors['win']}{win}{DEFAULT}   |   Temps : {colors["temps"]}{int(end_time-start_time)}{DEFAULT}   |   Tours : {colors["tours"]}{self.rounds}{DEFAULT}")
        if ask_replay():
            return game_function()
            
            