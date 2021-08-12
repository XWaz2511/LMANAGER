#! /usr/local/bin/python3

import os
from posixpath import commonpath, split  
from time import *
import re

headerBar = """
 ██▓     ███▄ ▄███▓ ▄▄▄       ███▄    █  ▄▄▄        ▄████ ▓█████  ██▀███  
▓██▒    ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ▒████▄     ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒██░    ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
▒██░    ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░██████▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░ ▒░▓  ░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░ ▒  ░░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
  ░ ░   ░      ░     ░   ▒      ░   ░ ░   ░   ▒   ░ ░   ░    ░     ░░   ░ 
    ░  ░       ░         ░  ░         ░       ░  ░      ░    ░  ░   ░     

        By XWaz.
                                                                          
"""

os.system("clear")
print("ET C'EST PARTIIIII !")
sleep(1)
os.system("clear")

print(headerBar)
sleep(1)
print("LMANAGER se lance...\n\n")

def displayDocumentation():
    print("""[1]: Exécute les commandes sudo apt update, sudo apt dist-upgrade et sudo apt autoclean;\n\n
             [2]: Renomme le fichier /etc/resolv.conf (non modifiable) en /etc/resolv.conf.disabled puis crée un nouveau fichier resolv.conf (modifiable), modifié pour répondre à vos besoins;\n\n""")


def updateDistro():
    os.system("sudo apt update")
    os.system("sudo apt dist-upgrade")
    os.system("sudo apt autoclean")
    print("\n\n")


def changeDNS():
    numberOfDNSs = input("Combien de serveurs DNS souhaitez-vous utiliser (il est recommendé d'en utiliser au moins 2, au cas où un soit down) ?\n\n")
    filesInEtc = os.listdir("/etc/")
    fileContent = list()

    for i in range(1, int(numberOfDNSs)+1):
        dns = input("Veuillez entrer le DNS numéro {}: ".format(str(i)) + "\n")
        tempDNS = "nameserver {}\n".format(str(dns))
        fileContent.append(str(tempDNS))
    
    if "resolv.conf.disabled" in filesInEtc:
        if "resolv.conf" in filesInEtc:
            os.system("sudo rm /etc/resolv.conf")
            file = open("/etc/resolv.conf", 'x')
            file.close()
            for DNS in fileContent:
                file = open("/etc/resolv.conf", 'a')
                file.write(str(DNS))
                file.close()
        else:
            file = open("/etc/resolv.conf", 'x')
            file.close()
            for DNS in fileContent:
                file = open("/etc/resolv.conf", 'a')
                file.write(str(DNS))
                file.close()
    else:
        if "resolv.conf" in filesInEtc:
            os.system("sudo mv /etc/resolv.conf /etc/resolv.conf.disabled")
            file = open("/etc/resolv.conf", 'x')
            file.close()
            for DNS in fileContent:
                file = open("/etc/resolv.conf", 'a')
                file.write(str(DNS))
                file.close()
        else:
            file = open("/etc/resolv.conf", 'x')
            file.close()
            for DNS in fileContent:
                file = open("/etc/resolv.conf", 'a')
                file.write(str(DNS))
                file.close()

    print("\nDNS changé avec succès !!!\n")


def createUser():
    username = str(input("Quel est le nom de l'utilisateur que vous souhaitez créer ?\n\n"))
    usergroupChoice = str(input("Voulez-vous que l'utilisateur puisse utiliser la commande sudo ou non ? [O;N]\n\n"))
    while True:
        if usergroupChoice != "o" and usergroupChoice != "O" and usergroupChoice != "n" and usergroupChoice != "N":
            print("\nVeuillez répondre par O (pour oui) ou N (pour non) !\n\n")
            usergroupChoice = str(input("Voulez-vous que l'utilisateur {} puisse utiliser la commande sudo ou non ? [O;N]\n\n".format(username)))
            continue
        else:
            usergroupChoice = usergroupChoice.lower()
            if usergroupChoice == "o":
                usergroupChoice = True
                print("Très bien. L'utilisateur {} pourra utiliser la commande sudo !".format(username))
                break
            else:
                usergroupChoice = False
                print("Très bien. L'utilisateur {} ne pourra pas utiliser la commande sudo !".format(username))
                break

    userPasswordChoice = str(input("Voulez-vous créer un mot de passe pour l'utilisateur ? [O;N]\n\n"))
    while True:
        if userPasswordChoice != "o" and userPasswordChoice != "O" and userPasswordChoice != "n" and userPasswordChoice != "N":
            print("\nVeuillez répondre par O (pour oui) ou N (pour non) !\n\n")
            userPasswordChoice = str(input("Voulez-vous créer un mot de passe pour l'utilisateur ? [O;N]\n\n"))
            continue
        else:
            userPasswordChoice = userPasswordChoice.lower()
            if userPasswordChoice == "o":
                userPasswordChoice = True
                break
            else:
                userPasswordChoice = False
                break

    if usergroupChoice == True and userPasswordChoice == True:
        os.system("sudo adduser {}".format(username))
        os.system("sudo adduser {} sudo".format(username))
        print("\nUtilisateur crée avec succès !\n\n")
    elif usergroupChoice == True and userPasswordChoice == False:
        os.system("sudo adduser --disabled-password {}".format(username))
        os.system("sudo adduser {} sudo".format(username))
        print("\nUtilisateur crée avec succès !\n\n")
    elif usergroupChoice == False and userPasswordChoice == True:
        os.system("sudo adduser {}".format(username))
        print("\nUtilisateur crée avec succès !\n\n")
    elif usergroupChoice == False and userPasswordChoice == False:
        os.system("sudo adduser --disabled-password {}".format(username))
        print("\nUtilisateur crée avec succès !\n\n")


