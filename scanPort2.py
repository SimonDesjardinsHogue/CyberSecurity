import socket

target = input("Entrez l'adresse IP ou le nom d'hôte de la machine à scanner : ")

# Liste des ports à scanner
ports = [21, 22, 80, 443, 3389]

def scan_port(target, port):
    try:
        # Créer une socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Définir un délai de connexion court
        sock.settimeout(1)
        
        # Tente de se connecter au port
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Le port {port} est ouvert")
        else:
            print(f"Le port {port} est fermé")
        
        sock.close()
    except socket.error:
        print(f"Impossible de se connecter au port {port}")

# Balayage des ports
for port in ports:
    scan_port(target, port)
