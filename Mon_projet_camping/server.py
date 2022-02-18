import http.server
PORT = 8888
server_adress = ("127.0.0.1", PORT)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)
httpd = server(server_adress, handler)
httpd.serve_forever()
