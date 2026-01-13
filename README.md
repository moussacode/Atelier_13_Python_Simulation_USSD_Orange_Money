# Simulation USSD Orange Money en Python

Ce projet est une simulation du service USSD Orange Money (#144#) développée en Python.  
Il reproduit les principales fonctionnalités d’Orange Money via un menu interactif en ligne de commande, avec une sauvegarde des données dans un fichier JSON.

Ce projet est réalisé à des fins pédagogiques afin de pratiquer la logique algorithmique et la gestion d’un système transactionnel simple.

---

## Fonctionnalités

L’application permet de :

- Consulter le solde
- Acheter du crédit
- Effectuer un transfert d’argent
- Annuler le dernier transfert
- Annuler un transfert par ID
- Consulter l’historique des transferts
- Acheter des forfaits internet
- Sécuriser chaque opération avec un code secret
- Sauvegarder automatiquement les données dans un fichier `data.json`

---

## Technologies utilisées

- Python 3
- JSON (persistance des données)
- Interface en ligne de commande (CLI)

---

## Gestion des données

Les informations sont stockées dans le fichier `data.json` :
- Solde du compte
- Liste des transferts
- Code secret
- Montant total transféré
- Historique des opérations

---

## Installation et exécution

1. Cloner le dépôt :
```bash
git clone https://github.com/moussacode/Atelier_13_Python_Simulation_USSD_Orange_Money.git
