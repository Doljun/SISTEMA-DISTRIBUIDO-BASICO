import json
import socket
import sys
import time

# Recibirá la IP del servidor como argumento desde la terminal
SERVER_HOST = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
SERVER_PORT = 5000

def run_client(client_name):
    print(f"[{client_name}] Intentando conectar al servidor en {SERVER_HOST}:{SERVER_PORT}...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5.0)
    
    try:
        client.connect((SERVER_HOST, SERVER_PORT))
        print(f"[{client_name}] ¡Conectado con éxito!")
        
        mensaje = {
            "id": f"id-{client_name.lower()}-001",
            "tipo": "solicitud",
            "contenido": f"Hola desde el nodo independiente {client_name}"
        }
        
        client.sendall(json.dumps(mensaje).encode('utf-8'))
        print(f"[{client_name}] Mensaje enviado.")
        
        data = client.recv(1024)
        respuesta = json.loads(data.decode('utf-8'))
        print(f"[{client_name}] Respuesta del servidor:\n{json.dumps(respuesta, indent=2)}")
        
    except socket.timeout:
        print(f"[{client_name}] Error: Tiempo de espera agotado.")
    except Exception as e:
        print(f"[{client_name}] Error de conexión: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    name = sys.argv[2] if len(sys.argv) > 2 else "Cliente"
    run_client(name)