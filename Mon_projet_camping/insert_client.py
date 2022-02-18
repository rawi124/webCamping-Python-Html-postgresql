#!/usr/bin/python
import psycopg2
import cgi

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

requete = """INSERT INTO luxiours_camping.client VALUES ('%s','%s','%s','%s','%s','%s')"""

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
                		<form action="view_client.py" method="">
						<input type="submit" value="Liste des clients" />
						
						</br></br></br>
                                </center></div>
                </body>





	</html>"""
print(Page)

			

# Recuperation des variables du fichier views.py
form = cgi.FieldStorage()

# Variables locales qui permettent de recuperer les valeurs du formulaire
num_client = form["num_client"].value
nom = form["nom"].value
prenom = form["prenom"].value
sexe = form["sexe"].value
age = form["age"].value
nb_personne = form["nb_personne"].value


conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
cur = conn.cursor()
cur.execute( requete % (num_client,nom,prenom,sexe,age,nb_personne))
conn.commit()
cur.close()
conn.close()
