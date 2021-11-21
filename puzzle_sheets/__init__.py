import logging

LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOGGING_LEVEL = logging.INFO
logging.basicConfig(format=LOGGING_FORMAT, level=LOGGING_LEVEL)
