import serial
import time

def calculate_motor_speed(temp, hum):
    # Eenvoudige formule (pas aan naar wens)
    if temp > 30:
        return 255
    elif temp > 20:
        return 150
    else:
        return 50

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print("Ontvangen:", line)

                if "," in line:
                    temp_str, hum_str = line.split(",")
                    temp = float(temp_str)
                    hum = float(hum_str)

                    # Bepaal motorsnelheid op basis van temp/hum
                    speed = calculate_motor_speed(temp, hum)
                    print(f"Temp: {temp}°C, Luchtvochtigheid: {hum}%, Motor Snelheid: {speed}")

                    # Stuur snelheid naar Arduino
                    ser.write(f"{speed}\n".encode('utf-8'))

        except Exception as e:
            print("Fout:", e)

        time.sleep(2)
