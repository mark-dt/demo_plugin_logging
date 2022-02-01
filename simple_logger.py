import logging
from logging.handlers import RotatingFileHandler
import os

    
def restore_logger(instance, log_level=None, logger=None):
    if logger == None:
        logger = logging.getLogger(__name__)

    var_log_path = '/var/log/dynatrace/oneagent/plugin'

    extension_path = instance.split('/')[-2]
    extension_log_path = os.path.join(var_log_path, extension_path)
    log_folder_created = True
    # if path does not exist try creating it
    if not os.path.isdir(extension_log_path):
        try:
            os.mkdir(extension_log_path)
        except Exception as e:
            log_folder_created = False

    log_file = instance.split('/')[-1].split('.')[0] + '.log'
    if log_folder_created:
        extension_log_file = os.path.join(extension_log_path, log_file)
    else:
        extension_log_file = os.path.join(var_log_path, log_file)

    if log_level == 'DEBUG':
        log_level = logging.DEBUG
    elif log_level == 'INFO':
        log_level = logging.INFO
    elif log_level == 'WARNING':
        log_level = logging.WARNING
    elif log_level == 'ERROR':
        log_level = logging.ERROR
    else:
        log_level = logging.DEBUG
    
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(funcName)s:%(lineno)d] %(message)s")
    logger.handlers = []
    rotating_handler = RotatingFileHandler(extension_log_file, maxBytes=1000000, backupCount=5)
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)
    logger.setLevel(log_level)
    logger.debug(f'FILENAME: {instance}')
    logger.debug(f'Log Level set to {log_level}')
    logger.debug(f'Extension log file: {extension_log_file}')
    logger.debug(f'Extension log path: {extension_log_path}')

    if not log_folder_created:
        logger.error('Could not create extension log folder')

    return logger


