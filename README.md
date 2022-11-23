Creer la base de donnée 'Medicaments' en suivant le schéma decrit sur: 'https://base-donnees-publique.medicaments.gouv.fr/docs/Contenu_et_format_des_fichiers_telechargeables_dans_la_BDM_v1.pdf'

Recuperez les donnees sur: https://base-donnees-publique.medicaments.gouv.fr/telechargement.php

(attention aux accents, et cle privées/etrangeres qui peuvent generer des erreurs)

pour que ca fonctionne(en trichant): SET GLOBAL foreign_key_checks=OFF;



FIN:
https://mariadb.com/fr/resources/blog/how-to-connect-python-programs-to-mariadb/
refaire l'interface, python ou bash (en commande line ) qu'on peut trouver sur:  https://base-donnees-publique.medicaments.gouv.fr/index.php


a=input("chercher un medicament par: 'nom/patho/sub'")

if a=='nom':
    input("tapez le nom: ")
    # select
if a=='patho':
    input("tapez la patho")
    # select
if a=='sub':
    input("tabez sub: )
    # select
