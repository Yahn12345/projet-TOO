# Classe de base Client
class Client:
    def _init_(self, nom, adresse, telephone, cnic, login, mot_de_passe, limite_retrait):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.cnic = cnic
        self.login = login
        self.mot_de_passe = mot_de_passe
        self.limite_retrait = limite_retrait
        self.compte = None
        self.id_client = None

    def ouvrir_compte(self, type_compte):
        # Assignation d'un ID client unique et génération d'une carte aléatoire
        self.id_client = random.randint(1000, 9999)
        self.compte = Compte(type_compte, self.id_client)
        return self.compte

# Classe ClientUtilisateur (héritée de Client)
class ClientUtilisateur(Client):
    def _init_(self, nom, adresse, telephone, cnic, login, mot_de_passe, limite_retrait):
        sup
er()._init_(nom, adresse, telephone, cnic, login, mot_de_passe, limite_retrait)
        self.type_client = "Utilisateur"

    def deposer_fonds(self, montant):
        if montant > 0:
            self.compte.solde += montant
            self.compte.enregistrer_transaction('Dépôt', montant)
        else:
            print("Montant invalide pour un dépôt.")

    def retirer_fonds(self, montant):
        if montant > 0 and montant <= self.compte.solde and montant <= self.limite_retrait:
            self.compte.solde -= montant
            self.compte.enregistrer_transaction('Retrait', montant)
        else:
            print("Montant excédant la limite ou solde insuffisant.")
