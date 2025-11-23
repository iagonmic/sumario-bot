"""
Gera recomendações para cada dimensão.
"""

from utils.logger import get_logger

logger = get_logger("recommendations")

def generate_recommendations(dimensao: dict, analise: str) -> str:
    logger.info(f"Gerando recomendações para {dimensao['nome']}")

    # TODO: integrar com IA
    return f"Recomendações baseadas na análise da dimensão {dimensao['nome']}."
