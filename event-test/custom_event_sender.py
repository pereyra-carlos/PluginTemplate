import socket

def send_event(event_data):
    host = '127.0.0.1'
    port = 65432  # El puerto debe coincidir con el que está escuchando el servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(event_data.encode())
        print(f"Sent event: {event_data}")

if __name__ == "__main__":
    # Ejemplo de enviar eventos
    send_event("Hello from the event sender!")
    send_event("Another event data")