def createGroup():
    groupname = str(input("Quel est le nom du groupe que vous souhaitez crée ?\n\n"))
    os.system("sudo addgroup {}".format(groupname))
    print("\nGroupe {} crée avec succès !\n\n".format(groupname))


def changeUserPassword():
    username = str(input("Quel est le nom de l'utilisateur dont vous souhaitez modifier le mot de passe ?\n\n"))
    os.system("sudo passwd {}".format(username))
    print("\nLe mot de passe de l'utilisateur {} a été changé avec succès !\n\n".format(username))


def deleteUser():
    username = str(input("Quel est le nom de l'utilisateur que vous souhaitez supprimer ?\n\n"))
    os.system("sudo deluser {}".format(username))
    os.system("sudo rm -d -r /home/{}".format(username))
    print("\nL'utilisateur {} a bien été supprimé.\n\n".format(username))


def deleteGroup():
    groupname = str(input("Quel est le nom du groupe que vous souhaitez supprimer ?\n\n"))
    os.system("sudo delgroup {}".format(groupname))
    print("\nLe groupe {} a bien été supprimé.\n\n".format(groupname))


def chmod():
    filePath = input("Veuillez indiquer le fichier dont les autorisations sont à modifier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n")
    while True:
        try:
            filePath = str(filePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès et un fichier existant correct !\n\n".format(filePath))
            sleep(1)
            filePath = str(input("Veuillez indiquer le fichier dont les autorisations sont à modifier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
            continue
        else:
            if os.path.exists(filePath):
                break
            else:
                print("Le fichier {} n'existe pas ! Veuillez indiquer un chemin d'accès et un fichier existant correct !\n\n".format(filePath))
                sleep(1)
                filePath = str(input("Veuillez indiquer le fichier dont les autorisations sont à modifier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
                continue

    authorizationForOwner = input("Voulez-vous que le propriétaire du fichier ait les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
    while True:
        try:
            authorizationForOwner = str(authorizationForOwner)
        except ValueError:
            print("Vous devez répondre par r, w, x ou par une combinaison de ces lettres !!!\n\n")
            sleep(1)
            authorizationForOwner = input("Voulez-vous que le propriétaire du fichier ait les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
            continue
        else:
            if re.search("[xwr]+", authorizationForOwner):
                break
            else:
                print("Vous devez répondre par r, w, x ou par une combinaison de ces lettres !!!\n\n")
                sleep(1)
                authorizationForOwner = input("Voulez-vous que le propriétaire du fichier ait les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
                continue

    authorizationForGroupMembers = input("Voulez-vous que les membres du groupe du propriétaire du fichier aient les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
    while True:
        try:
            authorizationForGroupMembers = str(authorizationForGroupMembers)
        except ValueError:
            print("Vous devez répondre par r, w, x ou par une combinaison de ces lettres !!!\n\n")
            sleep(1)
            authorizationForGroupMembers = input("Voulez-vous que les membres du groupe du propriétaire du fichier aient les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
            continue
        else:
            if re.search("[xwr]+", authorizationForGroupMembers):
                break
            else:
                print("Vous devez répondre par r, w, x ou par une combinaison de ces lettres !!!\n\n")
                sleep(1)
                authorizationForGroupMembers = input("Voulez-vous que les membres du groupe du propriétaire du fichier aient les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
                continue

    authorizationForAllOtherUsers = input("Voulez-vous que les utilisateurs n'étant ni le propriétaire du fichier ni membres du groupe du propriétaire du fichier aient les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
    while True:
        try:
            authorizationForAllOtherUsers = str(authorizationForAllOtherUsers)
        except ValueError:
            print("Vous devez répondre par r, w, x ou par une combinaison de ces lettres !!!\n\n")
            sleep(1)
            authorizationForAllOtherUsers = input("Voulez-vous que les utilisateurs n'étant ni le propriétaire du fichier ni membres du groupe du propriétaire du fichier aient les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
            continue
        else:
            if re.search("[xwr]+", authorizationForAllOtherUsers):
                break
            else:
                print("Vous devez répondre par r, w, x ou par une combinaison de ces lettres !!!\n\n")
                sleep(1)
                authorizationForAllOtherUsers = input("Voulez-vous que les utilisateurs n'étant ni le propriétaire du fichier ni membres du groupe du propriétaire du fichier aient les droits:\n\t-De lecture du fichier (répondre par r)\n\t-D'écriture du fichier (répondre par w);\n\t-D'exécution du fichier (répondre par x);\n\nVeuillez indiquer votre choix (vous pouvez indiquer plusieurs lettres. Exemple: xw): \n\n")
                continue

    os.system("sudo chmod u={}, g={}, o={} {}".format(authorizationForOwner, authorizationForGroupMembers, authorizationForAllOtherUsers, filePath))
    print("\nAutorisations du fichier changées avec succès !\n\n")


def modifyUserName():
    currentUserName = input("Quel est le nom de l'utilisateur dont vous souhaitez changer le nom ?\n\n")
    while True:
        try:
            currentUserName = str(currentUserName)
        except ValueError:
            print("Ce champ ne peut être vide !\n\n")
            sleep(1)
            currentUserName = input("Quel est le nom de l'utilisateur dont vous souhaitez changer le nom ?\n\n")
            continue
        else:
            if re.search("[^a-z0-9]", currentUserName):
                print("Ce nom d'utilisateur est invalide ! Il ne peut comporter que des lettres minuscules ou des chiffres !\n\n")
                sleep(1)
                currentUserName = input("Quel est le nom de l'utilisateur dont vous souhaitez changer le nom ?\n\n")
                continue
            else:
                break

    newUsername = input("Quel nouveau nom souhaitez vous attribuer à l'utilisateur {} ?\n\n".format(currentUserName))
    while True:
        try:
            newUsername = str(newUsername)
        except ValueError:
            print("Ce champ ne peut être vide !\n\n")
            sleep(1)
            newUsername = input("Quel nouveau nom souhaitez vous attribuer à l'utilisateur {} ?\n\n".format(currentUserName))
            continue
        else:
            if re.search("[^a-z0-9]", newUsername):
                print("Ce nom d'utilisateur est invalide ! Il ne peut comporter que des lettres minuscules ou des chiffres !\n\n")
                sleep(1)
                newUsername = input("Quel nouveau nom souhaitez vous attribuer à l'utilisateur {} ?\n\n".format(currentUserName))
                continue
            else:
                break

    os.system("sudo usermod -l {} {}".format(currentUserName, newUsername))
    print("Utilisateur {} changé en {} avec succès !\n\n".format(currentUserName, newUsername))


def modifyUserPersonalDirectory():
    personalDirectory = input("Veuillez indiquer un chemin absolu vers un dossier vide existant qui servira de nouveau répertoire personnel à l'utilisateur:\n\n")
    while True:
        try:
            personalDirectory = str(personalDirectory)
        except ValueError:
            print("Ce champ ne peut être vide ! Veuillez indiquer un chemin absolu vers un dossier vide existant !\n\n")
            sleep(1)
            personalDirectory = input("Veuillez indiquer un chemin absolu vers un dossier vide existant qui servira de nouveau répertoire personnel à l'utilisateur:\n\n")
            continue
        else:
            if os.path.exists(personalDirectory):
                break
            else:
                print("Le dossier {} n'existe pas ! Veuillez indiquer un chemin absolu vers un dossier vide existant !\n\n".format(personalDirectory))
                sleep(1)
                personalDirectory = input("Veuillez indiquer un chemin absolu vers un dossier vide existant qui servira de nouveau répertoire personnel à l'utilisateur:\n\n")
                continue
            
    userChoice = input("Voulez-vous cloner votre répertoire actuel dans le nouveau ? [O;N]\n\n")
    while True:
        try:
            userChoice = str(userChoice).lower()
        except ValueError:
            print("Ce champ ne peut ni être vide ni rempli avec des chiffres ! Veuillez répondre par o pour oui ou n pour non uniquement !\n\n")
            sleep(1)
            userChoice = input("Voulez-vous cloner votre répertoire actuel dans le nouveau ? [O;N]\n\n")
            continue
        else:
            if re.search("[on]", userChoice):
                break
            else:
                print("Veuillez répondre par o pour oui ou n pour non uniquement !\n\n")
                sleep(1)
                userChoice = input("Voulez-vous cloner votre répertoire actuel dans le nouveau ? [O;N]\n\n")
                continue

    if userChoice == "o":
        os.system("sudo usermod -dm {}".format(personalDirectory))
    else:
        os.system("sudo usermod -d {}".format(personalDirectory))


def addUserInGroup():
    userName = input("Quel est le nom de l'utilisateur que vous souhaitez ajouter à un groupe ?\n\n")
    while True:
        try:
            userName = str(userName)
        except ValueError:
            print("Veuillez entrer un nom d'utilisateur valide !\n\n")
            sleep(1)
            userName = input("Quel est le nom de l'utilisateur que vous souhaitez ajouter à un groupe ?\n\n")
            continue
        else:
            if re.search("[^a-z0-9]", userName):
                print("Veuillez entrer un nom d'utilisateur valide (uniquement des lettres minuscules et des chiffres) !\n\n")
                sleep(1)
                userName = input("Quel est le nom de l'utilisateur que vous souhaitez ajouter à un groupe ?\n\n")
                continue
            else:
                break

    groupName = input("Quel est le nom du groupe où vous voulez ajouter l'utilisateur ?\n\n")
    while True:
        try:
            groupName = str(groupName)
        except ValueError:
            print("Veuillez entrer un nom de groupe valide !\n\n")
            sleep(1)
            groupName = input("Quel est le nom du groupe où vous voulez ajouter l'utilisateur ?\n\n")
            continue
        else:
            if re.search("[^a-z0-9]", groupName):
                print("Veuillez entrer un nom de groupe valide (uniquement des lettres minuscules et des chiffres) !\n\n")
                sleep(1)
                groupName = input("Quel est le nom du groupe où vous voulez ajouter l'utilisateur ?\n\n")
                continue
            else:
                break

    os.system("sudo adduser {} {}".format(userName, groupName))
    print("L'utilisateur {} a été ajouté au groupe {} avec succès !\n\n".format(userName, groupName))


def findFile():
    choiceOfResearch = input("Souhaitez-vous effectuer une recherche de dossier ou fichier simple (rapide mais assez peu précise) ou plus complète (plus précise, mais demande plus d'arguments et plus lente) ? [1;2]\n\n")
    
    while True:
        try:
            choiceOfResearch = int(choiceOfResearch)
        except ValueError:
            print("veuillez répondre par 1 ou 2 et non par du vide ou une lettre !\n\n")
            sleep(1)
            choiceOfResearch = input("Souhaitez-vous effectuer une recherche de dossier ou fichier simple (rapide mais assez peu précise) ou plus complète (plus précise, mais demande plus d'arguments et plus lente) ? [1;2]\n\n")
            continue
        else:
            if choiceOfResearch != 1 and choiceOfResearch != 2:
                print("veuillez répondre par 1 ou 2 uniquement !\n\n")
                sleep(1)
                choiceOfResearch = input("Souhaitez-vous effectuer une recherche de dossier ou fichier simple (rapide mais assez peu précise) ou plus complète (plus précise, mais demande plus d'arguments et plus lente) ? [1;2]\n\n")
                continue
            else:
                break

    if choiceOfResearch == 1:
        fileName = input("Quel est le nom du fichier ou dossier que vous souhaitez rechercher ? Soyez le plus précis possible (exemples: exemple.txt, exemplededossier sont suffisants, mais /tmp/exemple.txt ou /bin/exemplededossier sont mieux).\n\n")
        while True:
            try:
                fileName = str(fileName)
            except ValueError:
                print("Veuillez entrer un nom de dossier ou de fichier valide !\n\n")
                sleep(1)
                fileName = input("Quel est le nom du fichier ou dossier que vous souhaitez rechercher ? Soyez le plus précis possible (exemples: exemple.txt, exemplededossier sont suffisants, mais /tmp/exemple.txt ou /bin/exemplededossier sont mieux).\n\n")
                continue
            else:
                break

        os.system("sudo apt get install locate")
        os.system("sudo updatedb")
        print("\nlancement de la recherche...\n\n")
        os.system("sudo locate {}".format(fileName))
    else:
        fileName = input("Quel est le nom du fichier ou dossier que vous souhaitez rechercher ? Soyez le plus précis possible (exemples: exemple.txt, exemplededossier)\n\n")
        while True:
            try:
                fileName = str(fileName)
            except ValueError:
                print("Veuillez entrer un nom de dossier ou de fichier valide !\n\n")
                sleep(1)
                fileName = input("Quel est le nom du fichier ou dossier que vous souhaitez rechercher ? (exemples: exemple.txt, exemplededossier)\n\n")
                continue
            else:
                break
        
        path = input("Quel est le répertoire le plus précis possible contenant l'élément que vous recherchez (l'écrire sous ce format: ./dossier) ? Si vous ne savez pas, taper './'.\n\n")
        while True:
            try:
                path = str(path)
            except ValueError:
                print("Veuillez entrer répertoire valide dans le format indiqué !\n\n")
                sleep(1)
                path = input("Quel est le répertoire le plus précis possible contenant l'élément que vous recherchez (l'écrire sous ce format: ./dossier) ? Si vous ne savez pas, taper './'.\n\n")
                continue
            else:
                break

        os.system("find {} -f {}".format(path, fileName))


def copyDistantFile():
    urlPath = input("Veuillez indiquer l'url complet du fichier que vous voulez copier (exemple: https://exempledesite/exemple/exemple.txt)\n\n")
    while True:
        try:
            urlPath = str(urlPath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un url complet correct !\n\n".format(urlPath))
            sleep(1)
            urlPath = str(input("Veuillez indiquer l'url complet du fichier que vous voulez copier (exemple: https://exempledesite/exemple/exemple.txt)\n\n"))
            continue
        else:
            break

    os.system("wget {}".format(urlPath))


def unzipFile():
    path = input("Veuillez indiquer quel est l'archive à décompresser ainsi que son chemin d'accès complet depuis le root:\n\n")
    while True:
        try:
            path = str(path)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à une archive existante correct !\n\n".format(path))
            sleep(1)
            path = input("Veuillez indiquer quel est l'archive à décompresser ainsi que son chemin d'accès complet depuis le root:\n\n")
            continue
        else:
            if os.path.exists(path):
                break
            else:
                print("L'archive {} n'existe pas ! Veuillez indiquer un chemin d'accès à une archive existante correct !\n\n".format(path))
                sleep(1)
                path = input("Veuillez indiquer quel est l'archive à décompresser ainsi que son chemin d'accès complet depuis le root:\n\n")
                continue

    os.system("sudo tar -czvf {}".format(path))


def zipFile():
    path = input("Veuillez indiquer quel est le dossier ou fichier à compresser ainsi que son chemin d'accès complet depuis le root:\n\n")
    while True:
        try:
            path = str(path)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(path))
            sleep(1)
            path = input("Veuillez indiquer quel est le dossier ou fichier à compresser ainsi que son chemin d'accès complet depuis le root:\n\n")
            continue
        else:
            if os.path.exists(path):
                break
            else:
                print("Le fichier ou dossier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(path))
                sleep(1)
                path = input("Veuillez indiquer quel est le dossier ou fichier à compresser ainsi que son chemin d'accès complet depuis le root:\n\n")
                continue

    os.system("sudo tar -czv {}".format(path))


def seeDocumentContent():
    filePath = input("Veuillez indiquer le fichier dont vous voulez voir le contenu ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n")
    while True:
        try:
            filePath = str(filePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un fichier existant correct !\n\n".format(filePath))
            sleep(1)
            filePath = str(input("Veuillez indiquer le fichier dont vous voulez voir le contenu ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
            continue
        else:
            if os.path.exists(filePath):
                break
            else:
                print("Le fichier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un fichier existant correct !\n\n".format(filePath))
                sleep(1)
                filePath = str(input("Veuillez indiquer le fichier dont vous voulez voir le contenu ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
                continue

    os.system("cat {}".format(filePath))


def seeCommandPurpose():
    commandName = input("De quelle commande voulez-vous voir le but ?\n\n")

    while True:
        try:
            commandName = str(commandName)
        except ValueError:
            print("veuillez entrer un nom de commande valide !\n\n")
            sleep(1)
            commandName = input("De quelle commande voulez-vous voir le but ?\n\n")
            continue
        else:
            break

    os.system("whatis {}\n\n".format(commandName))


def seeCommandUsage():
    commandName = input("De quelle commande voulez-vous voir la documentation ?\n\n")

    while True:
        try:
            commandName = str(commandName)
        except ValueError:
            print("veuillez entrer un nom de commande valide !\n\n")
            sleep(1)
            commandName = input("De quelle commande voulez-vous voir la documentation ?\n\n")
            continue
        else:
            break

    os.system("man {}".format(commandName))


def moveFile():
    filePath = input("Veuillez indiquer le fichier ou dossier à déplacer ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n")
    while True:
        try:
            filePath = str(filePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(filePath))
            sleep(1)
            filePath = str(input("Veuillez indiquer le fichier ou dossier à déplacer ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
            continue
        else:
            if os.path.exists(filePath):
                break
            else:
                print("Le fichier ou dossier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(filePath))
                sleep(1)
                filePath = str(input("Veuillez indiquer le fichier ou dossier à déplacer ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
                continue

    destinationPath = input("Veuillez indiquer le dossier de destination ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier)\n\n")
    while True:
        try:
            destinationPath = str(destinationPath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un dossier existant correct !\n\n".format(destinationPath))
            sleep(1)
            destinationPath = str(input("Veuillez indiquer le dossier de destination ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier)\n\n"))
            continue
        else:
            if os.path.exists(destinationPath):
                break
            else:
                print("Le dossier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un dossier existant correct !\n\n".format(destinationPath))
                sleep(1)
                destinationPath = str(input("Veuillez indiquer le dossier de destination ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier)\n\n"))
                continue

    os.system("sudo mv {} {}".format(filePath, destinationPath))
    print("{} déplacé à {} avec succès !\n\n".format(filePath, destinationPath))


def copyFile():
    filePath = input("Veuillez indiquer le fichier ou dossier à copier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n")
    while True:
        try:
            filePath = str(filePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(filePath))
            sleep(1)
            filePath = str(input("Veuillez indiquer le fichier ou dossier à copier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
            continue
        else:
            if os.path.exists(filePath):
                break
            else:
                print("Le fichier ou dossier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(filePath))
                sleep(1)
                filePath = str(input("Veuillez indiquer le fichier ou dossier à copier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
                continue

    destinationPath = input("Veuillez indiquer le dossier de destination ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier)\n\n")
    while True:
        try:
            destinationPath = str(destinationPath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un dossier existant correct !\n\n".format(destinationPath))
            sleep(1)
            destinationPath = str(input("Veuillez indiquer le dossier de destination ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier)\n\n"))
            continue
        else:
            if os.path.exists(destinationPath):
                break
            else:
                print("Le dossier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un dossier existant correct !\n\n".format(destinationPath))
                sleep(1)
                destinationPath = str(input("Veuillez indiquer le dossier de destination ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier)\n\n"))
                continue

    os.system("sudo cp {} {}".format(filePath, destinationPath))
    print("{} copié à {} avec succès !\n\n".format(filePath, destinationPath))


def renameFile():
    filePath = input("Veuillez indiquer le fichier ou dossier dont le nom est à modifier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n")
    while True:
        try:
            filePath = str(filePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(filePath))
            sleep(1)
            filePath = str(input("Veuillez indiquer le fichier ou dossier dont le nom est à modifier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
            continue
        else:
            if os.path.exists(filePath):
                break
            else:
                print("Le fichier ou dossier {} n'existe pas ! Veuillez indiquer un chemin d'accès à un fichier ou dossier existant correct !\n\n".format(filePath))
                sleep(1)
                filePath = str(input("Veuillez indiquer le fichier ou dossier dont le nom est à modifier ainsi que son chemin d'accès complet depuis le root (exemple: ~/home/exempledutilisateur/Bureau/exemplededossier/exemple.txt)\n\n"))
                continue

    newFileName = input("Quel nouveau nom souhaitez-vous donner au fichier ou dossier (n'oubliez pas l'extension si c'est un fichier) ?\n\n")
    while True:
        try:
            newFileName = str(newFileName)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuilez entrer un nom valide.\n\n")
            sleep(1)
            newFileName = input("Quel nouveau nom souhaitez-vous donner au fichier ou dossier (n'oubliez pas l'extension si c'est un fichier) ?\n\n")
            continue
        else:
            break

    newFileNameList = list()
    newFileNameList = newFileName.split("/")
    del newFileNameList[0]
    newFileNameList[len(newFileNameList) - 1] = newFileName
    newFileName = ''.join(newFileNameList)

    os.system("sudo mv {} {}".format(filePath, newFileName))
    print("{} changé en {} avec succès !\n\n".format(filePath, newFileName))


def seeUsage():
    os.system("sudo apt install htop")
    os.system("sudo htop")


def haltSystem():
    print("Halt va éteindre le système sans le mettre hors tension. Veuillez enregistrer vous assurer que tout votre travail est enregistré.\n\n")
    sleep(3)
    haltOrNot = input("Voulez vous exécuter la commande ? [O;N]\n\n")
    while True:
        if haltOrNot != "o" and haltOrNot != "O" and haltOrNot != "n" and haltOrNot != "N":
            print("\nVeuillez répondre par O (pour oui) ou N (pour non) !\n\n")
            sleep(1)
            haltOrNot = str(input("Voulez vous exécuter la commande ? [O;N]\n\n"))
            continue
        else:
            haltOrNot = haltOrNot.lower()
            if haltOrNot == "o":
                haltOrNot = True
                break
            else:
                haltOrNot = False
                break

    if haltOrNot == True:
        os.system("sudo halt --halt")
    else:
        print("Annulation...\n\n")


def mount():
    volumePath = input("Veuillez indiquer le volume à monter ainsi que son chemin d'accès complet depuis le root (exemple: /dev/sdd1)\n\n")
    while True:
        try:
            volumePath = str(volumePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un volume existant correct !\n\n".format(volumePath))
            sleep(1)
            volumePath = str(input("Veuillez indiquer le volume à monter ainsi que son chemin d'accès complet depuis le root (exemple: /dev/sdd1)\n\n"))
            continue
        else:
            if os.path.exists(volumePath):
                break
            else:
                print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un volume existant correct !\n\n".format(volumePath))
                sleep(1)
                volumePath = str(input("Veuillez indiquer le volume à monter ainsi que son chemin d'accès complet depuis le root (exemple: /dev/sdd1)\n\n"))
                continue

    destinationPath = input("Veuillez indiquer le répertoire cible ainsi que son chemin d'accès complet depuis le root (exemple: /mnt/ma_cle_usb)\n\n")
    while True:
        try:
            destinationPath = str(destinationPath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un répertoire existant correct !\n\n".format(destinationPath))
            sleep(1)
            destinationPath = str(input("Veuillez indiquer le répertoire cible ainsi que son chemin d'accès complet depuis le root (exemple: /mnt/ma_cle_usb)\n\n"))
            continue
        else:
            if os.path.exists(destinationPath):
                break
            else:
                print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un répertoire existant correct !\n\n".format(destinationPath))
                sleep(1)
                destinationPath = str(input("Veuillez indiquer le répertoire cible ainsi que son chemin d'accès complet depuis le root (exemple: /mnt/ma_cle_usb)\n\n"))
                continue

    os.system("sudo mount {} {}".format(volumePath, destinationPath))


def unmount():
    volumePath = input("Veuillez indiquer le volume à démonter ainsi que son chemin d'accès complet depuis le root (exemple: /mnt/ma_cle_usb)\n\n")
    while True:
        try:
            volumePath = str(volumePath)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un volume existant correct !\n\n".format(volumePath))
            sleep(1)
            volumePath = str(input("Veuillez indiquer le volume à démonter ainsi que son chemin d'accès complet depuis le root (exemple: /mnt/ma_cle_usb)\n\n"))
            continue
        else:
            if os.path.exists(volumePath):
                break
            else:
                print("Le champ ne peut pas être vide ! Veuillez indiquer un chemin d'accès à un volume existant correct !\n\n".format(volumePath))
                sleep(1)
                volumePath = str(input("Veuillez indiquer le volume à démonter ainsi que son chemin d'accès complet depuis le root (exemple: /mnt/ma_cle_usb)\n\n"))
                continue

    os.system("sudo umount {}".format(volumePath))


def DiskPartitionTool():
    os.system("sudo parted")


def seeIPAddress():
    os.system("sudo ip address")


def ping():
    target = input("Veuillez entrer une addresse IP ou un nom de domaine:\n\n")
    while True:
        try:
            target = str(target)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un url ou une addresse IP !\n\n".format(target))
            sleep(1)
            target = str(input("Veuillez entrer une addresse IP ou un nom de domaine (exemple: https://www.exemple.com ou 8.8.8.8):\n\n"))
            continue
        else:
            break
    
    print("IMPORTANT: pour stopper le ping, pressez Ctrl + C.")
    sleep(3)
    os.system("ping {}".format(target))


def tracePaquetRoute():
    target = input("Veuillez entrer une addresse IP ou un nom de domaine:\n\n")
    while True:
        try:
            target = str(target)
        except ValueError:
            print("Le champ ne peut pas être vide ! Veuillez indiquer un url ou une addresse IP !\n\n".format(target))
            sleep(1)
            target = str(input("Veuillez entrer une addresse IP ou un nom de domaine (exemple: https://www.exemple.com ou 8.8.8.8):\n\n"))
            continue
        else:
            break

    os.system("traceroute {}".format(target))       


def enableSwaps():
    os.system("sudo swapon -a")


def disableSwaps():
    os.system("sudo swapoff -a")


def purgeSwaps():
    os.system("sudo swapoff -a && sudo swapon -a")


def displaySysteminformations():
    os.system("sudo uname")


def displayBIOSInformations():
    os.system("sudo dmidecode")


def relaunchLmanager():
    os.system("clear")
    os.system("sudo ./linux_manager.py")


class __main__():
    sleep(1)
    print("Tout est ok ! Bienvenue !\n\n")
    sleep(1)
    
    while True:
        print("""Voici les tâches que vous pouvez effectuer avec LMANAGER:\n\n\t[0] Consulter le fonctionnement des commandes;\n\n\t
            [1] Mettre à jour la distribution et les paquets (il est possible que vous ayez à valider certaines étapes, suivez les instructions);\n\t
            [2] Changer le serveur DNS;\n
            [3] Créer un nouvel utilisateur;\n
            [4] Créer un nouveau groupe d'utilisateurs;\n
            [5] Changer le mot de passe d'un utilisateur;\n
            [6] Supprimer un utilisateur;\n
            [7] Supprimer un groupe d'utilisateurs;\n
            [8] Changer les permissions d'un fichier ou dossier;\n
            [9] Modifier le login d'un utilisateur;\n
            [10] Modifier l'emplacement du répertoire personnel d'un utilisateur\n
            [11] Ajouter un utilisateur dans un groupe d'utilisateurs;\n
            [12] Localiser un fichier ou un dossier;\n
            [13] Copier un fichier depuis un serveur distant sur l'ordinateur;\n
            [14] Décompresser une archive;\n
            [15] Compresser un dossier ou un fichier;\n
            [16] Voir le contenu d'un fichier;\n
            [17] Voir le but d'une commande shell;\n
            [18] Voir le mode d'emploi d'une commande shell;\n
            [19] Déplacer un fichier ou dossier;\n
            [20] Copier un fichier ou dossier;\n
            [21] Renommer un fichier ou dossier;\n
            [22] Voir l'utilisation des composants de l'ordinateur;\n
            [23] Halt le système;\n
            [24] Monter un volume;\n
            [25] Démonter un volume;\n
            [26] Créer, supprimer ou modifier des partitions disque;\n
            [27] Voir les caractéristiques réseau de la machine;\n
            [28] Pinger une addresse IP ou un URL;\n
            [29] Tracer les paquets en fonction d'une addresse IP ou d'un URL;\n
            [30] Activer le swap;\n
            [31] Désactiver le swap;\n
            [32] Purger le swap;\n
            [33] Voir les informations de la machine;\n
            [34] Voir les informations du BIOS;\n
            [35] Relancer lmanager\n""")

        choice = input("Quelle tâche voulez-vous effectuer ? [0-35]\n\n")

        while True:
            while True:
                try:
                    choice = int(choice)
                except ValueError:
                    print("\nLe choix doit être un chiffre compris entre 0 et 35 !!!\n\n")
                    sleep(3)
                    choice = input("\nQuelle tâche voulez-vous effectuer ? [0-35]\n\n")
                    continue
                else:
                    break

            if choice < 0 or choice > 35:
                print("\nLe choix doit être un chiffre compris entre 0 et 35 !!!\n\n")
                sleep(3)
                choice = input("\nQuelle tâche voulez-vous effectuer ? [0-35]\n\n")
                continue
            else:
                break
        
        if choice == 0:
            displayDocumentation()
        elif choice == 1:
            updateDistro()
        elif choice == 2:
            changeDNS()
        elif choice == 3:
            createUser()
        elif choice == 4:
            createGroup()
        elif choice == 5:
            changeUserPassword()
        elif choice == 6:
            deleteUser()
        elif choice == 7:
            deleteGroup()
        elif choice == 8:
            chmod()
        elif choice == 9:
            modifyUserName()
        elif choice == 10:
            modifyUserPersonalDirectory()
        elif choice == 11:
            addUserInGroup()
        elif choice == 12:
            findFile()
        elif choice == 13:
            copyDistantFile()
        elif choice == 14:
            unzipFile()
        elif choice == 15:
            zipFile()
        elif choice == 16:
            seeDocumentContent()
        elif choice == 17:
            seeCommandPurpose()
        elif choice == 18:
            seeCommandUsage()
        elif choice == 19:
            moveFile()
        elif choice == 20:
            copyFile()
        elif choice == 21:
            renameFile()
        elif choice == 22:
            seeUsage()
        elif choice == 23:
            haltSystem()
        elif choice == 24:
            mount()
        elif choice == 25:
            unmount()
        elif choice == 26:
            DiskPartitionTool()
        elif choice == 27:
            seeIPAddress()
        elif choice == 28:
            ping()
        elif choice == 29:
            tracePaquetRoute()
        elif choice == 30:
            enableSwaps()
        elif choice == 31:
            disableSwaps()
        elif choice == 32:
            purgeSwaps()
        elif choice == 33:
            displaySysteminformations()
        elif choice == 34:
            displayBIOSInformations()
        elif choice == 35:
            relaunchLmanager()

        continueOrNot = input("\nVoulez vous effectuer une autre tâche ? [O;N]\n\n")

        while True:
            while True:
                try:
                    continueOrNot = str(continueOrNot)
                except ValueError:
                    print("\nVeuillez répondre par O (pour oui) ou N (pour non) !\n\n")
                    sleep(3)
                    continueOrNot = input("\nVoulez vous effectuer une autre tâche ? [O;N]\n\n")
                    continue
                else:
                    continueOrNot = continueOrNot.lower()
                    break
            
            if continueOrNot != "o" and continueOrNot != "oui" and continueOrNot != "n" and continueOrNot != "non":
                print("\nVeuillez répondre par O (pour oui) ou N (pour non) !\n\n")
                sleep(3)
                continueOrNot = input("\nVoulez vous effectuer une autre tâche ? [O;N]\n\n")
                continue
            else:
                break

        if continueOrNot == "o" or continueOrNot == "oui":
            continue
        else:
            break

    print("\nMerci d'utiliser LMANAGER ! Au revoir !\n\n")
    sleep(3)
    os.system("exit")

"""
{([{([{([{([{([{|}])}])}])}])}])}   
1XXXXXXXXXXXXXX/0\XXXXXXXXXXXXXX1 
3             /000\             3
5            /00000\            5
7           /0000000\           7
9          /000000000\          9
1         /00000000000\         1
3        |000000|000000|        3  
5        |000000|000000|        5
7        |000000|000000|        7
9        |000000|000000|        9
1        |000000|000000|        1
3        |000000|000000|        3
5         \000000\0000/         5
7          \000000\00/          7
9           \000000\/           9 
1           /\000000\           1
3          /00\000000\          3
5         /0000\000000\         5
7        |000000|000000|        7
9        |000000|000000|        9
1        |000000|000000|        1
3        |000000|000000|        3
5        |000000|000000|        5
7        |000000|000000|        7
9         \00000000000/         9
1          \000000000/          1
3           \0000000/           3
5            \00000/            5
7             \000/             7
9XXXXXXXXXXXXXX\0/XXXXXXXXXXXXXX9  
{([{([{([{([{([{|}])}])}])}])}])}
"""