#!/usr/bin/python
import cgi
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'yarabbitsahal'
database = 'postgres'

Requete="select r.num_client,c.nom,c.prenom,r.num_menu ,count(r.num_menu) AS nombre_menu_par_client from luxiours_camping.client c , luxiours_camping.reservation_menu r where c.num_client = r.num_client group by r.num_client,c.nom,c.prenom,r.num_menu "

# Simple routine to run a query on a database and print the results:

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

cur = conn.cursor()

cur.execute( Requete )

page = """
    <!doctype html>
    <html lang="fr">
		<head>
			<meta charset="utf-8">
			<title>Liste des menu</title>
		</head>
		<body background="images/fond.jpg">
		<center><div class="principale" style="background-image:url(images/blanc.png); width: 700px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
               </br>
               <h1>nombre de menu par client </h1>
               <form action="stats.py" method="">
					<input type="submit" value="Retour" />
	       </br></br></br>
            <table border="1" cellpadding="5">
                <tr>
                    <td>num_client</td>
                    <td>nom</td>
                    <td>prenom</td>
                    <td>nom_menu</td>
                    <td>nombre de menu par client</td>
                </tr>""" 
                
print(page)
    
for num_client,nom,prenom,nombre_menu_par_client in cur.fetchall() :
   print (     """<tr>
                    <td>""", num_client , """</td>
                    <td>""", nom , """</td>
                    <td>""", prenom, """</td>
                    <td>""", nom_menu, """</td>
                    <td>""", nombre_menu_par_client, """</td>
                    </tr>""")
                    

page3 = """</table></br></br></br>
            

         </center></div>
        
        
			</form><BR>
        
        </body>
    </html>"""



print(page3)


conn.close()
