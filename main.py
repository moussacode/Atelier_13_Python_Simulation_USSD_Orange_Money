#Lien Github : https://github.com/moussacode/Atelier_13_Python_Simulation_USSD_Orange_Money.git

import json
solde_init = {
    "solde" :10000,
    "list_transfer":[],
    "mot_de_passe":"12345678",
    "montant_compte":0,
    "transfert" :{},

}


def sauvegarde():
    try:
        with open('./data.json','w') as data_view:
            json.dump(solde_init ,data_view,indent=4)
    except Exception as e :
        print('Erreur ',e)
def fetch_data():
    
    global solde_init 

    try :
        with open('./data.json','r') as data_view:
            solde_init = json.load(data_view)
    except  (FileNotFoundError, json.JSONDecodeError):
        sauvegarde()
            
    with open('./data.json','r') as data_view:
            solde_init = json.load(data_view)
            # print(solde_init)
            
            
            return 





mot_de_passe="12345678"
credit = 0
montant_compte=0


transfert ={}
list_transfer=[]

forfaits_acheter=[]


list_forfait = [
    {
    'id_pass':1,
    'forfait' : 'Pass 100 Mo',
    'prix' : 500
    },
    {
    'id_pass':2,
    'forfait' : 'Pass 500 Mo',
    'prix' : 1000
    },
    {
    'id_pass':3,
    'forfait' : 'Pass 1 Go',
    'prix' : 2000
    }
    ]


        

def afficher_transferts():
    print("===== LISTE DES  TRANSFERTS =====")
    for t in solde_init['list_transfer']:
        print(f"ID {t['id']} | {t['numero_destinataire']} | {t['montant']} F ")    


def annuler_transfert_par_id():
    global solde_init

    afficher_transferts()
    choix = input("Saisir l'ID du transfert à annuler (0 pour retour) : ")

    if choix == '0':
        return

    choix = int(choix)

    for transfert in solde_init['list_transfer']:
        if transfert['id'] == choix:

            if verifiermdp("l'annulation") == True:
                
                solde_init['solde'] += transfert['montant']

                solde_init['list_transfer'].remove(transfert)
                sauvegarde()
                

                print("Transfert annulé avec succès")
                print("Nouveau solde :", solde_init['solde'])
                return

    print("ID de transfert introuvable")

def historique():
    print('============= HISTORIQUE DE TRANSFERT ===============')
    print('')
    i=1
    for transfert in solde_init['list_transfer']:
                print(f" {i} {transfert['numero_destinataire']} : {transfert['montant']} F ")
                i=i+1 
    print('Appuyer 0 pour precedent')
    input()
    
def annuler_transfert() :
    global solde_init,solde_init
    
    print('============= ANULLER DE TRANSFERT ===============')
    
    print('')
    while True:
        try:
            try:
                if len(solde_init['list_transfer'])==0:
                    print('Pas de transfert effectuer')
                    break
            except ValueError:
                print('Pas de transfert effectuer')
                break
            i=1
            print('Voici les derniers transfers')
            for transfert in solde_init['list_transfer']:
                print(f" {1} {transfert['numero_destinataire']} : {transfert['montant']} F")  
            dernier_transfert = solde_init['list_transfer'][-1]
            print(f"Votre dernier transfert {dernier_transfert['numero_destinataire'] } : {dernier_transfert['montant']}")
            print('Veuillez mettre 1 pour Annuler ce transfert ou 0 pour precedent')

            confirmation = input('Saisir 1  : ')

            if confirmation == '0'  :
                print("Vous avez decidez de quitter le transfert")
                print("Redirection vers le menu Orange Money")
                break
            elif confirmation=='1':
                if verifiermdp("l annulation transfert") == True:
                    print(f"{dernier_transfert['numero_destinataire'] } : {dernier_transfert['montant']} vient d etre annuler")
                    solde_init['solde'] = solde_init['solde'] + dernier_transfert['montant']
                    
                    solde_init['list_transfer'].pop()
                    sauvegarde()
                    print('Annulation reussi')

                    menu_orange_money()
        except ValueError:
            print('P')
            print('')  
    



def acheter_forfait():
    global solde_init
    global forfaits_acheter
    global list_forfait

    print('============= ACHAT DE FORFAIT ===============')
    print('Appuyer 0 pour precedent')
    print('')
    while True:
        try:
            print('Veuillez mettre le choisir un forfait ou 0 pour precedent')
            
            for forfait in list_forfait:
                print(f"{forfait['id_pass']} {forfait['forfait']} : {forfait['prix']} F")  
            print("0. Pour precedent :")
            print("9. Pour Quitter :")
            print('')

            choix_forfait =int(input('Taper un choix : '))
            
            if choix_forfait == 0  :
                print("Vous avez decidez de quitter le transfert")
                print("Redirection vers le menu Orange Money")
                break

            for forfait in list_forfait:
                if choix_forfait == forfait['id_pass']:
                    prix_pass = forfait['prix']
                    print(f"{forfait['id_pass']} {forfait['forfait']} : {prix_pass} F") 

                    if prix_pass > solde_init['solde'] :
                        print("Solde Insuffisant")
                    elif verifiermdp("forfait") == True:
                        forfaits_acheter.append(forfait)
                        solde_init['solde']= solde_init['solde'] - prix_pass 
                        sauvegarde()
                        print (f"Achat du pass {forfait['forfait']} : {prix_pass} F reussit")
                        print('Votre solde est de ', solde_init['solde'])

               
        except ValueError:
            print('Choix invalide')
            print('')



