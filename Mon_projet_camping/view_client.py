#!/usr/bin/python
import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete = "SELECT num_client,nom,prenom,sexe,age,nb_personne FROM luxiours_camping.client"

# Simple routine to run a query on a database and print the results:

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

cur = conn.cursor()

cur.execute( Requete )

page = """
    <!doctype html>
    <html lang="fr">
		<head>
			<meta charset="utf-8">
			<title>Liste des clients</title>
		</head>
		<body background="images/fond.jpg">
		<center><div class="principale" style="background-image:url(images/blanc.png); width: 500px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
               </br>
               <h1>Liste des clients</h1>
               <form action="inscriptions.py" method="">
					<input type="submit" value="Retour" />
	       </br></br></br>
            <table border="1" cellpadding="5">
                <tr>
                    <td>num_client</td>
                    <td>nom</td>
                    <td>prenom</td>
                    <td>sexe</td>
                    <td>age</td>
                    <td>nb_personne</td>   

                </tr>""" 
                
print(page)
    
for num_client,nom,prenom,sexe,age,nb_personne in cur.fetchall() :
   print (     """<tr>
                    <td>""", num_client , """</td>
                    <td>""", nom , """</td>
                    <td>""", prenom, """</td>
                    <td>""", sexe, """</td>
                    <td>""", age, """</td>
                    <td>""",nb_personne,"""</td>   

                    </tr>""")
                    

page3 = """</table></br></br></br>
            

         </center></div>
        
        
			</form><BR>
        
        </body>
    </html>"""



print(page3)


conn.close()

        
