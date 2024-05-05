from PIL import Image
from datetime import datetime

def save_received_image(image_data, frequency):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"received_image_{frequency}_{timestamp}.jpg"
        with open(file_name, 'wb') as f:
            f.write(image_data)
        print(f"SSTV image received and saved successfully as {file_name}.")
        return file_name
    except Exception as e:
        print(f"Error: {e}")
        return None

def open_saved_image(file_name):
    try:
        received_image = Image.open(file_name)
        received_image.show()
    except Exception as e:
        print(f"Error opening image: {e}")
