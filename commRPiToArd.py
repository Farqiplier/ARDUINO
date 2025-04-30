import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        ser.write(b"1\n")  # Send the number 1
        time.sleep(0.5)

        if ser.in_waiting:
            response1 = ser.readline().decode('utf-8').strip()
            print(f"Received: {response1}")
        
        if ser.in_waiting:
            response2 = ser.readline().decode('utf-8').strip()
            print(f"Received: {response2}")
        
        time.sleep(1)