def effectuer_un_transfert():
    global transfert
    global solde_init
    montant = 0
    while True :
        try:
            
            print('============= TRANSFERT ===============')
            print('Appuyer 0 pour precedent')
            print('')
            while True :
                try:
                    numero_destinataire = input('Saisir le numero a envoyer: ').replace(" ", "")
                    if  numero_destinataire == "0" :
                        print("Vous avez decidez de quitter le transfert")
                        print("Redirection vers le menu Orange Money")
                        menu_orange_money()
                    elif len(numero_destinataire) == 9 :
                        if (numero_destinataire.startswith('77') or numero_destinataire.startswith('78')) and numero_destinataire.isdigit()  :
                            print(f"Le numero saisit est : {numero_destinataire}")
                            break
                    else :
                        print('Saisir Un Numero Valide')
                        print('')
                except ValueError:
                    print('Veullez saisir que des chiffre')
            montant = int(input('Saisir le montant a envoyer '))

            
            
            if montant < 0 :
                print('Donner un montant du transfere doit etre superieur ou egal 0')
            elif montant == 0  :
                print("Vous avez decidez de quitter le transfert")
                print("Redirection vers le menu Orange Money")
                break
            elif montant > solde_init['solde'] :
                print("Solde Insuffisant")
            elif verifiermdp("le transfert") == True:
                solde_init['solde']= solde_init['solde'] - montant
                solde_init['montant_compte'] = solde_init['montant_compte'] + montant 
                
                
                solde_init['transfert'] = {
                    'id': len(solde_init['list_transfer']) + 1,
                    'numero_destinataire' : numero_destinataire,
                    'montant' : montant,
                }
                
                solde_init['list_transfer'].append(solde_init['transfert'])
                sauvegarde()

                print (f"Vous avez effectuer un transfert de : {montant}" )
                print (f"Vers le numeros : {numero_destinataire}"  )
                print(f"Votre nouveaux solde est de {solde_init['solde']} FCFA") 
                break
            else :
                break
        except ValueError:
            print(f"Nombre Invalid")



def acheter_du_crédit():
    global solde_init
    global credit
    print('============= ACHAT DE CREDIT ===============')
    print('Appuyer 0 pour precedent')
    print('')
    while True :
        try:
            print('Veuillez mettre le montant ou 0 pour precedent')

            choix_achat = int(input('Saisir le montant : '))
            if choix_achat < 0 :
                print('Donner un montant superieur a 0')
            elif choix_achat == 0:
                print("Vous avez decidez de quitter l'achat de credit")
                print("Redirection vers le menu Orange Money")
                break
            elif choix_achat > solde_init['solde'] :
                print("Solde Insuffisant")
            elif verifiermdp("l'achat") == True:
                credit = credit + choix_achat 
                solde_init['solde']= solde_init['solde'] -choix_achat 
                sauvegarde()
                
                print ('achat effectue', choix_achat)
                print('Votre solde est de ', solde_init['solde']) 

                return credit ,solde_init['solde']
            else :
                break
                
        except ValueError:
            print('Nombre invalide')
            print('')


def verifiermdp(nom_service):
    global solde_init
    tentative_consulter=3
    while True :
        print('Veuillez mettre votre Code secret ou 0 pour precedent')
        mdp = input('Saisir le votre code secret : ').replace(" ", "")
        
        if mdp=='0':
            print(f"Vous avez decidez de quitter {nom_service}")
            print("Redirection vers le menu Orange Money")
            menu_orange_money()

        elif mdp != solde_init['mot_de_passe'] and tentative_consulter > 1:
            print('Code Incorect')
            tentative_consulter = tentative_consulter - 1 
            print(f"Il vous reste {tentative_consulter}")          
        elif mdp == solde_init['mot_de_passe'] :
            
            return True
            
        else:
            print('Trop de tentative ')
            break


def consulter_solde():
    global solde_init
    print('============= CONSULTATION DU SOLDE ===============')
    print('Appuyer 0 pour quitter')
    print('')
    if verifiermdp('la consultation') == True:
        print(f"Votre solde est de : {solde_init['solde']} Fcfa")
    
    
def menu_orange_money():
    
    print('============= MENU ORANGE MENU ===============')
    print('')
    while True:
        fetch_data()
        print("1. Pour consulter le solde :")
        print("2. Pour acheter du credit :")
        print("3. Pour effecter un transfert :")
        print("4. Pour acheter un forfait :")
        print("5. Pour annuler un transfert :")
        print("6. Pour  l'historique :")
        print("7. Pour  annuler un transfert par ID  :")
        print("0. Pour precedent :")
        print("9. Pour Quitter :")
        
        choix=input('Taper un choix : ').replace(" ", "")

        if choix =='1' :
            consulter_solde()
        elif choix =='2':
            acheter_du_crédit()
        elif choix =='3':
            effectuer_un_transfert()
        elif choix =='4':
            acheter_forfait()
        elif choix =='5':
            annuler_transfert()
        elif choix =='6':
            historique()
        elif choix =='7':
            annuler_transfert_par_id()
        elif choix =='8':
            fetch_data()
        elif choix=="9":
            exit()
        elif choix =='0' :
            break
        else:
            print('Choix invalide')






def menu_ussd () :
    print ('============= MENU USSD ===============')
    print('')
    while True:
        
        code_ussd = input('Veuillez taper #144# pour acceder au menu ou 0 pour quitter :').replace(" ", "")
        if code_ussd == '#144#' :
            menu_orange_money()
        elif code_ussd=='0':
            print('Merci et A bientot ')
            break
        else :
            print('Veuillez taper #144# pour acceder au menu ou 0 pour quitter')


def main ():
    menu_ussd()


main()