import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    value_to_send = 1

    while True:
        # Send integer to Arduino
        message = f"{value_to_send}\n"
        ser.write(message.encode('utf-8'))

        # Read response(s) from Arduino
        responses = []
        start_time = time.time()
        while time.time() - start_time < 1:  # Wait up to 1 second
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                if line:
                    responses.append(line)

        for response in responses:
            print(f"Raspberry Pi received: {response}")

        time.sleep(1)
