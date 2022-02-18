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
                        <form action="view_activite.py" method="">
					<input type="submit" value="Nombre activites reserves par client" />
			</form>
			</br>
			<form action="view_supplement.py" method="">
					<input type="submit" value="Nombre supplements commandes par client" />
			</form>
			</br>
			<form action="view_menu.py" method="">
					<input type="submit" value="Nombre menus commandes par client" />
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
