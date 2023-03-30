"Register all the logs"


import logging
import os
from datetime import datetime


# Log file name
LOG_FILE = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"

# Log directory name
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs")

# Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE)


# Create new log directory if not exists
os.makedirs(LOG_FILE_DIR, exist_ok=True)


# Registering the log into specified log file and directory
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s]", 
    level = logging.INFO
)