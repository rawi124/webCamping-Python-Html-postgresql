import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT nom_supp,tarif_supp FROM luxiours_camping.supplement"

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
cur = conn.cursor()
cur.execute( Requete )

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Supplement</title>
                </head>
                <body background="images/din.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 550px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>les supplements</h1>
                		</br></br>
                		<form action="listes.py" method="">
						<input type="submit" value="Retour listes" />
						</br></br></br>
				<table border="1" cellpadding="5">
                                <tr>
                                  
                                    <td>nom_supp</td>
                                    <td>tarif_supp</td>
                                </tr>"""
print(Page)
for nom_supp,tarif_supp in cur.fetchall() :

    print (                  """<tr>
                                    <td>""", nom_supp , """</td>
                                    <td>""", tarif_supp , """</td>
                                    </tr>""")

    
page3 =                      """</table>
				    



                	</center></div>
                </body>





	</html>"""
print(Page3)
