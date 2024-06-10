import serial

ser = serial.Serial("COM3", 9600)

with open("input.txt") as file:
    for line in file:
        message = f"{line.strip()}\r\n".encode()
        ser.write(message)
        print(f"Sent message: {message}, response: {ser.readline()}")