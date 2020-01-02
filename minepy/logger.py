import logging
import config

logging.getLogger().setLevel(config.LOGGING_LEVEL)
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)