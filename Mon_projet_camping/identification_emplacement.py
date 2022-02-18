# coding: utf-8

import cgi

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>reserver un emplacement</title>
                </head>
                <body background="images/fond.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 550px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>reserver un emplacement</h1>
                		</br>
                		</br>
                        	<form action="insert_emplacement.py" method="POST">
                                <label>Num_client</label> : <input type="text" name="num_client" /><BR>
                                <label>Num_emplacement</label> : <input type="text" name="num_emplacement" /><BR>
                                <label>date_deb_sejour</label> : <input type="text" name="date_deb_sejour" /><BR>
                                <label>Num_fin_sejour</label> : <input type="text" name="date_fin_sejour" /><BR>
                                                            </br></br></br>

                                        <input type="submit" value="Valider" />
                                </form>
                                </br>
                                <form action="reservations.py" method="">
					<input type="submit" value="Retour" />
                                        </br></br></br>
                            


                	</center></div>
                </body>





	</html>"""
print(Page)
