# coding: utf-8

import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT num_employe,nom_employe,domaine_activite,salaire_heure,prenom_employe FROM luxiours_camping.employes"

# Simple routine to run a query on a database and print the results:

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

cur = conn.cursor()

cur.execute( Requete )

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>employes</title>
                </head>
                <body background="images/r.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 570px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Nos employes</h1>
                		</br>
                		<form action="activite.py" method="">
						<input type="submit" value="Retour" />
						</br></br></br>
				<table border="1" cellpadding="5">
                                <tr>
                                  
                                    <td>num_employe</td>
                                    <td>nom_employe</td>
                                    <td>domaine_activite</td>
                                    <td>salaire_heure</td>
                                    <td>prenom_employe</td>
                                </tr>"""
print(Page)
for num_employe,nom_employe,domaine_activite,salaire_heure,prenom_employe in cur.fetchall() :

    print (                  """<tr>
                                    <td>""", num_employe , """</td>
                                    <td>""", nom_employe , """</td>
                                    <td>""", domaine_activite , """</td>
                                    <td>""", salaire_heure , """</td>
                                    <td>""", prenom_employe , """</td>
                                    </tr>""")

    
page3 =                      """</table>
				    



                        </br></br></br></br>
                	</div></center>
                </body>
	</html>"""
print(Page3)
