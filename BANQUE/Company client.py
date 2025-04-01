# Classe ClientEntreprise (héritée de Client)
class ClientEntreprise(Client):
    def _init_(self, nom_entreprise, adresse_entreprise, numero_fiscal, login, mot_de_passe, limite_retrait):
        super()._init_(nom_entreprise, adresse_entreprise, "", "", login, mot_de_passe, limite_retrait)
        self.nom_entreprise = nom_entreprise
        self.numero_fiscal = numero_fiscal
        self.type_client = "Entreprise"
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)
        
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
# Classe Compte
class Compte:
    def _init_(self, type_compte, id_client):
        self.id_client = id_client
        self.type_compte = type_compte
        self.solde = 0
        self.transactions = []

    def enregistrer_transaction(self, type_transaction, montant, id_client_transfert=None):
        date_transaction = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Date actuelle
        transaction = {'date': date_transaction, 'id_client': self.id_client, 'montant': montant, 'type': type_transaction, 'id_transfert': id_client_transfert}
        self.transactions.append(transaction)

    def consulter_transactions(self):
        return self.transactions

