# coding: utf-8

import cgi

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>inscription enfant</title>
                </head>
                <body background="images/fond.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 550px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Inscription enfant</h1>
                		</br>
                		<p>Si vous avez des enfants et que vous souhaitez les inscrire dans un camping autre que notre camping pendant que vous passez votre sejour chez nous avec votre conjoint ou un groupe de vos amis, vous pouvez le faire</p>
                		</br>
                        	<form action="insert_enfant.py" method="POST">
                                <label>Num_enfant</label> : <input type="text" name="num_enfant" /><BR>
                                <label>Nom_enfant</label> : <input type="text" name="nom_enfant" /><BR>
                                <label>Prenom_enfant</label> : <input type="text" name="prenom_enfant" /><BR>
                                <label>Sexe</label> : <input type="text" name="sexe" /><BR>
                                <label>Age</label> : <input type="text" name="age" /><BR>
                                <label>duree_sejour_enfant</label> : <input type="text" name="duree_sejour_enfant" /><BR>
                                <label>Num_client</label> : <input type="text" name="num_client" /><BR>

                                        						</br></br></br>

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
