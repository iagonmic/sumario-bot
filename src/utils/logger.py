import logging
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def get_logger(name: str) -> logging.Logger:
    """
    Retorna um logger configurado com base em variáveis de ambiente.
    LOG_LEVEL pode ser definido no .env.
    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
