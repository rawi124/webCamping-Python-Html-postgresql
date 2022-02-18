#!/usr/bin/python
import psycopg2
import cgi

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

requete = """INSERT INTO luxiours_camping.sejour VALUES ('%s','%s','%s','%s')"""

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>reserver un emplacement</title>
                </head>
                <body background="images/fond.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 800px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Enregistrement valide !</h1>
                		</br>
                		<p>votre inscription a bien fonctionne</p>						
				</br></br></br>
                                </center></div>
                </body>





	</html>"""
print(Page)

			

# Recuperation des variables du fichier views.py
form = cgi.FieldStorage()

# Variables locales qui permettent de recuperer les valeurs du formulaire
num_client = form["num_client"].value
num_emplacement = form["num_emplacement"].value
date_deb_sejour = form["date_deb_sejour"].value
date_fin_sejour = form["date_fin_sejour"].value



conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
cur = conn.cursor()
cur.execute( requete % (num_client,num_emplacement,date_deb_sejour,date_fin_sejour))
conn.commit()
cur.close()
conn.close()
