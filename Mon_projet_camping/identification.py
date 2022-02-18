# coding: utf-8

import cgi

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Identification</title>
                </head>
                <body background="images/fond.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 550px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Identification</h1>
                		</br>
                		<p>mettre les infos</p>
                		</br>
                        	<form action="insert_client.py" method="POST">
                                <label>Num_Client</label> : <input type="text" name="num_client" /><BR>
                                        <label>Nom</label> : <input type="text" name="nom" /><BR>
                                        <label>Prenom</label> : <input type="text" name="prenom" /><BR>
                                        <label>Sexe</label> : <input type="text" name="sexe" /><BR>
                                        <label>Age</label> : <input type="text" name="age" /><BR>
                                        <label>nb_personne</label> : <input type="text" name="nb_personne" /><BR>
                                        <input type="submit" value="Valider" />
                                </form>
                                        </br></br></br>
                             <form action="inscriptions.py" method="">
                			<input type="submit" value="Retour" />
                            </form>
                            
						</br></br></br>



                	</center></div>
                </body>





	</html>"""
print(Page)
