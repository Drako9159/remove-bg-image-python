#!/usr/bin/env python3
import logging
from utils.remove import BackgroundRemove


if __name__ == '__main__':
    try:
        bg_remove = BackgroundRemove()
        bg_remove.process_images()
    except Exception as e:
        logging.error(f"Error processing images. Error: {e}")
        raise
