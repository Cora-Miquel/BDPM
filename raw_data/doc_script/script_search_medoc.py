# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="BDPM"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


a=input("chercher un medicament par: 'nom/patho/sub'")

if a=='nom':
    nom=input("tapez le nom: ")
    SELECT Denom, Forme, Voies_admin, Denom_substance FROM CIS_bdpm A JOIN CIS_COMPO B ON A.Code_CIS=B.Code_CIS WHERE Denom='+nom+'  
if a=='patho':
    input("tapez la patho")
    # select
if a=='sub':
    input("tabez sub: )
    # select
