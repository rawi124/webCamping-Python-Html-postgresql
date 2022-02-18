# coding: utf-8

import cgi

Page = """
<!doctype html>
        <html lang="fr">
                <head>
                        <meta charset = "utf-8">
                        <title>Le formulaire</title>
                </head>
                <body background="images/fond.jpg">
                        <center><div class="principale" style="background-image:url(images/blanc.png); width: 430px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                        <h1>Luxiours Camping</h1>
                        </br>
                        <form action="identification.py" method="">
					<input type="submit" value="S'inscrire" />
			</form>
			</br>
			<form action="identification_enfant.py" method="">
					<input type="submit" value="Inscription enfant" />
			</form>
			</br>
			<form action="view_client.py" method="">
					<input type="submit" value="Liste des clients" />
			</form>
			</br>
			<form action="view_enfant.py" method="">
					<input type="submit" value="Liste des enfants" />
			</form>
			</br>
			<form action="view_emplacement.py" method="">
					<input type="submit" value="Les sejours" />
			</form>
			</br>
			<form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form>
			</br></br>
			</div></center>
                </body>
        </html>"""
print(Page)
