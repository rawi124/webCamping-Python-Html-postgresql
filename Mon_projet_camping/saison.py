# coding: utf-8

import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT num_saison,nom_saison,coefficient_majoration FROM luxiours_camping.saison"

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
                <body background="images/campin.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 600px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Saisons de l'annee</h1>
                		</br>
                		<p>selon la saison, les tarifs peuvent etre majores </p>
                		</br>
                		<form action="index.py" method="">
						<input type="submit" value="Accueil" />
						</br></br></br>
				<table border="1" cellpadding="5">
                                <tr>
                                  
                                    <td>num_saison</td>
                                    <td>nom_saison</td>
                                    <td>coefficient_majoration</td>
                                </tr>"""
print(Page)
for num_saison,nom_saison,coefficient_majoration in cur.fetchall() :

    print (                  """<tr>
                                    <td>""", num_saison , """</td>
                                    <td>""", nom_saison , """</td>
                                    <td>""", coefficient_majoration , """</td>
                                    </tr>""")

    
page3 =                      """</table>
				    



                        </br></br></br></br>
                	</div></center>
                </body>
	</html>"""
print(Page3)
