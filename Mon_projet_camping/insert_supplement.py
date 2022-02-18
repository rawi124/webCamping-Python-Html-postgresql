#!/usr/bin/python
import psycopg2
import cgi

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

requete = """INSERT INTO luxiours_camping.reservation_supplement VALUES ('%s','%s','%s')"""

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>supplement</title>
                </head>
                <body background="images/fond.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 800px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Enregistrement valide !</h1>
                		</br>
                		<form action="stats.py" method="">
					<input type="submit" value="Retour" />
				</form>
				</br>
                                </center></div>
                </body>





	</html>"""
print(Page)

			

# Recuperation des variables du fichier views.py
form = cgi.FieldStorage()

# Variables locales qui permettent de recuperer les valeurs du formulaire
num_client = form["num_client"].value
nom_supp = form["nom_supp"].value
date_supplement = form["date_supplement"].value 





conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
cur = conn.cursor()
cur.execute( requete % (num_client,nom_supp,date_supplement))
conn.commit()
cur.close()
