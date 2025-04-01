class Grille:
    def _init_(self):
        self.tableau = [[" " for _ in range(3)] for _ in range(3)]

    def afficher(self):
        for ligne in self.tableau:
            print("|".join(ligne))
            print("-" * 5)

    def placer_symbole(self, ligne, colonne, symbole):
        if self.tableau[ligne][colonne] == " ":
            self.tableau[ligne][colonne] = symbole
            return True
        return False

    def verifier_gagnant(self, symbole):
        # Vérification des lignes et colonnes
        for i in range(3):
            if all(self.tableau[i][j] == symbole for j in range(3)) or \
               all(self.tableau[j][i] == symbole for j in range(3)):
                return True
   # Vérification des diagonales
        if all(self.tableau[i][i] == symbole for i in range(3)) or \
           all(self.tableau[i][2 - i] == symbole for i in range(3)):
            return True

        return False

    def est_pleine(self):
        return all(self.tableau[i][j] != " " for i in range(3) for j in range(3))


class Partie:
    def _init_(self, joueur1, joueur2):
        self.grille = Grille()
        self.joueurs = [joueur1, joueur2]
        self.joueur_actuel = joueur1

    def changer_joueur(self):
        self.joueur_actuel = self.joueurs[1] if self.joueur_actuel == self.joueurs[0] else self.joueurs[0]
