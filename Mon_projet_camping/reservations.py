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
                        <form action="identification_supplement.py" method="">
					<input type="submit" value="Commander un supplement" />
			</form>
			</br>
			<form action="identification_activite.py" method="">
					<input type="submit" value="s'inscrire dans une activite " />
			</form>
			</br>
			<form action="identification_emplacement.py" method="">
					<input type="submit" value="reserver un emplacement" />
			</form>
			</br>
			<form action="identification_menu.py" method="">
					<input type="submit" value="commander un menu" />
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
