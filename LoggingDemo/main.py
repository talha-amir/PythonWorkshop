import logging

# Gets or creates a logger
logging.basicConfig(
    filename="logfile.log",
    filemode="a",
    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - "
    "%(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.INFO,
)


# Logs
logging.debug('A debug message')
logging.info('An info message')
logging.warning('Something is not right.')
logging.error('A Major error has happened.')
logging.critical('Fatal error. Cannot continue')
