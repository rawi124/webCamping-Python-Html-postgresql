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
                		<h1>Inscription activite</h1>
                		</br>
                		</br>
                        	<form action="insert_activite.py" method="POST">
                                <label>Num_client</label> : <input type="text" name="num_client" /><BR>
                                <label>Nom_activite</label> : <input type="text" name="nom_activite" /><BR>
                                <label>date_activite</label> : <input type="text" name="date_activite" /><BR>
                                                            </br></br></br>

                                        <input type="submit" value="Valider" />
                                </form>
                                        </br></br></br>
                             <form action="reservations.py" method="">
                			<input type="submit" value="Retour" />
                            </form>
                            
						</br></br></br>



                	</center></div>
                </body>





	</html>"""
print(Page)
