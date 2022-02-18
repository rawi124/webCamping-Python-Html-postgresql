# coding: utf-8

import cgi

Page = """
<!doctype html>
        <html lang="fr">
                <head>
                        <meta charset = "utf-8">
                        <title>Le formulaire</title>
                </head>
                <body background="images/tente.jpg">
                        <center><div class="principale" style="background-image:url(images/blanc.png); width: 430px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                        <h1>Luxiours Camping</h1>
                        </br>
                        <form action="emplacements.py" method="">
					<input type="submit" value="Emplacements" />
			</form>
			</br>
			<form action="activite.py" method="">
					<input type="submit" value="Activites" />
			</form>
			</br>
			<form action="supplement.py" method="">
					<input type="submit" value="Supplements" />
			</form>
			</br>
			<form action="restaurant.py" method="">
					<input type="submit" value="Carte Restaurant" />
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
