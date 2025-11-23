"""
Carregamento de dados de entrada.
"""

import json
from utils.logger import get_logger

logger = get_logger("loader")

def load_input_data(path: str) -> dict:
    logger.info(f"Lendo dados de entrada: {path}")
    
    with open(path, "r", encoding="utf-8") as f:
        dados = json.load(f)

    return dados
