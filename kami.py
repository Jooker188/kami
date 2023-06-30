from dependences.session import *
from dependences.request_utils import *
from dependences.utils import *
from vulns.get_csrf import get_csrf
from colorama import Fore, Style
import os, sys
import platform
from requests.exceptions import MissingSchema

''' ------------------------------------ DESCRIPTION ------------------------------------

Ce fichier contient un affichage d'introduction avec un logo et une version, puis il demande à l'utilisateur de fournir une URL cible et le type de page (connexion, modification ou suppression). 
Ensuite, il effectue des opérations pour vérifier la validité de l'URL, créer un fichier contenant le domaine de l'URL, et exécuter des détections de vulnérabilités CSRF en utilisant la fonction get_csrf du module vulns. 
Enfin, il affiche un message de fin.

'''

############################################### AFFICHAGE INTRO #############################################

if len(sys.argv) > 2 or sys.argv[1] not in ["connexion","change","delete"]:
    print("\nUsage : python kami.py connexion|change|delete")
else:
    #on clear le terminal
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system('clear')

    print(intro.format(
        Fore.GREEN + website + Style.RESET_ALL, 
        Fore.YELLOW + bouddha.strip() + Style.RESET_ALL, 
        Fore.RED + version + Style.RESET_ALL
        ) + "\n")
    
    page_type = sys.argv[1]
    
############################################### CORPS DU PROGRAMME #############################################

    target = input(forme("user") + " Entrez l'URL de la page cible : ")
    session = set_session()

    while True:
        try:
            session.get(target)
            print(forme("info") + " URL Valide ")
            break
        except MissingSchema:
            print(forme("info") + " URL Invalide ")
            target = input(forme("user") + " Entrez l'URL de la page cible : ")

    create_domain_file(target, "logs/url.log")
    vulns = get_csrf(session, target, page_type)
  
############################################### AFFICHAGE FIN #############################################

print(fin)
