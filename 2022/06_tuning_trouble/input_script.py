import socket

# ESP32 IP address and port
ESP32_IP = "192.168.2.107"
ESP32_PORT = 12345

def connect_to_esp32():
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the ESP32 server
    client_socket.connect((ESP32_IP, ESP32_PORT))
    print(f"Connected to ESP32 at {ESP32_IP}:{ESP32_PORT}")

    # Send data to ESP32
    with open("input.txt") as f:
        message = f.read()
    client_socket.sendall(message.encode())
    print(f"Sent: {message.strip()}")

    # Receive echo from ESP32
    response = client_socket.recv(1024).decode()
    print(f"Received: {response}")

    # Close the connection
    client_socket.close()
    print("Connection closed")

# Run the function to connect to ESP32
connect_to_esp32()