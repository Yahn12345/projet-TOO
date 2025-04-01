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
client1.retirer_fonds(20000)  # Cela doit échouer
