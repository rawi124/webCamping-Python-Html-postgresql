#!/usr/bin/python
import psycopg2
import cgi

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

requete = """INSERT INTO luxiours_camping.enfant (num_enfant,nom_enfant,prenom_enfant,sexe,age,duree_sejour_enfant,num_client) VALUES ('%s','%s','%s','%s','%s','%s','%s')"""


Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Activites</title>
                </head>
                <body background="images/fond.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 800px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Enregistrement valide !</h1>
                		</br>
                		<p>votre inscription a bien fonctionne</p>
                		</br>
                		<form action="view_enfant.py" method="">
						<input type="submit" value="Liste des enfants" />
						
						</br></br></br>
                                </center></div>
                </body>





	</html>"""
print(Page)

			

# Recuperation des variables du fichier views.py
form = cgi.FieldStorage()

# Variables locales qui permettent de recuperer les valeurs du formulaire
num_enfant = form["num_enfant"].value
nom_enfant = form["nom_enfant"].value
prenom_enfant = form["prenom_enfant"].value
sexe = form["sexe"].value
age = form["age"].value
duree_sejour_enfant = form["duree_sejour_enfant"].value
num_client = form["num_client"].value






conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
cur = conn.cursor()
cur.execute( requete % (num_enfant,nom_enfant,prenom_enfant,sexe,age,duree_sejour_enfant,num_client))
conn.commit()
cur.close()
conn.close()
