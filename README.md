# projet-TOO
import random
from datetime import datetime

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
        super()._init_(nom, adresse, telephone, cnic, login, mot_de_passe, limite_retrait)
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

# Classe EmployeBancaire
class EmployeBancaire:
    def _init_(self, nom_utilisateur, mot_de_passe):
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe

    def approuver_compte(self, client):
        print(f"Compte client {client.id_client} approuvé.")

# Classe Carte
class Carte:
    def _init_(self, id_client, num_carte, pin):
        self.id_client = id_client
        self.num_carte = num_carte
        self.pin = pin

    def verifier_pin(self, pin_entree):
        return self.pin == pin_entree

# Test des classes
# Création d'un client utilisateur
client1 = ClientUtilisateur("Jean Dupont", "123 rue Exemple", "0123456789", "CNIC123456", "jdupont", "motdepasse", 500000)
client1.ouvrir_compte("Compte courant")

# Déposer de l'argent
client1.deposer_fonds(10000)
print(f"Solde après dépôt: {client1.compte.solde} FCFA")

# Retirer de l'argent
client1.retirer_fonds(2000)
print(f"Solde après retrait: {client1.compte.solde} FCFA")

# Vérification des transactions
for transaction in client1.compte.consulter_transactions():
    print(transaction)

# Créer une carte et vérifier le PIN
carte1 = Carte(client1.id_client, "1234567890123456", "1234")
print(carte1.verifier_pin("1234"))  # Devrait retourner True
# Création d'un client utilisateur
client1 = ClientUtilisateur("Jean Dupont", "123 rue Exemple", "0123456789", "CNIC123456", "jdupont", "motdepasse", 500000)

# Ouverture d'un compte pour le client
compte1 = client1.ouvrir_compte("Compte courant")
print(f"Nom du client: {client1.nom}")
print(f"ID Client: {client1.id_client}")
print(f"Type de compte: {compte1.type_compte}")
print(f"Solde initial: {compte1.solde}")

# Déposer de l'argent
client1.deposer_fonds(10000)
print(f"Solde après dépôt: {client1.compte.solde}")

# Retirer de l'argent
client1.retirer_fonds(2000)
print(f"Solde après retrait: {client1.compte.solde}")

# Vérification des transactions
print("Transactions effectuées :")
for transaction in client1.compte.consulter_transactions():
    print(transaction)

# Test d'un retrait qui échoue (montant trop élevé)
client1.retirer_fonds(20000)  # Cela doit échouer
