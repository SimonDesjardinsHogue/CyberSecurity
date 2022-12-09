import socket

# Adresse IP et port cible
ip = "192.168.1.100"
port = 80

# Créer un socket et se connecter à l'adresse IP et au port cible
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))

# Si la connexion a réussi, le port est ouvert
if result == 0:
    print("Port {}: Open".format(port))
else:
    print("Port {}: Closed".format(port))

# Fermer le socket
sock.close()
