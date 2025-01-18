import os
from datetime import datetime
from rembg import remove

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class BackgroundRemove:
    SUPPORTED_FORMATS = ('.png', 'jpg', 'jpeg', 'webp')

    def __init__(self, input_path = "input", output_path = "output"):
        self.input_path = input_path
        self.output_path = output_path

    def process_images(self):
        try:
            if not os.path.exists(self.input_path):
                raise FileNotFoundError(f"Input path {self.input_path} does not exist")

            today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            proccessed_folder = os.path.join(self.output_path, today)

            files_processed = 0
            files_with_error = 0

            for filename in os.listdir(self.input_path):
                if filename.endswith(self.SUPPORTED_FORMATS):
                    try:
                        os.makedirs(proccessed_folder, exist_ok=True)
                        input_path = os.path.join(self.input_path, filename)
                        output_path = os.path.join(proccessed_folder, filename)
                        self.remove_background(input_path, output_path)
                        self.save_images(input_path, proccessed_folder)
                        files_processed += 1
                        logging.info(f"File {filename} processed successfully")
                    except Exception as e:
                        files_with_error += 1
                        logging.error(f"Error processing file {filename}. Error: {e}")
                        continue
            logging.info(f"Files processed: {files_processed}")
        except Exception as e:
            logging.error(f"Error processing images. Error: {e}")
            raise

    def remove_background(self, input_file, output_file):
        try:
            with open(input_file, 'rb') as inp, open(output_file, 'wb') as out:
                bg_output = remove(inp.read())
                out.write(bg_output)
        except Exception as e:
            logging.error(f"Error processing file {input_file}. Error: {e}")
            raise
        
    def save_images(self, input_file, output_file):
        try:
            originals_path = os.path.join(output_file, 'originals')
            os.makedirs(originals_path, exist_ok=True)

            filename = os.path.basename(input_file)
            new_path = os.path.join(originals_path, filename)
            os.rename(input_file, new_path)
        except Exception as e:
            logging.error(f"Error saving file {input_file}. Error: {e}")
            raise
