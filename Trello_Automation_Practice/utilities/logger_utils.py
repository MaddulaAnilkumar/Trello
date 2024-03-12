import inspect
import logging
from pathlib import Path
from utilities import file_utils
def get_logger(log_level=logging.INFO):
    root_path = str(Path(__file__).parent.parent)
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    file_utils.create_folder(root_path + '/logs/')
    file_handler = logging.FileHandler(root_path + '/logs/' + 'logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(log_level)
    return logger