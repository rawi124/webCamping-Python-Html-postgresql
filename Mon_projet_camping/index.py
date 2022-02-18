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
                        <form action="informations.py" method="">
					<input type="submit" value="Informations sur le camping" />
			</form>
			</br>
			<form action="listes.py" method="">
					<input type="submit" value="Ce que l'on propose" />
			</form>
			</br>
			<form action="inscriptions.py" method="">
					<input type="submit" value="Inscription au camping" />
			</form>
			</br>
			<form action="reservations.py" method="">
					<input type="submit" value="Reservations" />
			</form>
			</br>
			<form action="stats.py" method="">
					<input type="submit" value="Statistiques" />
			</form>
			</br></br>
			</div></center>
                </body>
        </html>"""
print(Page)
