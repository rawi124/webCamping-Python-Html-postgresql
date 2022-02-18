# coding: utf-8

import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT nom_activite,tarif_activite,num_employe FROM luxiours_camping.activite"

# Simple routine to run a query on a database and print the results:

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

cur = conn.cursor()

cur.execute( Requete )

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Activites</title>
                </head>
                <body background="images/paint.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 600px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Activites disponibles</h1>
                		</br>
                		<p>Nous proposons ces activites</p>
                		</br>
                		<form action="listes.py" method="">
						<input type="submit" value="Retour listes" />
				</form>
				</br>
                		<form action="employe.py" method="">
						<input type="submit" value="Employes" />
				</form>
						</br></br></br>
				<table border="1" cellpadding="5">
                                <tr>
                                  
                                    <td>nom_activite</td>
                                    <td>tarif_activite</td>
                                    <td>num_employe</td>
                                </tr>"""
print(Page)
for nom_activite,tarif_activite,num_employe in cur.fetchall() :

    print (                  """<tr>
                                    <td>""", nom_activite , """</td>
                                    <td>""", tarif_activite , """</td>
                                    <td>""", num_employe , """</td>
                                    </tr>""")

    
page3 =                      """</table>
				    



                        </br></br></br></br>
                	</div></center>
                </body>
	</html>"""
print(Page3)
