import logging


def get_logger(name=None, level=logging.INFO):
    logging_format = "%(lineno)d in %(filename)s at %(asctime)s: %(message)s"
    logging.basicConfig(format=logging_format)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

