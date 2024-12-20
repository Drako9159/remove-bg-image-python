import os
import sys
from datetime import datetime
from rembg import remove
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BackgroundRemove:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def process_images(self):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        proccessed_folder = os.path.join(self.output_path, today)
        os.makedirs(proccessed_folder, exist_ok=True)
        for filename in os.listdir(self.input_path):
            if filename.endswith(('.png', 'jpg', 'jpeg')):
                input_path = os.path.join(self.input_path, filename)
                output_path = os.join(proccessed_folder, filename)
                self.remove_background(input_path, output_path)
                self.save_images(input_path, proccessed_folder)

    def remove_background(self, input_file, output_file):
        with open(input_file, 'rb') as inp, open(output_file, 'wb') as out:
            bg_output = remove(inp.read())
            out.write(bg_output)
        

    def save_images(self, input_file, output_file):
        originals_path = os.path.join(output_file, 'originals')
        os.makedirs(originals_path, exist_ok=True)

        filename = os.path.basename(input_file)
        new_path = os.path.join(originals_path, filename)
        os.rename(input_file, new_path)

        