  def jouer_tour(self):
        while True:
            self.grille.afficher()
            print(f"C'est au tour de {self.joueur_actuel.get_nom()} ({self.joueur_actuel.get_symbole()})")

            try:
                ligne = int(input("Entrez la ligne (0-2) : "))
                colonne = int(input("Entrez la colonne (0-2) : "))
                if self.grille.placer_symbole(ligne, colonne, self.joueur_actuel.get_symbole()):
                    break
                else:
                    print("Case déjà occupée, réessayez.")
            except ValueError:
                print("Entrée invalide, réessayez.")

    def verifier_fin(self):
        if self.grille.verifier_gagnant(self.joueur_actuel.get_symbole()):
            self.grille.afficher()
            print(f"{self.joueur_actuel.get_nom()} a gagné !")
            return True
        if self.grille.est_pleine():
            self.grille.afficher()
    print("Match nul !")
            return True
        return False

    def lancer(self):
        print("Début du jeu !")
        while True:
            self.jouer_tour()
            if self.verifier_fin():
                break
            self.changer_joueur()


if _name_ == "_main_":
    nom1 = input("Nom du Joueur 1 : ")
    nom2 = input("Nom du Joueur 2 : ")
    
    joueur1 = Joueur(nom1, "X")
    joueur2 = Joueur(nom2, "O")
    
    partie = Partie(joueur1, joueur2)
    partie.lancer()
