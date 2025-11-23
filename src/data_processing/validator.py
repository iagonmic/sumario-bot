"""
Validação da estrutura dos dados.
"""

from utils.logger import get_logger

logger = get_logger("validator")

def validate_data_structure(dados: dict):
    logger.info("Validando estrutura dos dados...")

    # TODO: adicionar todas as validações reais
    if "dimensoes" not in dados:
        raise ValueError("O arquivo de entrada não contém o campo 'dimensoes'.")

    logger.info("Estrutura validada com sucesso.")
