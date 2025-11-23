"""
Extração das dimensões para processamento.
"""

from utils.logger import get_logger

logger = get_logger("dimensions")

def extract_dimensions(dados: dict) -> list:
    logger.info("Extraindo dimensões...")

    return dados.get("dimensoes", [])
