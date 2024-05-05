import serial


def serial_port_factory(port):
    return serial.Serial(port, baudrate=9600, timeout=1)


def send_data(serial_port, data):
    try:
        with serial_port as ser:
            ser.write(data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def receive_data(serial_port):
    try:
        with serial_port as ser:
            return ser.read()
    except Exception as e:
        print(f"Error: {e}")
        return None


def set_frequency(serial_port, frequency):
    return send_data(serial_port, f"FREQ {frequency}\n".encode())
