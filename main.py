#Lien Github : https://github.com/moussacode/Atelier_13_Python_Simulation_USSD_Orange_Money.git



solde = 3000
mot_de_passe="12345678"
credit = 0
montant_compte=0

def effectuer_un_transfert():
    global montant_compte
    global solde
    montant = 0
    while True :
        try:
            print('=====Effectuer Transfert=====')
            print('Appuyer 0 pour quitter')
            print('')
            while True :
                try:
                    numero_destinataire = input('Saisir le numero a envoyer: ').strip()
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
            elif montant > solde :
                print("Solde Insuffisant")
            elif verifiermdp("le transfert") == True:
                solde= solde - montant
                montant_compte = montant_compte + montant 
                 
                print ('Vous avez effectuer un transfert de : ', montant)
                print ('Vers le numeros : ', numero_destinataire )
                print('Votre nouveaux solde est de ', solde) 
                break
            else :
                break
        except ValueError:
            print('Nombre Invalid')



def acheter_du_crédit():
    global solde
    global credit
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
            elif choix_achat > solde :
                print("Solde Insuffisant")
            elif verifiermdp("l'achat") == True:
                credit = credit + choix_achat 
                solde= solde-choix_achat 
                print ('achat effectue', choix_achat)
                print('Votre solde est de ', solde) 

                return credit ,solde
            else :
                break
                
        except ValueError:
            print('Nombre invalide')
            print('')


def verifiermdp(nom_service):
    tentative_consulter=3
    while True :
        print('Veuillez mettre votre Code secret ou 0 pour precedent')
        mdp = input('Saisir le votre code secret : ').strip()
        
        if mdp=='0':
            print(f"Vous avez decidez de quitter {nom_service}")
            print("Redirection vers le menu Orange Money")
            menu_orange_money()

        elif mdp != mot_de_passe and tentative_consulter > 1:
            print('Code Incorect')
            tentative_consulter = tentative_consulter - 1 
            print(f"Il vous reste {tentative_consulter}")          
        elif mdp == mot_de_passe :
            
            return True
            
        else:
            print('Trop de tentative ')
            break


def consulter_solde():
    global solde

    if verifiermdp('la consultation') == True:
        print(f"Votre solde est de : {solde}")
    
    
def menu_orange_money():
    print('============= MENU ORANGE MENU ===============')
    print('')
    while True:
        print("1. Pour consulter le solde :")
        print("2. Pour acheter du credit :")
        print("3. Pour effecter un transfert :")
        print("0. Pour precedent :")
        print("9. Pour Quitter :")
        
        choix=input('Taper un choix : ').strip()

        if choix =='1' :
            consulter_solde()
        elif choix =='2':
            acheter_du_crédit()
        elif choix =='3':
            effectuer_un_transfert()
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
        
        code_ussd = input('Veuillez taper #144# pour acceder au menu ou 0 pour quitter :').strip()
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