# main.py

from time import sleep

from image_processing import open_saved_image, save_received_image
from serial_port import serial_port_factory
from sstv_image import receive_sstv_image, send_sstv_image


def transmit_sstv_image():
    image_path = input("Enter the path of the image file to transmit: ")
    serial_port = serial_port_factory(
        input("Enter the serial port (e.g., /dev/ttyUSB0): ")
    )
    frequency = input("Enter the frequency (e.g., 14230): ")
    with open(image_path, "rb") as f:
        image_data = f.read()
    if send_sstv_image(serial_port, image_data, frequency):
        resend = input(
            "Do you want to resend the image after a certain time interval? (Y/N): "
        ).upper()
        if resend == "Y":
            interval = float(input("Enter the time interval (in seconds): "))
            sleep(interval)
            transmit_sstv_image()


def receive_sstv_image_prompt():
    serial_port = serial_port_factory(
        input("Enter the serial port (e.g., /dev/ttyUSB0): ")
    )
    frequency = input("Enter the frequency (e.g., 14230): ")
    save_recording = (
        input("Do you want to save recorded WAV files? (Y/N): ").upper() == "Y"
    )
    image_data = receive_sstv_image(serial_port, frequency, save_recording)
    if image_data:
        file_name = save_received_image(image_data, frequency)
        if file_name:
            open_image = input(
                "Would you like to open the saved image? (Y/N): "
            ).upper()
            if open_image == "Y":
                open_saved_image(file_name)


def main():
    while True:
        choice = input("Select 'T' for transmit or 'R' for receive SSTV: ").upper()
        if choice == "T":
            transmit_sstv_image()
            break
        elif choice == "R":
            receive_sstv_image_prompt()
            break
        else:
            print("Invalid choice. Please select 'T' or 'R'.")


if __name__ == "__main__":
    main()
