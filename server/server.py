import json
import socket
import threading

HOST = ''
PORT = 5000

def handle_client(conn, addr):
    print(f"[+] Conexión establecida desde {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            # Decodificar mensaje JSON recibido
            mensaje_str = data.decode('utf-8')
            print(f"[Recibido] {mensaje_str}")
            
            try:
                peticion = json.loads(mensaje_str)
                msg_id = peticion.get("id", "desconocido")
                tipo = peticion.get("tipo", "")
                contenido = peticion.get("contenido", "")
                
                # Procesar según el tipo de solicitud
                respuesta_contenido = f"Procesado exitosamente: {contenido}"
                tipo_respuesta = "respuesta"
                
            except json.JSONDecodeError:
                msg_id = "error"
                tipo_respuesta = "error"
                respuesta_contenido = "Formato JSON inválido"

            # Construir respuesta en JSON
            respuesta = {
                "id": msg_id,
                "tipo": tipo_respuesta,
                "contenido": respuesta_contenido
            }
            
            conn.sendall(json.dumps(respuesta).encode('utf-8'))
            
    except Exception as e:
        print(f"[-] Error con el cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexión cerrada con {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Servidor escuchando en {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()