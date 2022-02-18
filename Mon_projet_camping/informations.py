# coding: utf-8

import cgi

Page = """
<!doctype html>
		<html lang="fr">
				<head>
                        <meta charset = "utf-8">
                        <title>Informations</title>
                </head>
                <body background="images/wifii.jpg">
                	<center><div class="principale" style="background-image:url(images/blanc.png); width: 800px; border-color: #000000; border-style:solid; border-width: 5px; border-radius: 10px; opacity:0.850; margin-top: 50px;">
                		<h1>Informations du Camping</h1>
                		</br>
                		<p>Notre camping est specialement dedie a ceux qui cherchent de l inspiration au milieu de la nature et a ceux  qui veulent se detendre et s amuser dans une ambiance calme.</p>
                		</br>
                		<form action="index.py" method="">
						<input type="submit" value="Retour" />
						</br></br></br>



                	</center></div>
                </body>





	</html>"""
print(Page)
