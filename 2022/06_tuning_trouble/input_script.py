import serial
import time

ser = serial.Serial("COM4", 115200)

with open("input.txt") as file:
    for line in file:
        message = f"{line.strip()}\r\n".encode()
        ser.write(message)
        time.sleep(0.01)
        print(f"Sent message: {message}, response: {ser.readline()}")