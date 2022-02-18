# coding: utf-8

import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT num_emplacement,nom_emplacement,tarif_emplacement FROM luxiours_camping.emplacement"

# Simple routine to run a query on a database and print the results:

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

cur = conn.cursor()

cur.execute( Requete )


Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Emplacements</title>
                </head>
                <body background="images/accueil.jpg" blur>
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 520px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Emplacements</h1>
                		</br>
                		<form action="listes.py" method="">
						<input type="submit" value="Retour listes" />
				</form>
				</br>
                		<form action="saison.py" method="">
						<input type="submit" value="Saisons" />
				</form>
				</br>
                		<table border="1" cellpadding="5">
                                <tr>
                                  
                                    <td>num_emplacement</td>
                                    <td>nom_emplacement</td>
                                    <td>tarif_emplacement</td>   
                                </tr>"""
print(Page)
for num_emplacement,nom_emplacement,tarif_emplacement in cur.fetchall() :

    print (                  """<tr>
                                    <td>""", num_emplacement , """</td>
                                    <td>""", nom_emplacement , """</td>
                                    <td>""", tarif_emplacement , """</td>
                                    </tr>""")

    
page3 =                      """</table>
                                </br>
                		<p>mettre les emplacements</p>
                		</br>                              




                		</br>
                		<form action="index.py" method="">
						<input type="submit" value="Retour" />
						</br></br></br>



                	</center></div>
                </body>





	</html>"""
print(Page3)
