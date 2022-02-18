# coding: utf-8

import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT num_menu,type_menu,tarif_menu,contenu FROM luxiours_camping.menu"

# Simple routine to run a query on a database and print the results:

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

cur = conn.cursor()

cur.execute( Requete )

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Restaurant</title>
                </head>
                <body background="images/picn.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 550px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Menus disponibles</h1>
                		<p>Notre restaurant vous propose</p>
                		</br>
                		<form action="listes.py" method="">
						<input type="submit" value="Retour listes" />
						</br></br>
				<table border="1" cellpadding="5">
                                <tr>
                                  
                                    <td>num_menu</td>
                                    <td>type_menu</td>
                                    <td>tarif_menu</td>
                                    <td>contenu</td>
                                </tr>"""
print(Page)
for num_menu,type_menu,tarif_menu,contenu in cur.fetchall() :

    print (                  """<tr>
                                    <td>""", num_menu , """</td>
                                    <td>""", type_menu , """</td>
                                    <td>""", tarif_menu , """</td>
                                    <td>""", contenu , """</td>
                                    </tr>""")

    
page3 =                      """</table>
				    



                	</center></div>
                </body>





	</html>"""
print(Page3)
