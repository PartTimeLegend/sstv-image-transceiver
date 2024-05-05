import datetime

import sounddevice as sd

from serial_port import receive_data, send_data, set_frequency


def send_sstv_image(serial_port, image_data, frequency):
    try:
        send_data(serial_port, image_data)
        print("SSTV image transmitted successfully.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def receive_sstv_image(serial_port, frequency, save_recording=False):
    try:
        set_frequency(serial_port, frequency)
        duration = 5
        fs = 44100
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
        sd.wait()
        if save_recording:
            recording_file = f"received_recording_{frequency}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
            sd.write(recording_file, recording, fs)
            print(f"Recording saved as {recording_file}.")
        return receive_data(serial_port)
    except Exception as e:
        print(f"Error receiving image: {e}")
        return None
